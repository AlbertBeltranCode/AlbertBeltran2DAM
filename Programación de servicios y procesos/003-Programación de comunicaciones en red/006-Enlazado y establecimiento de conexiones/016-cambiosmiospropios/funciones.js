// Función para comprimir una colección de píxeles
function comprimir(coleccion) {
	// Quitamos la transparencia y convertimos los colores RGB en un solo valor
	const sintransparencia = [];
	for (let i = 0; i < coleccion.length; i += 4) {
		const rojo = coleccion[i]; // Canal rojo
		const verde = coleccion[i + 1]; // Canal verde
		const azul = coleccion[i + 2]; // Canal azul
		// Convertimos los valores RGB en un solo número
		sintransparencia.push((rojo << 16) + (verde << 8) + azul);
	}

	// Aplicamos la compresión RLE (Run-Length Encoding) al array de colores sin transparencia
	const comprimido = rleCompressArray(sintransparencia);
	return comprimido;
}

// Función para descomprimir una colección comprimida
function descomprimir(coleccion) {
	// Descomprimimos la colección con RLE
	const desrle = rleDecompressArray(coleccion);
	// Creamos un nuevo array con la misma longitud, pero con 4 valores (RGBA)
	const descomprimido = new Uint8ClampedArray(desrle.length * 4);

	let j = 0;
	// Reconstruimos los valores de los colores y la transparencia (fija en 255)
	for (let i = 0; i < desrle.length; i++) {
		// Extraemos los canales de color y los colocamos en el nuevo array
		descomprimido[j++] = (desrle[i] >> 16) & 255; // Rojo
		descomprimido[j++] = (desrle[i] >> 8) & 255; // Verde
		descomprimido[j++] = desrle[i] & 255; // Azul
		descomprimido[j++] = 255; // Transparencia fija (opaca)
	}
	return descomprimido;
}

// Función para comprimir un array usando RLE (Run-Length Encoding)
function rleCompressArray(arr) {
	const compressed = [];
	let count = 1;
	// Recorremos el array y comprimimos las secuencias de elementos iguales
	for (let i = 1; i < arr.length; i++) {
		if (arr[i] === arr[i - 1]) {
			// Si el valor es igual al anterior, aumentamos el contador
			count++;
		} else {
			// Si el valor es diferente, guardamos el valor y la cantidad de repeticiones
			compressed.push([arr[i - 1], count]);
			count = 1;
		}
	}
	// Añadimos el último valor al array comprimido
	compressed.push([arr[arr.length - 1], count]);
	return compressed;
}

// Función para descomprimir un array usando RLE
function rleDecompressArray(compressed) {
	const decompressed = [];
	// Recorremos el array comprimido y reconstruimos el array original
	for (let i = 0; i < compressed.length; i++) {
		const [value, count] = compressed[i]; // Extraemos el valor y la cantidad de repeticiones
		for (let j = 0; j < count; j++) {
			// Añadimos el valor repetido al array descomprimido
			decompressed.push(value);
		}
	}
	return decompressed;
}

// Función para verificar la consistencia entre los datos originales y los descomprimidos
function verificarConsistencia(coleccionOriginal, coleccionDescomprimida) {
	// Verifica si la longitud de los arrays es la misma
	if (coleccionOriginal.length !== coleccionDescomprimida.length) {
		console.log("Los arrays no tienen la misma longitud");
		return false;
	}

	// Compara cada valor de los dos arrays
	for (let i = 0; i < coleccionOriginal.length; i++) {
		if (coleccionOriginal[i] !== coleccionDescomprimida[i]) {
			console.log(`Diferencia encontrada en el índice ${i}`);
			return false;
		}
	}

	// Si todo es igual
	return true;
}

// Ejemplo de uso dentro del flujo principal del código
function procesarImagen() {
	const lienzo = document.querySelector("canvas");
	const contexto = lienzo.getContext("2d");
	lienzo.width = 1920;
	lienzo.height = 1080;

	let imagen = new Image();
	imagen.src = "../captura.png"; // Ruta de la imagen original

	imagen.onload = function() {
		console.log("Imagen cargada correctamente");

		contexto.drawImage(imagen, 0, 0); // Dibuja la imagen original
		const coleccion = contexto.getImageData(0, 0, 1920, 1080).data; // Obtiene los datos de los píxeles

		// Mostramos los datos de la imagen antes de comprimir
		console.log("Datos de la imagen original (antes de comprimir):");
		console.log(coleccion);

		// Guardamos los datos originales para la verificación
		const coleccionOriginal = Array.from(coleccion);

		// Comprimimos los datos de la imagen
		let comprimido = comprimir(coleccion);
		console.log("Datos comprimidos:", comprimido);

		// Descomprimimos los datos de vuelta
		let descomprimido = descomprimir(comprimido);
		console.log("Datos descomprimidos:", descomprimido);

		// Verificación de consistencia
		const esConsistente = verificarConsistencia(coleccionOriginal, descomprimido);
		console.log("Verificación de consistencia:", esConsistente ? "Consistente" : "Inconsistente");

		// Colocamos los datos descomprimidos en el lienzo
		let datos = contexto.getImageData(0, 0, 1920, 1080);
		for (let i = 0; i < datos.data.length; i++) {
			datos.data[i] = descomprimido[i];
		}
		contexto.putImageData(datos, 0, 0);

		console.log("Imagen procesada y colocada en el lienzo.");
	};

	imagen.onerror = function() {
		// Si la imagen no se carga correctamente
		console.error("Error al cargar la imagen.");
	};
}

