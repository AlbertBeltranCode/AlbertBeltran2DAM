window.onload = function () {
	let videos = document.querySelectorAll("video");

	// Iteramos sobre todos los videos en la página
	videos.forEach(function (video) {
		let volumen = 1.0;

		let tagvideo = video;
		let contienevideo = document.createElement("div");
		contienevideo.classList.add("jvideo");

		// Reemplazamos el video original con el contenedor personalizado
		if (tagvideo.parentNode) {
			tagvideo.parentNode.replaceChild(contienevideo, tagvideo);
			contienevideo.appendChild(tagvideo);
		}

		// Creamos la barra de controles
		let barracontroles = document.createElement("div");
		barracontroles.classList.add("barracontroles");
		contienevideo.appendChild(barracontroles);

		// Creamos la barra de progreso
		let barraprogreso = document.createElement("div");
		barraprogreso.classList.add("barraprogreso");
		contienevideo.appendChild(barraprogreso);

		// Creamos el elemento de progreso
		let progreso = document.createElement("div");
		progreso.classList.add("progreso");
		barraprogreso.appendChild(progreso);

		// Evento para actualizar la barra de progreso y el tiempo cuando el video avanza
		tagvideo.addEventListener("timeupdate", () => {
			let actual = tagvideo.currentTime;
			let total = tagvideo.duration;
			let porcentaje = (actual / total) * 100;
			progreso.style.width = porcentaje + "%";
			actualizarTiempo();
		});

		// Indicador de tiempo actual y duración total del video
		let tiempoDisplay = document.createElement("div");
		tiempoDisplay.classList.add("tiempo");
		barracontroles.appendChild(tiempoDisplay);

		function actualizarTiempo() {
			let actual = tagvideo.currentTime;
			let total = tagvideo.duration;
			let formatTime = (time) => {
				let minutes = Math.floor(time / 60);
				let seconds = Math.floor(time % 60);
				return `${minutes}:${seconds.toString().padStart(2, "0")}`;
			};
			tiempoDisplay.textContent = `${formatTime(actual)} / ${formatTime(total)}`;
		}

		/*////////////////////// BOTÓN DE PLAY //////////////////////*/
		let botonplay = document.createElement("button");
		botonplay.innerHTML = "<img src='play.svg'>";
		barracontroles.appendChild(botonplay);
		let estado = "pause";
		botonplay.onclick = function () {
			playopausa();
		};

		/*////////////////////// BOTÓN DE VOLUMEN MÁS //////////////////////*/
		let botonvolumenmas = document.createElement("button");
		botonvolumenmas.innerHTML = "<img src='volumenmas.svg'>";
		barracontroles.appendChild(botonvolumenmas);

		botonvolumenmas.onclick = function () {
			if (tagvideo.volume < 1.0) {
				tagvideo.volume += 0.1;
			}
		};

		/*////////////////////// BOTÓN DE VOLUMEN MENOS //////////////////////*/
		let botonvolumenmenos = document.createElement("button");
		botonvolumenmenos.innerHTML = "<img src='volumenmenos.svg'>";
		barracontroles.appendChild(botonvolumenmenos);

		botonvolumenmenos.onclick = function () {
			if (tagvideo.volume > 0.0) {
				tagvideo.volume -= 0.1;
			}
		};

		/*////////////////////// CONTROL DE VOLUMEN //////////////////////*/
		let controlvolumen = document.createElement("input");
		controlvolumen.setAttribute("type", "range");
		contienevideo.appendChild(controlvolumen);
		controlvolumen.onchange = function () {
			tagvideo.volume = this.value / 100;
		};

		/*////////////////////// BOTÓN DE RETROCEDER //////////////////////*/
		let botonretroceder = document.createElement("button");
		botonretroceder.innerHTML = "<img src='retroceder.svg'>";
		barracontroles.appendChild(botonretroceder);

		botonretroceder.onclick = function () {
			tagvideo.currentTime -= 10;
		};

		/*////////////////////// BOTÓN DE AVANZAR //////////////////////*/
		let botonavanzar = document.createElement("button");
		botonavanzar.innerHTML = "<img src='avanzar.svg'>";
		barracontroles.appendChild(botonavanzar);

		botonavanzar.onclick = function () {
			tagvideo.currentTime += 10;
		};

		/*////////////////////// BOTÓN DE PANTALLA COMPLETA //////////////////////*/
		let botonPantallaCompleta = document.createElement("button");
		botonPantallaCompleta.innerHTML = "<img src='completa.png'>";
		barracontroles.appendChild(botonPantallaCompleta);

		botonPantallaCompleta.onclick = function () {
			if (!document.fullscreenElement) {
				contienevideo.requestFullscreen();
			} else {
				document.exitFullscreen();
			}
		};

		/*////////////////////// BOTÓN DE FILTRO CINEMATOGRÁFICO //////////////////////*/
		let botonFiltro = document.createElement("button");
		botonFiltro.innerHTML = "<img src='efecto.png'>";
		barracontroles.appendChild(botonFiltro);

		let filtroActivo = false;

		botonFiltro.onclick = function () {
			if (!filtroActivo) {
				tagvideo.style.filter = "contrast(1.2) saturate(0.8) brightness(0.9) sepia(0.3)";
				filtroActivo = true;
			} else {
				tagvideo.style.filter = "none";
				filtroActivo = false;
			}
		};

		/*////////////////////// BOTÓN DE VELOCIDAD DE REPRODUCCIÓN //////////////////////*/
		// Creamos el botón desplegable para cambiar la velocidad de reproducción
		let botonVelocidad = document.createElement("button");
		botonVelocidad.innerHTML = "<img src='velocidad.png'>";
		barracontroles.appendChild(botonVelocidad);

		// Creamos el menú desplegable con las opciones de velocidad
		let menuVelocidad = document.createElement("ul");
		menuVelocidad.classList.add("menu-velocidad");
		menuVelocidad.style.display = "none"; // Ocultamos el menú inicialmente
		let opciones = ["0.5x", "1x", "1.5x", "2x"];
		opciones.forEach(function (opcion) {
			let item = document.createElement("li");
			item.textContent = opcion;
			item.onclick = function () {
				// Asignamos la velocidad de reproducción al video según la opción seleccionada
				if (opcion === "0.5x") {
					tagvideo.playbackRate = 0.5;
				} else if (opcion === "1x") {
					tagvideo.playbackRate = 1.0;
				} else if (opcion === "1.5x") {
					tagvideo.playbackRate = 1.5;
				} else if (opcion === "2x") {
					tagvideo.playbackRate = 2.0;
				}
				// Cerramos el menú después de seleccionar una opción
				menuVelocidad.style.display = "none";
			};
			menuVelocidad.appendChild(item);
		});
		barracontroles.appendChild(menuVelocidad);

		// Hacemos que al hacer clic en el botón se muestre o se oculte el menú desplegable
		botonVelocidad.onclick = function () {
			if (menuVelocidad.style.display === "none") {
				menuVelocidad.style.display = "block";
			} else {
				menuVelocidad.style.display = "none";
			}
		};

		/*////////////////////// CLICK EN EL VIDEO //////////////////////*/
		tagvideo.onclick = function () {
			playopausa();
		};

		function playopausa() {
			if (estado == "pause") {
				botonplay.innerHTML = "<img src='pause.svg'>";
				estado = "play";
				tagvideo.play();
			} else {
				botonplay.innerHTML = "<img src='play.svg'>";
				estado = "pause";
				tagvideo.pause();
			}
		}

		/*////////////////////// FUNCIONALIDAD DE OCULTAR/MOSTRAR BARRA DE CONTROLES //////////////////////*/
		// Añadimos el evento para mostrar/ocultar los controles cuando el ratón entra o sale del área del video
		contienevideo.addEventListener("mouseenter", function () {
			barracontroles.style.opacity = 1; // Muestra los controles
		});

		contienevideo.addEventListener("mouseleave", function () {
			barracontroles.style.opacity = 0; // Oculta los controles
		});

		// Establecemos un estilo inicial para ocultar la barra de controles
		barracontroles.style.transition = "opacity 0.3s";
		barracontroles.style.opacity = 0; // Los controles se ocultan inicialmente
	});
};
