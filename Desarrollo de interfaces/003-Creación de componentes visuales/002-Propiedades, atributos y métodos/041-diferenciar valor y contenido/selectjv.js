window.onload = function() {
    let contenedores = [] // Array para almacenar los contenedores creados
    let selectores = document.querySelectorAll(".selectjv"); // Selecciona todos los elementos con la clase "selectjv"

    selectores.forEach(function(selector) { // Itera sobre cada selector encontrado
        contenedores.push(document.createElement("div")) // Crea un nuevo div y lo agrega al array de contenedores
        contenedores[contenedores.length - 1].classList.add("selectjv") // Agrega la clase "selectjv" al último contenedor creado

        contenedores[contenedores.length - 1].onclick = function(e) { 
            e.stopPropagation() // Evita que el evento se propague al hacer clic en el contenedor
        }

        selector.replaceWith(contenedores[contenedores.length - 1]) // Reemplaza el selector original con el nuevo contenedor
        let caja = document.createElement("div") // Crea un div para la "caja"
        caja.classList.add("caja") // Agrega la clase "caja"
        caja.textContent = selector.querySelector("option:first-child").textContent // Establece el texto del primer <option> en la caja
        contenedores[contenedores.length - 1].appendChild(caja) // Añade la caja al contenedor
        contenedores[contenedores.length - 1].appendChild(selector) // Añade el selector original dentro del contenedor

        caja.onclick = function(e) { // Evento cuando se hace clic en la caja
            e.stopPropagation(); // Evita la propagación del evento
            caja.classList.add("radio2") // Agrega la clase "radio2" a la caja
            let resultados = document.createElement("div") // Crea un div para mostrar los resultados
            resultados.classList.add("resultados") // Agrega la clase "resultados" al div
            this.appendChild(resultados) // Añade el div de resultados a la caja
            
            let buscador = document.createElement("input") // Crea un campo de entrada para buscar
            buscador.setAttribute("type", "search") // Define el tipo de entrada como "search"
            buscador.setAttribute("placeholder", "busca...") // Agrega un placeholder al campo
            resultados.appendChild(buscador) // Añade el campo de búsqueda a los resultados

            buscador.onclick = function(e) {
                console.log("ok hola") // Muestra un mensaje en la consola al hacer clic en el buscador
                e.stopPropagation(); // Evita la propagación del evento
            }

            buscador.onkeyup = function(e) { // Evento al escribir en el buscador
                let busca = this.value // Almacena el valor del campo de búsqueda
                contieneresultados.innerHTML = "" // Limpia el contenido de los resultados
                opciones.forEach(function(opcion) { // Itera sobre cada opción del selector
                    if (opcion.textContent.toLowerCase().includes(busca.toLowerCase())) { // Si la opción contiene el texto buscado
                        let texto = document.createElement("p") // Crea un elemento <p>
                        texto.textContent = opcion.textContent // Establece el texto de la opción en el <p>
                        contieneresultados.appendChild(texto) // Añade el <p> al contenedor de resultados
                        texto.onclick = function() { // Evento al hacer clic en una opción
                            console.log("has hecho click en una opcion: ", texto.textContent) // Muestra un mensaje en la consola
                            resultados.remove() // Elimina el div de resultados
                            caja.textContent = texto.textContent // Actualiza el texto de la caja con la opción seleccionada
                            let opciones2 = selector.querySelectorAll("option") // Selecciona todas las opciones
                            console.log(opciones2) // Muestra las opciones en la consola

                            opciones2.forEach(function(opcion2) { // Itera sobre las opciones para actualizar el atributo "selected"
                                if (opcion2.textContent == texto.textContent) {
                                    opcion2.setAttribute("selected", true) // Marca la opción seleccionada
                                } else {
                                    opcion2.removeAttribute("selected") // Elimina el atributo "selected" de las demás opciones
                                }
                            })
                        }
                    }
                })
            }

            let contieneresultados = document.createElement("div") // Crea un contenedor para los resultados
            contieneresultados.onclick = function(e) {
                e.stopPropagation(); // Evita la propagación del evento
            }

            let opciones = selector.querySelectorAll("option") // Selecciona todas las opciones del selector
            opciones.forEach(function(opcion) { // Itera sobre cada opción
                let texto = document.createElement("p") // Crea un elemento <p>
                texto.textContent = opcion.textContent // Establece el texto de la opción en el <p>
                contieneresultados.appendChild(texto) // Añade el <p> al contenedor de resultados
                texto.onclick = function() { // Evento al hacer clic en una opción
                    console.log("has hecho click en una opcion: ", texto.textContent) // Muestra un mensaje en la consola
                    resultados.remove() // Elimina el div de resultados
                    caja.textContent = texto.textContent // Actualiza el texto de la caja
                    let opciones2 = selector.querySelectorAll("option") // Selecciona todas las opciones
                    console.log(opciones2) // Muestra las opciones en la consola

                    opciones2.forEach(function(opcion2) { // Itera sobre las opciones para actualizar el atributo "selected"
                        if (opcion2.textContent == texto.textContent) {
                            opcion2.setAttribute("selected", true) // Marca la opción seleccionada
                        } else {
                            opcion2.removeAttribute("selected") // Elimina el atributo "selected" de las demás opciones
                        }
                    })
                }
            })

            resultados.appendChild(contieneresultados) // Añade el contenedor intermedio a los resultados
            resultados.onclick = function(e) {
                e.stopPropagation(); // Evita la propagación del evento
            }
        }
    })

    document.onclick = function() { // Evento al hacer clic en cualquier parte del documento
        console.log("ok body") // Muestra un mensaje en la consola
        contenedores.forEach(function(contenedor) { // Itera sobre todos los contenedores
            console.log(contenedor) // Muestra el contenedor en la consola
            try {
                contenedor.querySelector(".resultados").remove() // Elimina el div de resultados si existe
                contenedor.querySelector(".caja").classList.remove("radio2") // Elimina la clase "radio2" de la caja
            } catch (error) {
                console.log("error pero no pasa nada") // Maneja cualquier error sin interrumpir el flujo
            }
        })
    }
}