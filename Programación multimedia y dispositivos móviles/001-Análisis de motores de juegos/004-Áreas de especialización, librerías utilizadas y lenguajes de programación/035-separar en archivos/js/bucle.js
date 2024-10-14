var temporizador;
let puntuacion = 0; // Inicializa la puntuación en 0
let mensajeHistoria = "¡Defiende la tierra!"; // Mensaje de historia
let indiceMensaje = 0; // Índice del carácter actual del mensaje

function iniciarHistoria() {
  // Reinicia el índice del mensaje y empieza el bucle de la historia
  indiceMensaje = 0;
  temporizador = setTimeout(mostrarMensajeHistoria, 1000); // Comienza a mostrar el mensaje
}

function mostrarMensajeHistoria() {
  contexto.clearRect(0, 0, 512, 512); // Limpio el lienzo

  contexto.fillStyle = "rgba(0, 0, 0, 0.8)"; // Fondo semi-transparente
  contexto.fillRect(0, 0, 512, 512); // Dibuja un rectángulo que cubre la pantalla

  contexto.fillStyle = "white"; // Color del texto
  contexto.font = "30px Arial"; // Fuente y tamaño del texto
  contexto.textAlign = "center"; // Centra el texto

  // Dibuja el mensaje actual
  contexto.fillText(mensajeHistoria.substring(0, indiceMensaje), 256, 256); 

  // Incrementa el índice para mostrar el siguiente carácter
  indiceMensaje++;
  
  // Si no se ha llegado al final del mensaje, continua
  if (indiceMensaje <= mensajeHistoria.length+10) {
    temporizador = setTimeout(mostrarMensajeHistoria, 100); // Muestra el siguiente carácter después de 100ms
  } else {
    // Una vez que termine la historia, inicia el bucle del juego
    clearTimeout(temporizador);
    bucle(); // Comienza el bucle del juego
  }
}

function bucle() {
  // Código para el movimiento y desplazamiento...
  
  contexto.clearRect(0, 0, 512, 512); // Limpio el lienzo 1
  contexto2.clearRect(0, 0, 512, 512); // Limpio el lienzo 2
  contextoplataformas.clearRect(0, 0, 512, 512); // Limpio el contexto de las plataformas

  // Dibuja las plataformas
  contextoplataformas.drawImage(imagennivel, 0 - desfase_global_x, 0, 2048, 512);

  for (let i = 0; i < misnpcs.length; i++) {
    misnpcs[i].mueve();
    misnpcs[i].rebota();
    misnpcs[i].dibuja(desfase_global_x);
  }

  for (let i = 0; i < balas.length; i++) {
    balas[i].mueve();
    balas[i].dibuja();
  }

  // Para comprobar si ALGUNA de las balas colisiona con ALGUNO de los npc
  for (let i = balas.length - 1; i >= 0; i--) { // Recorre balas en reversa
    for (let j = 0; j < misnpcs.length; j++) {
      if (calculateDistance(balas[i].x, balas[i].y, misnpcs[j].x, misnpcs[j].y) < 20) {
        misnpcs.splice(j, 1); // Elimino un npc del array de npcs

        // Incrementa la puntuación
        puntuacion += 100; // Suma 100 puntos

        // Generar dos nuevos NPCs en posiciones aleatorias
        misnpcs.push(new Npc()); // Crea un nuevo NPC con posición aleatoria
        misnpcs.push(new Npc()); // Crea otro nuevo NPC con posición aleatoria
        
        balas.splice(i, 1); // Elimino la bala del array de balas
        break; // Salimos del bucle interno para evitar problemas de índice
      }
    }
  }

  // Dibuja la puntuación en la parte inferior izquierda
  contexto.fillStyle = "white"; // Color del texto
  contexto.font = "20px Arial"; // Fuente y tamaño del texto
  contexto.fillText("Puntuación: " + puntuacion, 80, 500); // Dibuja el texto

  // Verifica si se ha alcanzado la puntuación de 5000
  if (puntuacion >= 5000) {
    contexto.fillStyle = "rgba(0, 0, 0, 0.8)"; // Color de fondo con transparencia
    contexto.fillRect(0, 0, 512, 512); // Dibuja un rectángulo que cubre la pantalla

    contexto.fillStyle = "white"; // Color del texto del mensaje
    contexto.font = "30px Arial"; // Fuente y tamaño del texto
    contexto.textAlign = "center"; // Centra el texto
    contexto.fillText("¡Has Ganado!", 256, 256); // Dibuja el mensaje en el centro
    return; // Detiene el bucle para evitar que se siga jugando
  }

  jugador.mueve();
  jugador.dibuja(); // Dibujamos al jugador 1

  // Dibuja el mensaje de recarga si está recargando
  if (recargando) {
    contexto.fillStyle = "yellow"; // Color del texto
    contexto.font = "20px Arial"; // Fuente y tamaño del texto
    contexto.textAlign = "center"; // Centra el texto
    contexto.fillText("Recargando...", jugador.x, jugador.y + 20); // Dibuja el mensaje debajo del jugador
  }

  var datos = contexto.getImageData(jugador.x, jugador.y, 1, 1).data; // Obtengo un array con los componentes de color de un pixel
  var alpha = datos[3]; // El índice 3 es la transparencia
  if (alpha == 255) {
    window.location = window.location; // Esto es recargar la página, lo que viene a querer decir que has perdido
  }

  clearTimeout(temporizador);
  temporizador = setTimeout(bucle, 30);
}

// Inicia la historia al cargar el juego
iniciarHistoria();
