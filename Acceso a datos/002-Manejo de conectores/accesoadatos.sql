-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-10-2024 a las 20:20:00
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `accesoadatos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `Identificador` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`Identificador`, `nombre`, `apellidos`) VALUES
(1, 'Nombre de prueba', 'Apellidos de prueba'),
(2, 'Ana', 'González'),
(3, 'Luis', 'Martínez'),
(5, 'Carlos', 'Hernández'),
(6, 'María', 'López'),
(7, 'Pedro', 'Sánchez'),
(8, 'Isabel', 'Jiménez'),
(9, 'Fernando', 'Cruz'),
(10, 'Laura', 'Ramírez'),
(11, 'Javier', 'Torres'),
(12, 'Clara', 'Moreno'),
(13, 'Diego', 'Vázquez'),
(14, 'Patricia', 'Salas'),
(15, 'Samuel', 'Núñez'),
(16, 'Gabriela', 'Rivas'),
(17, 'Andrés', 'Cordero'),
(18, 'Victoria', 'Méndez'),
(19, 'Miguel', 'Ponce'),
(20, 'Lucía', 'Salazar'),
(21, 'Alberto', 'Cabrera'),
(22, 'Nombre de prueba', 'Apellidos de prueba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `Identificador` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `cp` int(255) DEFAULT NULL,
  `localidad` varchar(255) DEFAULT NULL,
  `pais` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`Identificador`, `nombre`, `apellidos`, `email`, `direccion`, `cp`, `localidad`, `pais`) VALUES
(1, 'Juan', 'Pérez', 'juan.perez@example.com', 'Calle Falsa 123', 28001, 'Madrid', 'España'),
(2, 'Ana', 'García', 'ana.garcia@example.com', 'Avenida Siempre Viva 456', 8001, 'Barcelona', 'España'),
(3, 'Luis', 'Martínez', 'luis.martinez@example.com', 'Calle de la Paz 789', 41001, 'Sevilla', 'España'),
(4, 'María', 'López', 'maria.lopez@example.com', 'Calle Sol 321', 29001, 'Málaga', 'España'),
(5, 'Pedro', 'Sánchez', 'pedro.sanchez@example.com', 'Calle Luna 654', 46001, 'Valencia', 'España'),
(6, 'Laura', 'Rodríguez', 'laura.rodriguez@example.com', 'Calle Estrella 987', 50001, 'Zaragoza', 'España'),
(7, 'Carlos', 'Hernández', 'carlos.hernandez@example.com', 'Calle Río 135', 15001, 'La Coruña', 'España'),
(8, 'Isabel', 'Jiménez', 'isabel.jimenez@example.com', 'Calle Mar 246', 37001, 'Salamanca', 'España'),
(9, 'Javier', 'Torres', 'javier.torres@example.com', 'Calle Tierra 357', 41001, 'Sevilla', 'España'),
(10, 'Sofía', 'Ramírez', 'sofia.ramirez@example.com', 'Calle Aire 468', 29001, 'Málaga', 'España'),
(11, 'Diego', 'Cruz', 'diego.cruz@example.com', 'Calle Verde 579', 46001, 'Valencia', 'España'),
(12, 'Clara', 'Moreno', 'clara.moreno@example.com', 'Calle Amarillo 680', 8001, 'Barcelona', 'España'),
(13, 'Miguel', 'Vázquez', 'miguel.vazquez@example.com', 'Calle Naranja 791', 28001, 'Madrid', 'España'),
(14, 'Lucía', 'Méndez', 'lucia.mendez@example.com', 'Calle Azul 802', 15001, 'La Coruña', 'España'),
(15, 'Andrés', 'Ponce', 'andres.ponce@example.com', 'Calle Rosa 913', 37001, 'Salamanca', 'España'),
(16, 'Patricia', 'Salas', 'patricia.salas@example.com', 'Calle Lila 024', 50001, 'Zaragoza', 'España'),
(17, 'Fernando', 'Cordero', 'fernando.cordero@example.com', 'Calle Blanco 135', 29001, 'Málaga', 'España'),
(18, 'Victoria', 'Núñez', 'victoria.nunez@example.com', 'Calle Negro 246', 41001, 'Sevilla', 'España'),
(19, 'Alberto', 'Rivas', 'alberto.rivas@example.com', 'Calle Gris 357', 8001, 'Barcelona', 'España'),
(20, 'Gabriela', 'Soto', 'gabriela.soto@example.com', 'Calle Cielo 468', 28001, 'Madrid', 'España'),
(21, 'Samuel', 'Cruz', 'samuel.cruz@example.com', 'Calle Tierra 579', 15001, 'La Coruña', 'España');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `Identificador` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`Identificador`, `nombre`, `descripcion`) VALUES
(1, 'Laptop Dell XPS 13', 'Laptop ultradelgada con pantalla de 13 pulgadas y procesador Intel Core i7.'),
(2, 'Smartphone Samsung Galaxy S21', 'Teléfono inteligente con cámara de 64 MP y pantalla AMOLED de 6.2 pulgadas.'),
(3, 'Auriculares Sony WH-1000XM4', 'Auriculares inalámbricos con cancelación de ruido y sonido de alta calidad.'),
(4, 'Reloj inteligente Apple Watch Series 7', 'Reloj inteligente con seguimiento de salud y notificaciones de smartphone.'),
(5, 'Tableta Apple iPad Pro', 'Tableta de 12.9 pulgadas con chip M1 y soporte para Apple Pencil.'),
(6, 'Cámara Canon EOS R5', 'Cámara sin espejo de fotograma completo con capacidad de grabación en 8K.'),
(7, 'Televisor LG OLED 55\"', 'Televisor OLED de 55 pulgadas con calidad de imagen 4K y HDR.'),
(8, 'Altavoz inteligente Amazon Echo', 'Altavoz con asistente de voz Alexa y capacidades de control del hogar.'),
(9, 'Router Wi-Fi TP-Link Archer AX50', 'Router Wi-Fi 6 de alta velocidad para una conectividad rápida y estable.'),
(10, 'Disco duro externo Seagate 2TB', 'Disco duro externo portátil de 2TB con conectividad USB 3.0.'),
(11, 'Teclado mecánico Razer BlackWidow', 'Teclado mecánico con retroiluminación RGB y switches mecánicos Razer.'),
(12, 'Mouse Logitech MX Master 3', 'Mouse ergonómico con múltiples botones programables y conectividad Bluetooth.'),
(13, 'Monitor ASUS 27\"', 'Monitor de 27 pulgadas con resolución 1440p y tiempo de respuesta rápido.'),
(14, 'Impresora HP LaserJet Pro', 'Impresora láser de alta velocidad y calidad para oficina.'),
(15, 'Proyector Epson Home Cinema', 'Proyector 4K para cine en casa con calidad de imagen excepcional.'),
(16, 'Bicicleta de montaña Trek Marlin 7', 'Bicicleta de montaña con suspensión delantera y marco ligero.'),
(17, 'Patinete eléctrico Xiaomi Mi', 'Patinete eléctrico plegable con batería de larga duración.'),
(18, 'Cafetera Nespresso Vertuo', 'Cafetera de cápsulas que prepara café y espresso con un solo botón.'),
(19, 'Aspiradora robot Roomba 675', 'Aspiradora robot que limpia automáticamente y se controla desde el móvil.'),
(20, 'Silla ergonómica Hbada', 'Silla de oficina ergonómica con soporte lumbar y ajuste de altura.'),
(21, 'Mochila para laptop Targus', 'Mochila con compartimento acolchado para laptop y múltiples bolsillos.');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`Identificador`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`Identificador`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`Identificador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `Identificador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `Identificador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `Identificador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
