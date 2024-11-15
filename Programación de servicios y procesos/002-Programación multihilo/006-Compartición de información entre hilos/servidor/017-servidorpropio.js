const WebSocket = require("ws");
const http = require("http");
const cors = require("cors");
const url = require("url");

// Crear un servidor HTTP
const server = http.createServer((req, res) => {
  // Configurar CORS
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("Access-Control-Allow-Credentials", "true");

  if (req.method === "OPTIONS") {
    return res.status(204).end(); // Si es una petición OPTIONS, respondemos rápidamente
  }

  // Aquí podrías manejar las rutas de la API, si las tienes
  if (req.url.startsWith("/toma")) {
    const { mensaje, usuario } = url.parse(req.url, true).query;
    console.log("Mensaje recibido:", mensaje, "de:", usuario);
    // Responder al cliente
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ mensaje: "Mensaje recibido" }));
  }
});

const wss = new WebSocket.Server({ server });

let clientes = [];

wss.on("connection", (socket) => {
  console.log("Nuevo cliente conectado");
  clientes.push(socket);

  socket.on("message", (mensaje) => {
    console.log("Mensaje recibido:", mensaje);

    let mensajeJSON = JSON.parse(mensaje);
    if (mensajeJSON.usuario && mensajeJSON.mensaje) {
      let mensajeObjeto = {
        usuario: mensajeJSON.usuario,
        mensaje: mensajeJSON.mensaje
      };

      let mensajeString = JSON.stringify(mensajeObjeto);

      // Enviar el mensaje a todos los clientes conectados
      clientes.forEach((cliente) => {
        if (cliente !== socket) {
          cliente.send(mensajeString);
        }
      });
    }
  });

  socket.on("close", () => {
    console.log("Cliente desconectado");
    clientes = clientes.filter((cliente) => cliente !== socket);
  });
});

server.listen(5000, () => {
  console.log("Servidor corriendo en http://localhost:5000");
});

//Para ejecutar este servidor, iniciar una terminal de windows en la carpeta de los ficheros.
//ejecutamos npm init -y  # Para crear un package.json
//ahora ejecutamos
//npm install ws  # Para instalar la librería WebSocket
//Ahora ejecutar el siguiente codigo
//npm install cors #Para permitir que los recursos de una web pueden ser solicitados desde otro dominio en este caso, entre http://localhost y http://localhost:5000.
//Acto seguido ejecutar el comando para iniciar el servidor:
// node 017-servidorpropio.js
