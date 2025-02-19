<?php
session_start();

// Credenciales de acceso
$VALID_USERNAME = 'albert';
$VALID_PASSWORD = 'albert';

// Logout
if (isset($_GET['action']) && $_GET['action'] === 'logout') {
    session_unset();
    session_destroy();
    header("Location: index.php");
    exit;
}

// Manejo del login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';
    if ($username === $VALID_USERNAME && $password === $VALID_PASSWORD) {
        $_SESSION['loggedin'] = true;
        $_SESSION['username'] = $username;
        header("Location: index.php");
        exit;
    } else {
        $error = "Usuario o contraseña inválidos.";
    }
}

$loggedIn = $_SESSION['loggedin'] ?? false;

// Obtener imágenes de una carpeta
function getImages($folder) {
    $images = [];
    if (is_dir($folder)) {
        $files = array_diff(scandir($folder), array('.', '..'));
        foreach ($files as $file) {
            if (preg_match('/\.(jpg|jpeg|png|gif)$/i', $file)) {
                $images[] = $file;
            }
        }
    }
    return $images;
}

// Carpeta de imágenes
$chartFolder = 'img/hourly';
$images = $loggedIn ? getImages($chartFolder) : [];
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Albert | Tomata</title>
    <link rel="icon" href="tomata.png">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    body {
        font-family: 'Roboto', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: rgb(182, 165, 15);
        color: white;
        min-height: 100vh;
    }

    /* Header */
    .header {
        background-color: rgb(182, 165, 15);
        width: 100%;
        padding: 15px 30px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 100;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .header .app-name {
        font-size: 1.5rem;
        font-weight: bold;
        display: flex;
        align-items: center;
    }
    .header .app-name img {
        width: 50px;
        margin-right: 20px;
    }
    .header .logout-button {
        background-color: rgb(182, 165, 15);
        color: white;
        border: 2px solid white;
        padding: 8px 16px;
        border-radius: 25px;
        cursor: pointer;
        text-decoration: none;
        font-size: 1rem;
        transition: background-color 0.3s, border-color 0.3s;
    }
    .header .logout-button:hover {
        background-color: #311b92;
        border-color: #311b92;
    }

    /* Sidebar */
    .sidebar {
        width: 250px;
        background: rgba(255,255,255,0.1);
        padding: 20px;
        border-right: 1px solid rgba(255,255,255,0.2);
        position: fixed;
        top: 70px;
        bottom: 0;
        overflow-y: auto;
    }
    .sidebar h3 {
        margin-bottom: 20px;
        color: white;
        font-size: 1.2rem;
    }
    .sidebar a {
        display: block;
        padding: 12px 16px;
        margin: 8px 0;
        color: rgba(255,255,255,0.9);
        text-decoration: none;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .sidebar a:hover, .sidebar a.active {
        background-color: rgba(255,255,255,0.2);
    }

    /* Contenido principal */
    .content {
        flex: 1;
        padding: 20px;
        overflow-y: auto;
        margin-top: 70px;
        margin-left: 270px;
    }
    .dashboard {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
    }
    .image-card {
        text-align: center;
        background: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.2s;
    }
    .image-card:hover {
        transform: translateY(-3px);
    }
    .image-card img {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
        cursor: pointer;
    }

    /* Estado del Hardware */
    .hardware-status {
        background: rgba(0,0,0,0.1);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .hardware-status h3 {
        margin-bottom: 15px;
    }
    .hardware-metric {
        display: flex;
        justify-content: space-between;
        padding: 10px;
        margin: 8px 0;
        background: rgba(255,255,255,0.05);
        border-radius: 5px;
    }
    .metric-label {
        font-weight: 300;
    }
    .metric-value {
        font-weight: 500;
        color: rgb(255, 223, 0);
    }

    /* Reporte Diario */
    .daily-report {
        background: rgba(0,0,0,0.1);
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .daily-report h3 {
        margin-bottom: 15px;
    }
    .report-metrics {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
    }
    .report-metric {
        background: rgba(255,255,255,0.05);
        padding: 15px;
        border-radius: 8px;
        text-align: center;
    }
    .report-metric h4 {
        margin-bottom: 10px;
        font-weight: 400;
    }
    .report-metric p {
        font-size: 1.4rem;
        font-weight: bold;
        color: rgb(255, 223, 0);
    }

    /* Login */
    .login-container {
        background: rgba(255,255,255,0.1);
        padding: 40px 30px;
        max-width: 400px;
        width: 90%;
        margin: 100px auto;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        text-align: center;
    }
    .login-container input {
        width: 100%;
        padding: 10px 12px;
        margin-bottom: 20px;
        background: rgba(255,255,255,0.9);
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 5px;
        font-size: 1rem;
    }
    .login-container button {
        width: 100%;
        padding: 12px;
        background-color: rgba(255,255,255,0.9);
        border: none;
        color: rgb(182, 165, 15);
        font-size: 1rem;
        font-weight: 500;
        border-radius: 25px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .login-container button:hover {
        background-color: white;
    }
    </style>
</head>
<body>
    <?php if ($loggedIn): ?>
        <div class="header">
            <div class="app-name"><img src="tomata.png">Albert | Tomata</div>
            <a href="index.php?action=logout" class="logout-button">Cerrar Sesión</a>
        </div>

        <div class="sidebar">
            <h3>Gráficas</h3>
            <a href="index.php?type=hourly">Última Hora</a>
        </div>

        <div class="content">
            <!-- Estado del Hardware -->
            <div class="hardware-status">
                <h3>Estado del Hardware</h3>
                <?php
                $hardware_file = 'hardware_status.txt';
                if (file_exists($hardware_file) && is_readable($hardware_file)) {
                    $hardware_info = file($hardware_file);
                    foreach ($hardware_info as $line) {
                        $parts = explode(':', $line, 2);
                        if (count($parts) === 2) {
                            echo '<div class="hardware-metric">';
                            echo '<span class="metric-label">'.trim($parts[0]).'</span>';
                            echo '<span class="metric-value">'.trim($parts[1]).'</span>';
                            echo '</div>';
                        }
                    }
                } else {
                    echo '<p>Información de hardware no disponible temporalmente</p>';
                }
                ?>
            </div>

            <!-- Reporte Diario -->
            <div class="daily-report">
                <?php
                $report_file = 'daily_report.html';
                if (file_exists($report_file) && is_readable($report_file)) {
                    include $report_file;
                } else {
                    echo '<p>El reporte diario se generará automáticamente cada 24 horas</p>';
                }
                ?>
            </div>

            <!-- Gráficas -->
            <div class="dashboard">
                <?php if (!empty($images)): ?>
                    <?php foreach ($images as $image): ?>
                        <div class="image-card">
                            <a href="<?= $chartFolder . '/' . $image ?>" download>
                                <img src="<?= $chartFolder . '/' . $image ?>" alt="Chart">
                            </a>
                        </div>
                    <?php endforeach; ?>
                <?php else: ?>
                    <p>No hay gráficas disponibles actualmente</p>
                <?php endif; ?>
            </div>
        </div>
    <?php else: ?>
        <div class="login-container">
            <h2>Iniciar Sesión</h2>
            <?php if (isset($error)): ?>
                <p style="color: #ff4444; margin-bottom: 15px;"><?= $error ?></p>
            <?php endif; ?>
            <form action="index.php" method="post">
                <input type="text" name="username" required placeholder="Usuario">
                <input type="password" name="password" required placeholder="Contraseña">
                <button type="submit" name="login">Entrar</button>
            </form>
        </div>
    <?php endif; ?>
</body>
</html>