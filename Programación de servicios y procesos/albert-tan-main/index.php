<!doctype html>
<html>
    <head>
        <script defer src="jocarsa-tan.js"></script>
        <style>
            table tbody tr td { text-align: center; padding: 10px; }
            .controls { margin: 20px 0; }
        </style>
    </head>
    <body>
        <?php
            $columnas = 8;
            $filas = 16;
        ?>
        <h1>Una tabla</h1>
        <div class="controls">
            <label for="startColor">Color Inicial:</label>
            <input type="range" id="startColor" name="startColor" min="0" max="360" value="0">
            <span id="startColorValue">0</span>
            <br>
            <label for="endColor">Color Final:</label>
            <input type="range" id="endColor" name="endColor" min="0" max="360" value="120">
            <span id="endColorValue">120</span>
        </div>
        <table class="jocarsa-tan" style="color:rgb(234,0,0);background:rgb(0,255,0);">
            <thead>
                <tr>
                    <?php
                        for($i = 0; $i < $columnas; $i++){
                            echo '<th>'.$i.'</th>';
                        }
                    ?>
                </tr>
            </thead>
            <tbody>
                <?php
                    for($i = 0; $i < $filas; $i++){
                        echo '<tr>';
                        for($j = 0; $j < $columnas; $j++){
                            echo '<td>'.rand(1,500).'</td>';
                        }
                        echo '</tr>';
                    }
                ?>
            </tbody>
        </table>
        <h1>Otra tabla</h1>
        <table>
            <thead>
                <tr>
                    <?php
                        for($i = 0; $i < $columnas; $i++){
                            echo '<th>'.$i.'</th>';
                        }
                    ?>
                </tr>
            </thead>
            <tbody>
                <?php
                    for($i = 0; $i < $filas; $i++){
                        echo '<tr>';
                        for($j = 0; $j < $columnas; $j++){
                            echo '<td>'.rand(1,500).'</td>';
                        }
                        echo '</tr>';
                    }
                ?>
            </tbody>
        </table>
    </body>
</html>
