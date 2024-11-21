let tamanio = 1; // Tamaño inicial del texto, en unidades relativas (em).
let cantidadcontraste = 1; // Valor inicial del contraste de la página.
let contenedor = document.createElement("div"); // Crea un contenedor para los botones.
contenedor.classList.add("jvampliador"); // Añade la clase 'jvampliador' al contenedor.

////////////////// AUMENTAR /////////////////

let aumentar = document.createElement("button"); // Crea un botón para aumentar el tamaño del texto.
aumentar.textContent = "+"; // Asigna el texto "+" al botón.

contenedor.appendChild(aumentar); // Añade el botón de aumentar al contenedor.
aumentar.onclick = function () {
	// Define el evento de clic para el botón de aumentar.
	tamanio *= 1.1; // Incrementa el tamaño del texto en un 10%.
	document.querySelector("body").style.fontSize = tamanio + "em"; // Aplica el nuevo tamaño al texto del <body>.
};

////////////////// CONTRASTE /////////////////

let contraste = document.createElement("button"); // Crea un botón para ajustar el contraste.
contraste.textContent = "C"; // Asigna el texto "C" al botón.

contenedor.appendChild(contraste); // Añade el botón de contraste al contenedor.
contraste.onclick = function () {
	// Define el evento de clic para el botón de contraste.
	cantidadcontraste = 30; // Fija el nivel de contraste a 30.
	document.querySelector("body").style.filter = "contrast(" + cantidadcontraste + ")"; // Aplica el filtro de contraste al <body>.
};

////////////////// INVERTIR /////////////////

let invertir = document.createElement("button"); // Crea un botón para invertir los colores.
invertir.textContent = "I"; // Asigna el texto "I" al botón.

contenedor.appendChild(invertir); // Añade el botón de invertir al contenedor.
invertir.onclick = function () {
	// Define el evento de clic para el botón de invertir.
	document.querySelector("body").style.filter = "invert(1)"; // Aplica el filtro de inversión al <body>.
};

////////////////// DISMINUIR /////////////////

let disminuir = document.createElement("button"); // Crea un botón para disminuir el tamaño del texto.
disminuir.textContent = "-"; // Asigna el texto "-" al botón.
contenedor.appendChild(disminuir); // Añade el botón de disminuir al contenedor.

disminuir.onclick = function () {
	// Define el evento de clic para el botón de disminuir.
	tamanio *= 0.9; // Reduce el tamaño del texto en un 10%.
	document.querySelector("body").style.fontSize = tamanio + "em"; // Aplica el nuevo tamaño al texto del <body>.
};

document.querySelector("body").appendChild(contenedor); // Añade el contenedor con los botones al <body>.
