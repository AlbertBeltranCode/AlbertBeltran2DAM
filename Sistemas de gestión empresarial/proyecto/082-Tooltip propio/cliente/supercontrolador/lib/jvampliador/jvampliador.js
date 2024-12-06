let tamanio = 1;
let cantidadcontraste = 1;
let contenedor = document.createElement("div");
contenedor.classList.add("jvampliador");
let invertido = false;

// AUMENTAR
let aumentar = document.createElement("button");
aumentar.textContent = "+";
aumentar.setAttribute("aria-label", "Ampliar");
aumentar.setAttribute("title", "Ampliar el tamaño de la letra");
contenedor.appendChild(aumentar);
aumentar.onclick = function () {
    tamanio *= 1.1;
    document.querySelector("body").style.fontSize = tamanio + "em";
};

// CONTRASTE
let contraste = document.createElement("button");
contraste.textContent = "C";
contraste.setAttribute("aria-label", "Contraste");
contraste.setAttribute("title", "Cambiar el contraste de los colores de la aplicacion");
contenedor.appendChild(contraste);

// Variable para controlar el estado del contraste
let contrasteActivo = false;

contraste.onclick = function () {
    if (!contrasteActivo) {
        cantidadcontraste = 30;
        document.querySelector("body").style.filter = "contrast(" + cantidadcontraste + ")";
        contrasteActivo = true; // Marcar el contraste como activado
    } else {
        document.querySelector("body").style.filter = "contrast(1)";
        contrasteActivo = false; // Marcar el contraste como desactivado
    }
};

// INVERTIR
let invertir = document.createElement("button");
invertir.textContent = "I";
invertir.setAttribute("aria-label", "Invertir");
invertir.setAttribute("title", "Activar el modo nocturno");
contenedor.appendChild(invertir);
invertir.onclick = function () {
    if (invertido == false) {
        document.querySelector("body").style.filter = "invert(1) hue-rotate(180deg)";
        invertido = true;
    } else {
        document.querySelector("body").style.filter = "invert(0) hue-rotate(0deg)";
        invertido = false;
    }
};

// FUENTES
let fuentes = ['"bailsun"', '"notosans"', '"arial"', '"verdana"']; // Lista de fuentes
let fuente = document.createElement("button");
fuente.textContent = "F";
fuente.setAttribute("aria-label", "Cambiar la fuente");
fuente.setAttribute("title", "Cambiar la fuente de nuestra aplicacion");
contenedor.appendChild(fuente);

// Crear la lista de fuentes (ul) y agregarle la clase
let listaFuentes = document.createElement("ul");
listaFuentes.classList.add("fuentes-list"); // Clase específica para la lista

// Añadir las opciones (fuentes) al desplegable (como li) y agregarles una clase
fuentes.forEach(function(fuente) {
    let item = document.createElement("li");
    item.classList.add("fuente-item"); // Clase específica para cada item
    item.textContent = fuente;

    // Cambiar la fuente al hacer clic en la opción
    item.onclick = function() {
        document.querySelector("body").style.fontFamily = fuente;
        listaFuentes.style.display = "none"; // Ocultar la lista después de seleccionar
    };

    listaFuentes.appendChild(item);
});

// Mostrar/ocultar la lista de fuentes al hacer clic en el botón
fuente.onclick = function () {
    // Si la lista está oculta, mostrarla justo debajo del botón
    if (listaFuentes.style.display === "none" || listaFuentes.style.display === "") {
        let rect = fuente.getBoundingClientRect(); // Obtener la posición del botón
        listaFuentes.style.top = rect.bottom + "px"; // Posicionar la lista debajo del botón
        listaFuentes.style.left = rect.left + "px"; // Alinear la lista con el borde izquierdo del botón
        listaFuentes.style.display = "block"; // Mostrar la lista
    } else {
        listaFuentes.style.display = "none"; // Ocultar la lista si ya está visible
    }
};

// Añadir la lista de fuentes al contenedor
document.querySelector("body").appendChild(listaFuentes);


// DISMINUIR
let disminuir = document.createElement("button");
disminuir.textContent = "-";
disminuir.setAttribute("aria-label", "Disminuir el tamaño de la fuente");
disminuir.setAttribute("title", "Reducir el tamaño de la fuente");
contenedor.appendChild(disminuir);
disminuir.onclick = function () {
    tamanio *= 0.9;
    document.querySelector("body").style.fontSize = tamanio + "em";
};

