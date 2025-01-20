window.onload = function(){
	fetch("http://localhost/dam2/AlbertBeltran2DAM/Sistemas%20de%20gesti%c3%b3n%20empresarial/proyecto/114-endpoint%20publico/endpointpublico/")
	.then(function(result){
		return result.json()
	})
	.then(function(datos){
	console.log(datos)
	let contenedor = document.querySelector("body")
	let plantilla = document.querySelector("#plantillacoche")
		datos.forEach(function(dato){
			let instancia = plantilla.content.cloneNode(true)
			instancia.querySelector("h3").textContent = dato.nombre
			instancia.querySelector(".descripcion").textContent = dato.descripcion
			instancia.querySelector(".precio").textContent = dato.precio
			contenedor.appendChild(instancia)
		})
	})
}	
