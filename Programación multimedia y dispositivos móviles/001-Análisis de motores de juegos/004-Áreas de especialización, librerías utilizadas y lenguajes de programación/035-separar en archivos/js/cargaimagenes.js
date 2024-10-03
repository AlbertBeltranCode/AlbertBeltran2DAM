/*//////////////////////////////IMAGENES////////////////////////////////*/
      
      var imagenbueno = new Image();                                          // Creo una nueva imagen como objeto de Javascript
      imagenbueno.src = "./img/spritesoldado.png"                                     // Le pongo el origen de la imagen
      var imagenmalo = new Image()
      imagenmalo.src = "./img/malvado.png"
      
      
      var imagenfondo = new Image();
      imagenfondo.src = "./img/fondo.png"
      imagenfondo.onload = function(){                                  // Cuando la imagen de las plataformas ha cargado desde el disco duro
        contextofondo.drawImage(imagenfondo,0,0)                  // La pinto sobre el lienzo del fondo
      }
      
      var imagennivel = new Image();
      imagennivel.src = "./img/suelo.png"
      imagennivel.onload = function(){
        contextoplataformas.imageSmoothingEnabled = false;
        console.log("imagen cargada")
        contextoplataformas.drawImage(imagennivel,0,0,2048,512) 
      }
      
      /*//////////////////////////////IMAGENES////////////////////////////////*/
