document.addEventListener("DOMContentLoaded", function () {
    const tabla = document.querySelector(".jvtabla");
    const tbody = tabla.querySelector("tbody");
    const buscador = document.getElementById("buscador");
    const indices = [];
    let contenido = [];

    // Cargar datos del archivo XML
    function cargarDatosDesdeXML() {
        fetch("data.xml") // Ruta al archivo XML
            .then((response) => response.text())
            .then((xmlString) => {
                const parser = new DOMParser();
                const xmlDoc = parser.parseFromString(xmlString, "text/xml");

                // Obtener los elementos de fila del XML
                const filas = xmlDoc.getElementsByTagName("row");

                contenido = Array.from(filas).map((fila) => {
                    const linea = {};
                    Array.from(fila.children).forEach((campo) => {
                        linea[campo.tagName] = campo.textContent.trim();
                    });
                    return linea;
                });

                poblarTabla();
            })
            .catch((error) => console.error("Error al cargar el archivo XML:", error));
    }

    // Poblar la tabla con los datos cargados
    function poblarTabla(filtradoContenido = contenido) {
        tbody.innerHTML = ""; // Limpiar el cuerpo de la tabla

        filtradoContenido.forEach((linea) => {
            const fila = document.createElement("tr");

            Object.keys(linea).forEach((campo) => {
                if (!indices.includes(campo)) indices.push(campo); // Añadir campo a índices si no existe
                const celda = document.createElement("td");
                celda.textContent = linea[campo];
                fila.appendChild(celda);
            });

            tbody.appendChild(fila);
        });

        actualizarCabeceras();
    }

    // Actualizar cabeceras para incluir funcionalidad de ordenación
    function actualizarCabeceras() {
        const cabeceras = tabla.querySelectorAll("thead th");
        cabeceras.forEach((cabecera, colIndex) => {
            cabecera.onclick = function () {
                contenido.sort((a, b) => {
                    const valA = a[indices[colIndex]].toLowerCase();
                    const valB = b[indices[colIndex]].toLowerCase();
                    if (!isNaN(valA) && !isNaN(valB)) {
                        return parseFloat(valA) - parseFloat(valB);
                    }
                    return valA > valB ? 1 : valA < valB ? -1 : 0;
                });
                poblarTabla();
            };
        });
    }

    // Filtrar filas en función del texto de búsqueda (solo ID y Name)
    buscador.addEventListener("input", function () {
        const textoBusqueda = buscador.value.toLowerCase();

        const filtradoContenido = contenido.filter((linea) => {
            const id = linea["ID"] ? linea["ID"].toLowerCase() : "";
            const name = linea["Name"] ? linea["Name"].toLowerCase() : "";
            return id.includes(textoBusqueda) || name.includes(textoBusqueda);
        });

        poblarTabla(filtradoContenido);
    });

    // Exportar tabla a CSV
    document.getElementById("exportCSV").onclick = function () {
        const csvContent = contenido.map((linea) =>
            indices.map((campo) => `"${linea[campo] || ""}"`).join(",")
        );
        csvContent.unshift(indices.join(",")); // Añadir cabeceras
        const blob = new Blob([csvContent.join("\n")], { type: "text/csv" });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.download = "tabla.csv";
        link.click();
    };

    // Iniciar cargando datos desde XML
    cargarDatosDesdeXML();
});