// COMANDOS DE VOZ
// Crear mensajes flotantes
let mensaje1 = document.createElement("div");
mensaje1.classList.add("mensaje", "mensaje1"); // Agregar las clases "mensaje" y "mensaje1"
document.body.appendChild(mensaje1);

let mensaje2 = document.createElement("div");
mensaje2.classList.add("mensaje", "mensaje2"); // Agregar las clases "mensaje" y "mensaje2"
document.body.appendChild(mensaje2);

let mensaje3 = document.createElement("div");
mensaje3.classList.add("mensaje", "mensaje3"); // Agregar las clases "mensaje" y "mensaje3"
document.body.appendChild(mensaje3);

let mensaje4 = document.createElement("div");
mensaje4.classList.add("mensaje", "mensaje4"); // Agregar las clases "mensaje" y "mensaje4"
document.body.appendChild(mensaje4);

// Botón de voz
let voz = document.createElement("button");
voz.textContent = "🎤";
voz.setAttribute("aria-label", "Comandos de voz");
voz.setAttribute("title", "Activar comandos de voz");
contenedor.appendChild(voz);

voz.onclick = function () {
    if (!window.SpeechRecognition && !window.webkitSpeechRecognition) {
        alert("Tu navegador no soporta reconocimiento de voz. Por favor, utiliza Google Chrome.");
        return;
    }

    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "es-ES";
    
    // Mostrar el mensaje inicial
    mensaje1.style.display = "block";
    mensaje1.textContent = "Escuchando: diga 'ampliar' o 'reducir'"; // Instrucción inicial
    recognition.start();

    let timeoutID; // Variable para almacenar el ID del temporizador

    function reiniciarTemporizador() {
        // Si existe un temporizador anterior, lo borramos
        if (timeoutID) {
            clearTimeout(timeoutID);
        }
        // Establecemos un nuevo temporizador de 5 segundos
        timeoutID = setTimeout(function () {
            mensaje1.style.display = "none"; // Ocultar el mensaje después de 5 segundos
        }, 5000);
    }

    recognition.onresult = function (event) {
        let comando = event.results[0][0].transcript.toLowerCase();
        console.log("Comando recibido:", comando);

        // Acción si el comando es válido
        if (comando.includes("ampliar")) {
            tamanio *= 1.1;
            document.querySelector("body").style.fontSize = tamanio + "em";
            
            // Actualizar el mensaje para el comando "ampliar"
            mensaje2.style.display = "block";
            mensaje2.textContent = "Perfecto, vamos a ampliar la fuente";
			setTimeout(function () {
                mensaje2.style.display = "none"; // Ocultar el mensaje de error después de 5 segundos
            }, 5000); // Tiempo de 5 segundos
            
            
        } else if (comando.includes("reducir")) {
            tamanio *= 0.9;
            document.querySelector("body").style.fontSize = tamanio + "em";
            
            // Actualizar el mensaje para el comando "reducir"
            mensaje3.style.display = "block";
            mensaje3.textContent = "Perfecto, vamos a reducir la fuente";
			setTimeout(function () {
                mensaje3.style.display = "none"; // Ocultar el mensaje de error después de 5 segundos
            }, 5000); // Tiempo de 5 segundos
            
            
        } else {
            // Si el comando no es reconocido, mostrar mensaje de error
            mensaje4.style.display = "block";
            mensaje4.textContent = "Error 410: No he reconocido el mensaje";
            
            // Ocultar el mensaje de error después de 5 segundos
            setTimeout(function () {
                mensaje4.style.display = "none"; // Ocultar el mensaje de error después de 5 segundos
            }, 5000); // Tiempo de 5 segundos
        }
    };

    recognition.onerror = function (event) {
        console.error("Error de reconocimiento de voz:", event.error);
        // Ocultar el mensaje si hay un error
        mensaje1.style.display = "none";
    };

    recognition.onend = function () {
        // Ocultar el mensaje si el reconocimiento finaliza
        mensaje1.style.display = "none";
    };
};

document.querySelector("body").appendChild(contenedor);






