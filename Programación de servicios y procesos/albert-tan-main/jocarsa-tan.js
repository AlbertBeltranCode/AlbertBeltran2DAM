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

    // Función auxiliar para modificar la luminosidad de un color HSL
    function modifyHslLightness(hslString, newLightness) {
        if (newLightness < 0 || newLightness > 100) {
            throw new Error("El valor de luminosidad debe estar entre 0 y 100.");
        }

        const match = hslString.match(/^hsl\((\d{1,3}),\s*(\d{1,3})%,\s*(\d{1,3})%\)$/);
        if (!match) {
            throw new Error("Formato HSL inválido. Use el formato 'hsl(x, y%, z%)'.");
        }

        const h = parseInt(match[1], 10);
        const s = parseInt(match[2], 10);

        return `hsl(${h}, ${s}%, ${newLightness}%)`;
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
            // Se obtiene el color de fondo, pero ahora lo ignoramos para usar siempre los sliders
            // let bgColor = computedStyle.backgroundColor;

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

            tabla.style.background = "none";
            tabla.style.color = "inherit";
        });
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
});
