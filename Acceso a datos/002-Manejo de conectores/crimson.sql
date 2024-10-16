-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-10-2024 a las 20:19:55
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
-- Base de datos: `crimson`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `EspanaEsEs` ()   BEGIN
	UPDATE clientes
    SET pais = 'ES'
    WHERE pais = 'España';
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `SeleccionaClientesBueno` (IN `cadena` VARCHAR(50))   BEGIN
	SELECT
    	CONCAT(nombre,'',apellidos) AS nombrecompleto,
        email,
        direccion,
        poblacion
    FROM clientes
    WHERE nombre LIKE CONCAT ('%', cadena, '%');
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `SeleccionaClientesMalo` ()   BEGIN
	SELECT
    	CONCAT(nombre,' ',apellidos) AS 
nombrecompleto,
        email,
        direccion,
        poblacion
    FROM clientes
    WHERE nombre LIKE '%ju%';
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aplicaciones`
--

CREATE TABLE `aplicaciones` (
  `Identificador` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text NOT NULL,
  `icono` varchar(255) NOT NULL,
  `ruta` varchar(255) NOT NULL,
  `activa` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `aplicaciones`
--

INSERT INTO `aplicaciones` (`Identificador`, `nombre`, `descripcion`, `icono`, `ruta`, `activa`) VALUES
(1, 'CRM', 'Un CRM es un sistema de gestión de la relación con el cliente. Con este sistema vas a poder realizar un seguimiento de tus clientes y de sus pedidos', 'crm.png', 'crm', 1),
(2, 'CMS', 'Un CMS, o Content Management System, es un sistema de gestión de contenidos donde varias personas de la empresa pueden introducir contenidos en texto', 'cms.png', 'cms', 1),
(3, '', '', '', '', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `Identificador` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `cp` varchar(20) NOT NULL,
  `poblacion` varchar(255) NOT NULL,
  `pais` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`Identificador`, `nombre`, `apellidos`, `email`, `direccion`, `cp`, `poblacion`, `pais`) VALUES
(1, 'Luis', 'Lopez', 'luis.lopez@example.com', 'Avenida Central 95', '1070', 'Ciudad de México', 'Venezuela'),
(2, 'Lucia', 'Rodriguez', 'lucia.rodriguez@example.com', 'Calle Secundaria 79', '4000', 'Madrid', 'Colombia'),
(3, 'Carlos', 'Rodriguez', 'carlos.rodriguez@example.com', 'Plaza Principal 8', '1070', 'Quito', 'Guatemala'),
(4, 'Carlos', 'Romero', 'carlos.romero@example.com', 'Avenida Central 15', '22000', 'Caracas', 'México'),
(5, 'Carlos', 'Sanchez', 'carlos.sanchez@example.com', 'Plaza Principal 56', '11001', 'Buenos Aires', 'México'),
(6, 'Alberto', 'Gonzalez', 'alberto.gonzalez@example.com', 'Pasaje Los Pinos 14', '1070', 'Ciudad de México', 'Ecuador'),
(7, 'Miguel', 'Romero', 'miguel.romero@example.com', 'Plaza Principal 48', '1070', 'Valencia', 'Argentina'),
(8, 'Juan', 'Ortiz', 'juan.ortiz@example.com', 'Calle Secundaria 49', '10001', 'Santiago', 'Ecuador'),
(9, 'Miguel', 'Perez', 'miguel.perez@example.com', 'Avenida Central 59', '4000', 'Lima', 'Chile'),
(10, 'Juan', 'Rodriguez', 'juan.rodriguez@example.com', 'Calle Mayor 10', '11001', 'Quito', 'Uruguay'),
(11, 'Maria', 'Martinez', 'maria.martinez@example.com', 'Pasaje Los Pinos 7', '22000', 'Montevideo', 'ES'),
(12, 'Miguel', 'Gonzalez', 'miguel.gonzalez@example.com', 'Plaza Principal 51', '1070', 'Valencia', 'ES'),
(13, 'Carmen', 'Lopez', 'carmen.lopez@example.com', 'Plaza Principal 31', '10001', 'Ciudad de México', 'Chile'),
(14, 'Luis', 'Perez', 'luis.perez@example.com', 'Plaza Principal 29', '830000', 'Montevideo', 'Chile'),
(15, 'Miguel', 'Garcia', 'miguel.garcia@example.com', 'Calle Secundaria 22', '11001', 'Quito', 'ES'),
(16, 'Luis', 'Romero', 'luis.romero@example.com', 'Plaza Principal 47', '28001', 'Madrid', 'Venezuela'),
(18, 'Alberto', 'Rubio', 'alberto.rubio@example.com', 'Plaza Principal 79', '22000', 'Valencia', 'Argentina'),
(19, 'Carmen', 'Martinez', 'carmen.martinez@example.com', 'Calle Secundaria 27', '4000', 'Ciudad de México', 'Ecuador'),
(20, 'Lucia', 'Perez', 'lucia.perez@example.com', 'Pasaje Los Pinos 67', '830000', 'Caracas', 'México');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `peso` decimal(10,2) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `fecha` date NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`id`, `cantidad`, `peso`, `precio`, `fecha`, `descripcion`) VALUES
(1, 15, '0.45', '329.99', '2024-10-15', 'Procesador Intel Core i7-12700K 3.6 GHz'),
(2, 8, '1.35', '699.99', '2024-10-15', 'Tarjeta gráfica NVIDIA GeForce RTX 4070 8GB GDDR6'),
(3, 20, '5.50', '249.99', '2024-10-16', 'Monitor gaming ASUS TUF 27\" 165Hz 1ms'),
(4, 50, '0.08', '89.99', '2024-10-16', 'SSD Samsung 970 EVO Plus 1TB NVMe'),
(5, 30, '1.10', '129.99', '2024-10-17', 'Teclado mecánico Razer BlackWidow V3 Pro'),
(6, 40, '0.15', '49.99', '2024-10-18', 'Ratón inalámbrico Logitech G305 LIGHTSPEED'),
(7, 10, '1.25', '189.99', '2024-10-18', 'Placa base MSI MAG B550 TOMAHAWK AM4 ATX'),
(8, 25, '0.08', '129.99', '2024-10-18', 'Memoria RAM Corsair Vengeance LPX 16GB (2x8GB) DDR4 3200MHz'),
(9, 15, '2.10', '99.99', '2024-10-19', 'Fuente de alimentación Corsair RM750 750W 80 PLUS Gold'),
(10, 5, '21.50', '349.99', '2024-10-20', 'Silla gaming Secretlab TITAN Evo 2024 Series');

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `seleccion_clientes`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `seleccion_clientes` (
`nombrecompleto` varchar(200)
,`email` varchar(255)
,`direccion` varchar(255)
,`poblacion` varchar(255)
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `Identificador` int(11) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Identificador`, `usuario`, `contrasena`, `nombre`, `apellidos`) VALUES
(1, 'jdoe', 'Doe1234!', 'John', 'Doe'),
(2, 'asmith', 'SmithyPass22', 'Alice', 'Smith'),
(3, 'bjohnson', 'BobbyJ2024', 'Bobby', 'Johnson'),
(4, 'cwilliams', 'WillPower99', 'Catherine', 'Williams'),
(5, 'mgarcia', 'GarciaSecure7', 'Marco', 'Garcia');

-- --------------------------------------------------------

--
-- Estructura para la vista `seleccion_clientes`
--
DROP TABLE IF EXISTS `seleccion_clientes`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `seleccion_clientes`  AS SELECT concat(`clientes`.`nombre`,'',`clientes`.`apellidos`) AS `nombrecompleto`, `clientes`.`email` AS `email`, `clientes`.`direccion` AS `direccion`, `clientes`.`poblacion` AS `poblacion` FROM `clientes` WHERE `clientes`.`nombre` like '%ju%''%ju%'  ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `aplicaciones`
--
ALTER TABLE `aplicaciones`
  ADD PRIMARY KEY (`Identificador`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`Identificador`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Identificador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `aplicaciones`
--
ALTER TABLE `aplicaciones`
  MODIFY `Identificador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `Identificador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `Identificador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
