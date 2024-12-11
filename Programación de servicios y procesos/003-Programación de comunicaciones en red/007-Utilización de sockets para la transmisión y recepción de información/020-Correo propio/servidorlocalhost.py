from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from funcioncorreolocalhost import enviar, recibir, recibir_por_fecha

app = Flask(__name__)
CORS(app, origins="*")  # Permitir solicitudes desde cualquier origen  # Configuración básica de CORS para permitir peticiones desde cualquier origen

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar_email():
    try:
        data = request.get_json()
        print(f"Datos recibidos: {data}")  # Imprimir los datos recibidos
        asunto = data.get("asunto")
        para = data.get("para")
        mensaje = data.get("mensaje")
        
        if not asunto or not para or not mensaje:
            return jsonify({"error": "Faltan datos necesarios"}), 400

        resultado = enviar("localhost@example.com", para, asunto, mensaje)
        return jsonify({"mensaje": "Correo enviado con éxito", "resultado": resultado}), 200
    except Exception as e:
        print(f"Error al enviar el correo: {e}")  # Mostrar el error completo
        return jsonify({"error": "No se pudo enviar el correo", "detalle": str(e)}), 500


@app.route("/recibir")
def recibir_email():
    try:
        correos = recibir()
        return jsonify(correos), 200
    except Exception as e:
        return jsonify({"error": "No se pudieron recuperar los correos", "detalle": str(e)}), 500

@app.route("/recibir_por_fecha/<fecha>")
def recibir_email_por_fecha(fecha):
    try:
        correo = recibir_por_fecha(fecha)
        if correo:
            return jsonify(correo), 200
        else:
            return jsonify({"mensaje": "Correo no encontrado para la fecha especificada"}), 404
    except Exception as e:
        return jsonify({"error": "No se pudo recuperar el correo", "detalle": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

    #Para arrancar el servidor iniciar un power shell en la carpeta del proyecto y ejecutar python servidorlocalhost.py