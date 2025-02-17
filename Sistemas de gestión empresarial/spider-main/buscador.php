<?php
// Conectar a la base de datos SQLite
$db = new PDO('sqlite:targets.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Definir el número de resultados por página
$resultsPerPage = 10;

// Obtener el número total de registros
$searchQuery = '';
if (isset($_GET['search'])) {
    $searchQuery = $_GET['search'];
    // Preparar y ejecutar la consulta de búsqueda
    $stmt = $db->prepare('SELECT COUNT(*) FROM target_attributes WHERE target LIKE :searchQuery');
    $stmt->execute([':searchQuery' => '%' . $searchQuery . '%']);
    $totalRecords = $stmt->fetchColumn();
} else {
    // Si no hay búsqueda, seleccionar todos los registros
    $stmt = $db->query('SELECT COUNT(*) FROM target_attributes');
    $totalRecords = $stmt->fetchColumn();
}

// Calcular el número total de páginas
$totalPages = ceil($totalRecords / $resultsPerPage);

// Obtener la página actual desde la URL, o establecer la primera página por defecto
$page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
$page = max($page, 1); // Asegurar que la página sea al menos 1
$page = min($page, $totalPages); // Asegurar que la página no exceda el total de páginas

// Calcular el desplazamiento (offset)
$offset = ($page - 1) * $resultsPerPage;

// Preparar y ejecutar la consulta de búsqueda con paginación
if ($searchQuery) {
    $stmt = $db->prepare('SELECT target FROM target_attributes WHERE target LIKE :searchQuery LIMIT :offset, :resultsPerPage');
    $stmt->bindValue(':searchQuery', '%' . $searchQuery . '%', PDO::PARAM_STR);
    $stmt->bindValue(':offset', $offset, PDO::PARAM_INT);
    $stmt->bindValue(':resultsPerPage', $resultsPerPage, PDO::PARAM_INT);
} else {
    // Si no hay búsqueda, seleccionar todos los registros con paginación
    $stmt = $db->prepare('SELECT target FROM target_attributes LIMIT :offset, :resultsPerPage');
    $stmt->bindValue(':offset', $offset, PDO::PARAM_INT);
    $stmt->bindValue(':resultsPerPage', $resultsPerPage, PDO::PARAM_INT);
}
$stmt->execute();
$results = $stmt->fetchAll(PDO::FETCH_ASSOC);

// Función para convertir texto en enlaces
function convertUrlsToLinks($text) {
    // Expresión regular para encontrar URLs
    $pattern = '/(https?:\/\/[^\s]+)/';
    // Reemplazar las URLs por enlaces HTML
    $replacement = '<a href="$1" target="_blank">$1</a>';
    return preg_replace($pattern, $replacement, $text);
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Buscador de Targets</title>
    <link rel="stylesheet" href="estilo.css">
</head>
<body>
    <h1>Buscador de Targets</h1>
    <form method="get" action="">
        <input type="text" name="search" placeholder="Buscar..." value="<?php echo htmlspecialchars($searchQuery); ?>">
        <button type="submit">Buscar</button>
    </form>

    <?php if ($searchQuery): ?>
        <h2>Resultados de búsqueda para "<?php echo htmlspecialchars($searchQuery); ?>"</h2>
    <?php else: ?>
        <h2>Todos los Targets</h2>
    <?php endif; ?>

    <?php if ($results): ?>
        <ul>
            <?php foreach ($results as $row): ?>
                <li><?php echo convertUrlsToLinks(htmlspecialchars($row['target'])); ?></li>
            <?php endforeach; ?>
        </ul>

        <!-- Paginación -->
        <div class="pagination">
            <?php if ($page > 1): ?>
                <a href="?page=1<?php echo $searchQuery ? '&search=' . urlencode($searchQuery) : ''; ?>">Primera</a>
                <a href="?page=<?php echo $page - 1; ?><?php echo $searchQuery ? '&search=' . urlencode($searchQuery) : ''; ?>">Anterior</a>
            <?php endif; ?>

            <span>Página <?php echo $page; ?> de <?php echo $totalPages; ?></span>

            <?php if ($page < $totalPages): ?>
                <a href="?page=<?php echo $page + 1; ?><?php echo $searchQuery ? '&search=' . urlencode($searchQuery) : ''; ?>">Siguiente</a>
                <a href="?page=<?php echo $totalPages; ?><?php echo $searchQuery ? '&search=' . urlencode($searchQuery) : ''; ?>">Última</a>
            <?php endif; ?>
        </div>
    <?php else: ?>
        <p>No se encontraron resultados.</p>
    <?php endif; ?>
</body>
</html>
