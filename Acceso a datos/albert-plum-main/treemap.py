#!/usr/bin/env python3
import json
from plum import transform_for_d3_sunburst  # Importamos la función para reutilizar la transformación

def create_html_treemap_chart(data, html_file):
    """
    Crea un fichero HTML que muestra un treemap interactivo.
    Incluye un formulario de login (username/password ambos 'albert') y,
    tras autenticarse, muestra la visualización del treemap.
    """
    json_data = json.dumps(data)
    html_content = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Treemap Chart</title>
<style>
  /* ----- Reset & Body ----- */
  body {{
    font-family: "Open Sans", Arial, sans-serif;
    background: linear-gradient(135deg, #f4f7f9, #dce1e6);
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 20px;
  }}
  /* ----- Login Card ----- */
  .login-card {{
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
    max-width: 420px;
    width: 100%;
    padding: 35px;
    text-align: center;
    transition: transform 0.3s ease-in-out;
  }}
  .login-card:hover {{
    transform: translateY(-5px);
  }}
  .login-card h1 {{
    color: #2c3e50;
    font-size: 24px;
    margin-bottom: 20px;
  }}
  .login-card label {{
    display: block;
    text-align: left;
    font-weight: 600;
    color: #555;
    margin: 12px 0 5px;
  }}
  .login-card input[type="text"],
  .login-card input[type="password"] {{
    width: 100%;
    padding: 12px;
    border: 2px solid #dfe3e8;
    border-radius: 6px;
    font-size: 15px;
    transition: border 0.3s;
  }}
  .login-card input[type="text"]:focus,
  .login-card input[type="password"]:focus {{
    border-color: #3498db;
    outline: none;
  }}
  .login-card button {{
    background: #3498db;
    border: none;
    border-radius: 6px;
    width: 100%;
    padding: 14px;
    font-size: 17px;
    color: #fff;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.3s, transform 0.2s;
  }}
  .login-card button:hover {{
    background: #2980b9;
    transform: scale(1.05);
  }}
  .error-msg {{
    color: #c0392b;
    font-weight: 600;
    margin-top: 10px;
  }}
  /* ----- Treemap Container ----- */
  #treemap-container {{
    display: none;
    width: 90%;
    max-width: 1000px;
    margin: 30px auto;
    position: relative;
  }}
  .chart-title {{
    font-size: 26px;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 20px;
    text-align: center;
  }}
  /* Estilos para los nodos del treemap */
  .node {{
    border: 1px solid #fff;
    font: 10px sans-serif;
    line-height: 12px;
    overflow: hidden;
    position: absolute;
    text-align: center;
  }}
</style>
</head>
<body>
<div class="center-container">
  <!-- LOGIN FORM -->
  <div class="login-card" id="login-card">
    <h1>Login</h1>
    <label for="username">Username</label>
    <input type="text" id="username" placeholder="Username" />
    <label for="password">Password</label>
    <input type="password" id="password" placeholder="Password" />
    <button onclick="attemptLogin()">Sign In</button>
    <div class="error-msg" id="error-msg"></div>
  </div>

  <!-- TREEMAP CONTAINER (hidden until login) -->
  <div id="treemap-container">
    <div class="chart-title">Interactive Treemap Chart</div>
    <div id="treemap"></div>
  </div>
</div>

<!-- Incluimos D3.js -->
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
  const VALID_USER = "albert";
  const VALID_PASS = "albert";
  const data = {json_data};

  function attemptLogin() {{
    const userField = document.getElementById("username");
    const passField = document.getElementById("password");
    const errMsg    = document.getElementById("error-msg");

    if (userField.value === VALID_USER && passField.value === VALID_PASS) {{
      document.getElementById("login-card").style.display = "none";
      document.getElementById("treemap-container").style.display = "block";
      initTreemap();
    }} else {{
      errMsg.textContent = "Invalid username or password";
    }}
  }}

  function initTreemap() {{
    const width = 960;
    const height = 600;

    const root = d3.hierarchy(data)
      .sum(d => d.value || 0)
      .sort((a, b) => b.value - a.value);

    d3.treemap()
      .size([width, height])
      .padding(1)
      (root);

    const color = d3.scaleOrdinal(d3.schemeCategory10);

    const container = d3.select("#treemap")
      .style("position", "relative")
      .style("width", width + "px")
      .style("height", height + "px")
      .style("margin", "0 auto");

    container.selectAll(".node")
      .data(root.leaves())
      .enter().append("div")
      .attr("class", "node")
      .style("left", d => d.x0 + "px")
      .style("top", d => d.y0 + "px")
      .style("width", d => (d.x1 - d.x0) + "px")
      .style("height", d => (d.y1 - d.y0) + "px")
      .style("background", d => color(d.parent.data.name))
      .text(d => d.data.name);
  }}
</script>
</body>
</html>
"""
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

def main():
    # Directorio raíz (debe coincidir con el usado en plum.py)
    root_dir = "/xampp/htdocs"
    output_file = "file_structure.json"  # Se asume que ya existe, generado por plum.py
    treemap_html_file = "file_structure_treemap.html"

    print(f"Leyendo estructura de ficheros desde {output_file}...")
    with open(output_file, "r", encoding="utf-8") as f:
        file_structure = json.load(f)

    print("Transformando datos para el treemap...")
    # Utilizamos la misma transformación que para el sunburst
    d3_data = transform_for_d3_sunburst(file_structure, parent_name=root_dir)

    print(f"Creando fichero HTML del treemap en {treemap_html_file}...")
    create_html_treemap_chart(d3_data, treemap_html_file)
    print(f"Fichero HTML del treemap guardado en {treemap_html_file}")

if __name__ == "__main__":
    main()
