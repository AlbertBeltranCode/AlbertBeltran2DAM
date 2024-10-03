// Controles para mover al jugador con las teclas del teclado ////////////////////////////////

let puedeDisparar = true; // Controla si se puede disparar
let cooldownTiempo = 1000; // Tiempo de cooldown en milisegundos
let recargando = false; // Controla si está en recarga

document.onkeydown = function(e) {
  console.log(e);
  
  if (e.key == "ArrowUp" && jugador.cayendo == false) {
    jugador.y -= 5;
    jugador.vy = salto;
  }
  
  if (e.key == "ArrowDown") {
    jugador.y += 5;
  }
  
  if (e.key == "ArrowLeft") {
    jugador.x -= 5;
    jugador.direccion = "izquierda"; // Esto es lo que ocurre cuando el jugador pulsa la flecha izquierda
  }
  
  if (e.key == "ArrowRight") {
    jugador.x += 5;
    jugador.direccion = "derecha"; // Esto es lo que ocurre cuando el jugador pulsa la flecha derecha
  }

  if (e.keyCode == 32) { // Si se presiona la barra espaciadora
    if (puedeDisparar) { // Verifica si se puede disparar
      console.log("ok disparo");
      balas.push(new Bala()); // Dispara una nueva bala
      puedeDisparar = false; // Desactiva el disparo
      recargando = true; // Activa el estado de recarga

      // Reinicia el cooldown después de 1.5 segundos
      setTimeout(() => {
        puedeDisparar = true; // Permite disparar de nuevo
        recargando = false; // Desactiva el estado de recarga
      }, cooldownTiempo);
    }
  }
}
