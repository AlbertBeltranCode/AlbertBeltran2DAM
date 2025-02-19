import matplotlib.pyplot as plt
import psutil
import time
import os
import subprocess
from datetime import datetime, timedelta
import numpy as np

# ========== CONFIGURACIÓN DE RUTAS ==========
base_path = r"C:\xampp\htdocs\DAM2\AlbertBeltran2DAM\Desarrollo de interfaces\007-Distribución de aplicaciones\tomato-local"
data_paths = {
    "hourly": os.path.join(base_path, "carga_hourly.txt"),
}
plot_folders = {
    "hourly": os.path.join(base_path, "img/hourly"),
}

# ========== FUNCIONES PRINCIPALES ==========
def trim_data(data, time_window_seconds):
    """Filtra datos dentro de la ventana temporal"""
    now = datetime.now()
    return [entry for entry in data if (now - entry[0]).total_seconds() <= time_window_seconds]

def load_data(file_path):
    """Carga datos desde archivo"""
    try:
        with open(file_path, 'r') as f:
            return [
                (datetime.fromisoformat(row[0]), *map(float, row[1:]))
                for row in (line.strip().split(',') for line in f if line.strip())
            ]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error cargando datos: {str(e)}")
        return []

def save_data(file_path, data):
    """Guarda datos en archivo con manejo de errores"""
    try:
        with open(file_path, 'w') as f:
            for row in data:
                f.write(','.join(map(str, [row[0].isoformat()] + list(row[1:]))) + '\n')
    except Exception as e:
        print(f"Error guardando datos: {str(e)}")

def measure_metrics():
    """Mide las métricas del sistema"""
    try:
        carga_cpu = psutil.cpu_percent(interval=1)
        carga_ram = psutil.virtual_memory().percent
        uso_disco = psutil.disk_usage('/').percent
        data_inicio = psutil.net_io_counters()
        time.sleep(1)
        data_final = psutil.net_io_counters()
        return (
            datetime.now(),
            carga_cpu,
            carga_ram,
            uso_disco,
            (data_final.bytes_recv - data_inicio.bytes_recv) / (1024 * 1024),
            (data_final.bytes_sent - data_inicio.bytes_sent) / (1024 * 1024),
            45.0,
            len(psutil.net_connections()),
        )
    except Exception as e:
        print(f"Error midiendo métricas: {str(e)}")
        return None

# ========== NUEVAS FUNCIONALIDADES ==========
def get_hardware_info():
    """Monitorea la salud del hardware"""
    hw_info = {
        'cpu_temp': 'N/A',
        'disk_health': 'Buen estado',
        'battery': 'N/A',
        'system_status': 'Estable'
    }
    
    try:
        import wmi
        w = wmi.WMI()
        
        # Estado del disco
        disk_issues = 0
        for disk in w.Win32_DiskDrive():
            if disk.Status != 'OK':
                disk_issues += 1
        if disk_issues > 0:
            hw_info['disk_health'] = f'{disk_issues} advertencias'
            
        # Batería
        batteries = w.Win32_Battery()
        if batteries:
            hw_info['battery'] = f'{batteries[0].EstimatedChargeRemaining}% restante'
            
    except ImportError:
        print("Instale el módulo wmi: pip install wmi")
    except Exception as e:
        print(f"Error hardware: {str(e)}")
        hw_info['system_status'] = 'Error de monitorización'
    
    # Guardar información
    hardware_file = os.path.join(base_path, "hardware_status.txt")
    try:
        with open(hardware_file, 'w') as f:
            for k, v in hw_info.items():
                f.write(f"{k}: {v}\n")
    except Exception as e:
        print(f"Error guardando hardware_status: {str(e)}")

def generate_daily_report():
    """Genera reporte diario con manejo de errores"""
    report_file = os.path.join(base_path, "daily_report.html")
    try:
        # Datos básicos
        report_data = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'max_cpu': 0,
            'avg_ram': 0,
            'total_network': 0,
            'incidents': 0
        }
        
        # Calcular métricas
        if data_buffers["hourly"]:
            cpu_values = [row[1] for row in data_buffers["hourly"]]
            ram_values = [row[2] for row in data_buffers["hourly"]]
            
            report_data['max_cpu'] = max(cpu_values)
            report_data['avg_ram'] = sum(ram_values) / len(ram_values)
            report_data['total_network'] = sum(row[4] + row[5] for row in data_buffers["hourly"])
        
        # Contar incidentes
        try:
            with open(os.path.join(base_path, "anomalies.txt"), 'r') as f:
                report_data['incidents'] = len(f.readlines())
        except:
            pass
        
        # Generar HTML
        html_content = f"""
        <div class="daily-report">
            <h3>Reporte Diario - {report_data['date']}</h3>
            <div class="metrics">
                <div class="metric">
                    <span class="label">CPU Máximo:</span>
                    <span class="value">{report_data['max_cpu']:.1f}%</span>
                </div>
                <div class="metric">
                    <span class="label">RAM Promedio:</span>
                    <span class="value">{report_data['avg_ram']:.1f}%</span>
                </div>
                <div class="metric">
                    <span class="label">Tráfico Total:</span>
                    <span class="value">{report_data['total_network']:.2f} MB</span>
                </div>
                <div class="metric">
                    <span class="label">Incidentes:</span>
                    <span class="value">{report_data['incidents']}</span>
                </div>
            </div>
        </div>
        """
        
        with open(report_file, 'w') as f:
            f.write(html_content)
            
    except Exception as e:
        print(f"Error generando reporte: {str(e)}")
        with open(report_file, 'w') as f:
            f.write("<div class='daily-report-error'>Reporte no disponible temporalmente</div>")

# ========== EJECUCIÓN PRINCIPAL ==========
# Crear carpetas necesarias
for folder in plot_folders.values():
    os.makedirs(folder, exist_ok=True)

# Cargar datos existentes
data_buffers = {key: load_data(path) for key, path in data_paths.items()}

# Medición y almacenamiento de métricas
new_entry = measure_metrics()
if new_entry:
    data_buffers["hourly"].append(new_entry)
    data_buffers["hourly"] = trim_data(data_buffers["hourly"], 3600)

# Guardar datos actualizados
for key, path in data_paths.items():
    save_data(path, data_buffers[key])

# Función para generar gráficas
def generate_plot(data, index, title, ylabel, save_path, ylim=None):
    if not data:
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot([row[0] for row in data], [row[index] for row in data], marker='o')
    plt.title(title)
    plt.ylabel(ylabel)
    if ylim:
        plt.ylim(ylim)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

# Configuración de gráficas (actualizada)
plot_configs = [
    (1, 'Uso de CPU', '%', (0, 100)),
    (2, 'Uso de RAM', '%', (0, 100)),
    (3, 'Uso de Disco', '%', (0, 100)),
    (4, 'Ancho de Banda - Descarga', 'Mbps', None),
    (5, 'Ancho de Banda - Subida', 'Mbps', None),
]

# Generar gráficas (loop corregido)
for config in plot_configs:
    index, title, ylabel, ylim = config
    save_path = os.path.join(
        plot_folders["hourly"], 
        f"{title.lower().replace(' ', '_')}_hourly.jpg"
    )
    generate_plot(
        data=data_buffers["hourly"],
        index=index,
        title=title,
        ylabel=ylabel,
        save_path=save_path,
        ylim=ylim
    )

# Ejecutar nuevas funcionalidades
get_hardware_info()

# Generar reporte diario a las 23:59
if datetime.now().hour == 23 and datetime.now().minute >= 55:
    generate_daily_report()

print("Monitorización completada correctamente.")
