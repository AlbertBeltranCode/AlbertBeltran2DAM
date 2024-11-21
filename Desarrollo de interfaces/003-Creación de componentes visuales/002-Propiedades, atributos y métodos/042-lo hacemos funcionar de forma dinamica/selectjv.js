let texto = "Albert Beltran"; // Cadena de texto que contiene los caracteres que se utilizarán como opciones en el selector.

let contenedor = document.querySelector("#contenedor"); // Selecciona un elemento del DOM con el ID 'contenedor'.
let selector = document.createElement("select"); // Crea un elemento <select>.
contenedor.appendChild(selector); // Añade el elemento <select> al contenedor.
for (let i = 0; i < 10; i++) {
  // Itera 10 veces para crear opciones en el <select>.
  let opcion = document.createElement("option"); // Crea un elemento <option>.
  opcion.textContent = texto[i]; // Asigna el carácter correspondiente de la cadena 'texto' al contenido del <option>.
  opcion.value = i; // Asigna el índice actual como valor del <option>.
  selector.appendChild(opcion); // Añade el <option> al <select>.
}
selectjv(selector); // Llama a la función selectjv con el <select> creado.

function selectjv(selector) {
  contenedores = []; // Inicializa un array vacío para almacenar contenedores.
  contenedores.push(document.createElement("div")); // Crea un nuevo <div> y lo añade al array.
  contenedores[contenedores.length - 1].classList.add("selectjv"); // Añade la clase 'selectjv' al último contenedor del array.

  contenedores[contenedores.length - 1].onclick = function (e) {
    e.stopPropagation(); // Evita que el evento haga burbuja hacia otros elementos.
  };

  selector.replaceWith(contenedores[contenedores.length - 1]); // Sustituye el <select> original por el nuevo contenedor.
  let caja = document.createElement("div"); // Crea un nuevo <div> que servirá como caja visible.
  caja.classList.add("caja"); // Añade la clase 'caja' al nuevo <div>.
  caja.textContent = selector.querySelector("option:first-child").textContent; // Asigna el texto del primer <option> al contenido de la caja.
  contenedores[contenedores.length - 1].appendChild(caja); // Añade la caja al contenedor.
  contenedores[contenedores.length - 1].appendChild(selector); // Vuelve a añadir el <select> al contenedor.

  caja.onclick = function (e) {
    // Maneja el clic en la caja.
    e.stopPropagation(); // Evita la propagación del evento.
    caja.classList.add("radio2"); // Añade la clase 'radio2' a la caja.
    let resultados = document.createElement("div"); // Crea un <div> para mostrar los resultados.
    resultados.classList.add("resultados"); // Añade la clase 'resultados' al <div>.
    this.appendChild(resultados); // Añade el <div> de resultados al contenedor.

    let buscador = document.createElement("input"); // Crea un campo <input> para búsqueda.
    buscador.setAttribute("type", "search"); // Establece el tipo del <input> como 'search'.
    buscador.setAttribute("placeholder", "busca..."); // Añade un texto de marcador de posición al <input>.
    resultados.appendChild(buscador); // Añade el <input> al <div> de resultados.

    buscador.onclick = function (e) {
      console.log("ok hola"); // Imprime un mensaje al hacer clic en el buscador.
      e.stopPropagation(); // Evita que el evento haga burbuja.
    };
    buscador.onkeyup = function (e) {
      // Maneja las pulsaciones de teclas en el buscador.
      let busca = this.value; // Obtiene el texto ingresado en el buscador.
      contieneresultados.innerHTML = ""; // Limpia los resultados previos.
      opciones.forEach(function (opcion) {
        // Itera por cada <option>.
        if (opcion.textContent.toLowerCase().includes(busca.toLowerCase())) {
          // Comprueba si el texto del <option> coincide con la búsqueda.
          let texto = document.createElement("p"); // Crea un párrafo para mostrar la opción coincidente.
          texto.textContent = opcion.textContent; // Asigna el texto del <option> al párrafo.
          contieneresultados.appendChild(texto); // Añade el párrafo al contenedor de resultados.
          texto.onclick = function () {
            // Maneja el clic en una opción de los resultados.
            console.log("has hecho click en una opcion: ", texto.textContent); // Muestra el texto de la opción en la consola.
            resultados.remove(); // Elimina el <div> de resultados.
            caja.textContent = texto.textContent; // Actualiza el texto de la caja con la opción seleccionada.
            let opciones2 = selector.querySelectorAll("option"); // Obtiene todas las opciones del <select>.
            console.log(opciones2); // Imprime las opciones en la consola.
            opciones2.forEach(function (opcion2) {
              // Itera por las opciones.
              if (opcion2.textContent == texto.textContent) {
                // Selecciona la opción que coincide con el texto.
                opcion2.setAttribute("selected", true);
              } else {
                opcion2.removeAttribute("selected"); // Deselecciona las demás opciones.
              }
            });
          };
        }
      });
    };

    let contieneresultados = document.createElement("div"); // Crea un contenedor para las opciones filtradas.
    contieneresultados.onclick = function (e) {
      e.stopPropagation(); // Evita que el clic haga burbuja.
    };

    let opciones = selector.querySelectorAll("option"); // Obtiene todas las opciones del <select>.
    opciones.forEach(function (opcion) {
      // Itera por cada opción.
      let texto = document.createElement("p"); // Crea un párrafo para cada opción.
      texto.textContent = opcion.textContent; // Asigna el texto de la opción al párrafo.
      contieneresultados.appendChild(texto); // Añade el párrafo al contenedor de resultados.
      texto.onclick = function () {
        // Maneja el clic en una opción del contenedor.
        console.log("has hecho click en una opcion: ", texto.textContent); // Muestra el texto de la opción seleccionada en la consola.
        resultados.remove(); // Elimina el <div> de resultados.
        caja.textContent = texto.textContent; // Actualiza el texto de la caja.
        let opciones2 = selector.querySelectorAll("option"); // Obtiene todas las opciones del <select>.
        console.log(opciones2); // Imprime las opciones en la consola.
        opciones2.forEach(function (opcion2) {
          // Itera por las opciones.
          if (opcion2.textContent == texto.textContent) {
            // Selecciona la opción coincidente.
            opcion2.setAttribute("selected", true);
          } else {
            opcion2.removeAttribute("selected"); // Deselecciona las demás opciones.
          }
        });
      };
    });

    resultados.appendChild(contieneresultados); // Añade el contenedor de resultados al <div> de resultados.
    resultados.onclick = function (e) {
      e.stopPropagation(); // Evita que el clic haga burbuja.
    };
  };

  document.onclick = function () {
    // Maneja los clics fuera de los elementos interactivos.
    console.log("ok body"); // Imprime un mensaje en la consola.
    contenedores.forEach(function (contenedor) {
      // Itera por todos los contenedores.
      console.log(contenedor); // Imprime el contenedor en la consola.
      try {
        contenedor.querySelector(".resultados").remove(); // Intenta eliminar el <div> de resultados.
        contenedor.querySelector(".caja").classList.remove("radio2"); // Quita la clase 'radio2' de la caja.
      } catch (error) {
        console.log("error pero no pasa nada"); // Maneja cualquier error y continúa la ejecución.
      }
    });
  };
}
