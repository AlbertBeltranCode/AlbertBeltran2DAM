document.addEventListener('DOMContentLoaded', function() {
    // Función auxiliar para convertir RGB a HSL
    function rgbToHsl(rgbString) {
        const match = rgbString.match(/^rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$/);
        if (!match) {
            throw new Error("Formato RGB inválido. Use el formato 'rgb(x, y, z)'.");
        }

        let r = parseInt(match[1], 10);
        let g = parseInt(match[2], 10);
        let b = parseInt(match[3], 10);

        r /= 255;
        g /= 255;
        b /= 255;

        const max = Math.max(r, g, b);
        const min = Math.min(r, g, b);

        let h, s, l = (max + min) / 2;

        if (max === min) {
            h = s = 0; // achromático
        } else {
            const delta = max - min;
            s = l > 0.5 ? delta / (2 - max - min) : delta / (max + min);
            switch (max) {
                case r:
                    h = (g - b) / delta + (g < b ? 6 : 0);
                    break;
                case g:
                    h = (b - r) / delta + 2;
                    break;
                case b:
                    h = (r - g) / delta + 4;
                    break;
            }
            h /= 6;
        }

        h = Math.round(h * 360); // Tono en grados
        s = Math.round(s * 100); // Saturación en porcentaje
        l = Math.round(l * 100); // Luminosidad en porcentaje

        return `hsl(${h}, ${s}%, ${l}%)`;
    }

    // Función auxiliar para interpolar entre dos colores HSL
    function interpolateHsl(hsl1, hsl2, percentage) {
        const match1 = hsl1.match(/^hsl\((\d{1,3}),\s*(\d{1,3})%,\s*(\d{1,3})%\)$/);
        const match2 = hsl2.match(/^hsl\((\d{1,3}),\s*(\d{1,3})%,\s*(\d{1,3})%\)$/);

        if (!match1 || !match2) {
            throw new Error("Formato HSL inválido para la interpolación.");
        }

        let h1 = parseInt(match1[1], 10);
        let s1 = parseInt(match1[2], 10);
        let l1 = parseInt(match1[3], 10);

        let h2 = parseInt(match2[1], 10);
        let s2 = parseInt(match2[2], 10);
        let l2 = parseInt(match2[3], 10);

        let deltaH = h2 - h1;
        if (deltaH > 180) deltaH -= 360;
        if (deltaH < -180) deltaH += 360;
        let h = (h1 + percentage * deltaH) % 360;
        if (h < 0) h += 360;

        let s = s1 + percentage * (s2 - s1);
        let l = l1 + percentage * (l2 - l1);

        return `hsl(${Math.round(h)}, ${Math.round(s)}%, ${Math.round(l)}%)`;
    }

    // Función principal para actualizar los colores de la tabla
    function updateTableColors() {
        const tablas = document.querySelectorAll(".jocarsa-tan");
        const startColorInput = document.getElementById('startColor');
        const endColorInput = document.getElementById('endColor');

        if (!startColorInput || !endColorInput) {
            console.error('No se encontraron los elementos de entrada de color.');
            return;
        }

        const startColor = startColorInput.value;
        const endColor = endColorInput.value;

        tablas.forEach(function(tabla) {
            const computedStyle = window.getComputedStyle(tabla);
            let color = computedStyle.color;
            // Si el color no está definido, se asigna un valor por defecto
            if (!color || color === 'rgba(0, 0, 0, 0)' || color === 'transparent') {
                color = "rgb(255, 0, 0)";
            }

            const colorHsl = rgbToHsl(color);

            const celdas = tabla.querySelectorAll("tbody td");
            const valores = [];

            celdas.forEach(function(celda) {
                const valor = parseFloat(celda.textContent);
                if (!isNaN(valor)) {
                    valores.push(valor);
                }
            });

            if (valores.length === 0) {
                console.warn("No se encontraron valores numéricos en la tabla:", tabla);
                return;
            }

            const maximo = Math.max(...valores);
            const minimo = Math.min(...valores);
            let rango = maximo - minimo;
            if (rango === 0) rango = 1;

            celdas.forEach(function(celda) {
                const valor = parseFloat(celda.textContent);
                if (isNaN(valor)) return;

                const porcentaje = ((valor - minimo) / rango);

                // Se utiliza siempre la interpolación basada en los sliders
                const startHsl = `hsl(${startColor}, 100%, 50%)`;
                const endHsl = `hsl(${endColor}, 100%, 50%)`;
                const backgroundColorHsl = interpolateHsl(startHsl, endHsl, porcentaje);

                celda.style.backgroundColor = backgroundColorHsl;
                celda.style.color = "black";
            });

            const filas = tabla.querySelectorAll("tbody tr");
            filas.forEach(function(fila) {
                const celdasFila = fila.querySelectorAll("td");
                const maxValorFila = Math.max(...Array.from(celdasFila).map(celda => parseFloat(celda.textContent)));
                celdasFila.forEach(function(celda) {
                    if (parseFloat(celda.textContent) === maxValorFila) {
                        celda.style.border = "2px solid black";
                    }
                });
            });

            // Resaltar solo la celda con el valor máximo global
            const maxGlobal = Math.max(...valores);
            celdas.forEach(function(celda) {
                if (parseFloat(celda.textContent) === maxGlobal) {
                    celda.style.border = "3px solid red";
                }
            });

            tabla.style.background = "none";
            tabla.style.color = "inherit";
        });
    }

    // Función para manejar el clic en las celdas
    function handleCellClick(event) {
        const celda = event.target;
        if (celda.style.border === "3px solid red") {
            celda.style.border = "";
        } else {
            celda.style.border = "3px solid red";
        }
    }

    // Función para guardar los valores resaltados en un JSON
    function saveHighlightedValues() {
        const tablas = document.querySelectorAll(".jocarsa-tan");
        const highlightedValues = [];

        tablas.forEach(function(tabla) {
            const celdas = tabla.querySelectorAll("tbody td");
            celdas.forEach(function(celda) {
                if (celda.style.border === "3px solid red") {
                    highlightedValues.push(parseFloat(celda.textContent));
                }
            });
        });

        const jsonData = JSON.stringify(highlightedValues, null, 2);
        const blob = new Blob([jsonData], { type: 'application/json' });
        const url = URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = 'highlighted_values.json';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }

    // Asignar eventos a los controles
    const startColorInput = document.getElementById('startColor');
    const endColorInput = document.getElementById('endColor');
    const startColorValue = document.getElementById('startColorValue');
    const endColorValue = document.getElementById('endColorValue');

    if (startColorInput && endColorInput && startColorValue && endColorValue) {
        startColorInput.addEventListener('input', function() {
            startColorValue.textContent = this.value;
            updateTableColors();
        });

        endColorInput.addEventListener('input', function() {
            endColorValue.textContent = this.value;
            updateTableColors();
        });

        // Llamada inicial para actualizar los colores al cargar la página
        updateTableColors();
    } else {
        console.error('No se pudieron encontrar uno o más elementos necesarios en el DOM.');
    }

    // Asignar el evento de clic a todas las celdas de la tabla
    const tablas = document.querySelectorAll(".jocarsa-tan");
    tablas.forEach(function(tabla) {
        const celdas = tabla.querySelectorAll("tbody td");
        celdas.forEach(function(celda) {
            celda.addEventListener('click', handleCellClick);
        });
    });

    // Añadir botón para guardar los valores resaltados
    const saveButton = document.createElement('button');
    saveButton.textContent = "Guardar Valores Resaltados";
    saveButton.addEventListener('click', saveHighlightedValues);
    document.querySelector('.controls').appendChild(saveButton);

    // Función para aplicar el filtro de valor mínimo y máximo
    function applyFilter() {
        const minValueInput = document.getElementById('minValue');
        const maxValueInput = document.getElementById('maxValue');

        if (!minValueInput || !maxValueInput) {
            console.error('No se encontraron los elementos de entrada de filtro.');
            return;
        }

        const minValue = parseFloat(minValueInput.value);
        const maxValue = parseFloat(maxValueInput.value);

        const tablas = document.querySelectorAll(".jocarsa-tan");
        tablas.forEach(function(tabla) {
            const celdas = tabla.querySelectorAll("tbody td");
            celdas.forEach(function(celda) {
                const valor = parseFloat(celda.textContent);
                if (valor >= minValue && valor <= maxValue) {
                    celda.style.display = "";
                } else {
                    celda.style.display = "none";
                }
            });
        });
    }

    // Función para reiniciar el filtro
    function resetFilter() {
        const tablas = document.querySelectorAll(".jocarsa-tan");
        tablas.forEach(function(tabla) {
            const celdas = tabla.querySelectorAll("tbody td");
            celdas.forEach(function(celda) {
                celda.style.display = "";
            });
        });
    }

    // Añadir botón para aplicar el filtro
    const applyFilterButton = document.createElement('button');
    applyFilterButton.textContent = "Aplicar Filtro";
    applyFilterButton.addEventListener('click', applyFilter);
    document.querySelector('.controls').appendChild(applyFilterButton);

    // Añadir botón para reiniciar el filtro
    const resetFilterButton = document.createElement('button');
    resetFilterButton.textContent = "Reiniciar Filtro";
    resetFilterButton.addEventListener('click', resetFilter);
    document.querySelector('.controls').appendChild(resetFilterButton);

    // Añadir sliders para filtrar por valor mínimo y máximo
    const minValueLabel = document.createElement('label');
    minValueLabel.textContent = "Valor Mínimo: ";
    minValueLabel.htmlFor = "minValue";
    document.querySelector('.controls').appendChild(minValueLabel);

    const minValueInputElement = document.createElement('input');
    minValueInputElement.type = "range";
    minValueInputElement.id = "minValue";
    minValueInputElement.min = "0";
    minValueInputElement.max = "500";
    minValueInputElement.value = "0";
    document.querySelector('.controls').appendChild(minValueInputElement);

    const minValueValueElement = document.createElement('span');
    minValueValueElement.id = "minValueValue";
    minValueValueElement.textContent = "0";
    document.querySelector('.controls').appendChild(minValueValueElement);

    const maxValueLabel = document.createElement('label');
    maxValueLabel.textContent = "Valor Máximo: ";
    maxValueLabel.htmlFor = "maxValue";
    document.querySelector('.controls').appendChild(maxValueLabel);

    const maxValueInputElement = document.createElement('input');
    maxValueInputElement.type = "range";
    maxValueInputElement.id = "maxValue";
    maxValueInputElement.min = "0";
    maxValueInputElement.max = "500";
    maxValueInputElement.value = "500";
    document.querySelector('.controls').appendChild(maxValueInputElement);

    const maxValueValueElement = document.createElement('span');
    maxValueValueElement.id = "maxValueValue";
    maxValueValueElement.textContent = "500";
    document.querySelector('.controls').appendChild(maxValueValueElement);

    document.querySelector('.controls').appendChild(document.createElement('br'));
});
