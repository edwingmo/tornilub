-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-04-2022 a las 03:40:59
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ecommerce`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accounts_user`
--

CREATE TABLE `accounts_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `company_name` varchar(150) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superadmin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `accounts_user`
--

INSERT INTO `accounts_user` (`id`, `password`, `first_name`, `last_name`, `username`, `email`, `phone_number`, `company_name`, `date_joined`, `last_login`, `is_admin`, `is_staff`, `is_active`, `is_superadmin`) VALUES
(1, 'pbkdf2_sha256$320000$9Jx1t6yWrTw7v6WtJf9zCS$pw2k51h+VXvpAK/md6uOFqZI848biNzCF0/Yv76yczY=', 'Edwing', 'Monrroy', 'Edwing', 'monrroyedwing@gmail.com', '', '', '2022-04-18 00:00:00.000000', '2022-04-25 00:26:12.311192', 1, 1, 1, 1),
(47, 'pbkdf2_sha256$320000$0VHaDuRUzaGaLvTnwQnfy6$sGdnDUAtBnnB3zz21w8wIX91rgov1QQDefev8CIQ4us=', 'Edwing', 'Monrroy', 'Edwingmo', 'emonrroy@tornilub.com', '', '', '2022-04-25 00:44:30.918436', '2022-04-25 00:44:30.899908', 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Categoria', 6, 'add_categoria'),
(22, 'Can change Categoria', 6, 'change_categoria'),
(23, 'Can delete Categoria', 6, 'delete_categoria'),
(24, 'Can view Categoria', 6, 'view_categoria'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add productos', 8, 'add_productos'),
(30, 'Can change productos', 8, 'change_productos'),
(31, 'Can delete productos', 8, 'delete_productos'),
(32, 'Can view productos', 8, 'view_productos'),
(33, 'Can add carrito', 9, 'add_carrito'),
(34, 'Can change carrito', 9, 'change_carrito'),
(35, 'Can delete carrito', 9, 'delete_carrito'),
(36, 'Can view carrito', 9, 'view_carrito'),
(37, 'Can add cart item', 10, 'add_cartitem'),
(38, 'Can change cart item', 10, 'change_cartitem'),
(39, 'Can delete cart item', 10, 'delete_cartitem'),
(40, 'Can view cart item', 10, 'view_cartitem');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito_carrito`
--

CREATE TABLE `carrito_carrito` (
  `id` bigint(20) NOT NULL,
  `id_carrito` varchar(250) NOT NULL,
  `date_added` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carrito_carrito`
--

INSERT INTO `carrito_carrito` (`id`, `id_carrito`, `date_added`) VALUES
(1, 'bvks1f5lk14xffh129yv1g3ie95v0wj8', '2022-04-19');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito_cartitem`
--

CREATE TABLE `carrito_cartitem` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `carrito_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_categoria`
--

CREATE TABLE `categoria_categoria` (
  `id` bigint(20) NOT NULL,
  `categoria_nombre` varchar(100) NOT NULL,
  `categoria_descripcion` varchar(250) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `imagen_categoria` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categoria_categoria`
--

INSERT INTO `categoria_categoria` (`id`, `categoria_nombre`, `categoria_descripcion`, `slug`, `imagen_categoria`) VALUES
(7, 'Secadores', '', 'secadores', 'photos/categoria/CM10_ABB.png'),
(8, 'Filtro de aire', '', 'filtro-de-aire', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-04-19 23:47:29.820975', '1', 'asdasd', 1, '[{\"added\": {}}]', 6, 1),
(2, '2022-04-19 23:48:02.228388', '1', 'asdasd', 3, '', 6, 1),
(3, '2022-04-19 23:48:31.677349', '2', 'Charts', 1, '[{\"added\": {}}]', 6, 1),
(4, '2022-04-19 23:48:39.371344', '3', 'Players', 1, '[{\"added\": {}}]', 6, 1),
(5, '2022-04-19 23:49:51.676992', '4', 'asdihsdfsdf', 1, '[{\"added\": {}}]', 6, 1),
(6, '2022-04-19 23:49:55.038223', '5', 'asdasdas', 1, '[{\"added\": {}}]', 6, 1),
(7, '2022-04-19 23:49:58.658942', '6', 'asdsfdgcvfg', 1, '[{\"added\": {}}]', 6, 1),
(8, '2022-04-19 23:51:02.913707', '1', 'Pain', 1, '[{\"added\": {}}]', 8, 1),
(9, '2022-04-19 23:55:08.903458', '2', 'asdasd', 1, '[{\"added\": {}}]', 8, 1),
(10, '2022-04-19 23:55:25.015263', '3', 'fghfghfghfgh', 1, '[{\"added\": {}}]', 8, 1),
(11, '2022-04-19 23:55:38.282863', '4', 'fgfgghfgh', 1, '[{\"added\": {}}]', 8, 1),
(12, '2022-04-19 23:56:39.942453', '5', 'sdfsdfsdf', 1, '[{\"added\": {}}]', 8, 1),
(13, '2022-04-19 23:56:47.849549', '6', 'asdasdasd', 1, '[{\"added\": {}}]', 8, 1),
(14, '2022-04-19 23:57:19.603603', '7', 'asdasgdfcvcbnvcb', 1, '[{\"added\": {}}]', 8, 1),
(15, '2022-04-20 15:33:57.299532', '6', 'asdsfdgcvfg', 3, '', 6, 1),
(16, '2022-04-20 15:33:57.306186', '5', 'asdasdas', 3, '', 6, 1),
(17, '2022-04-20 15:33:57.308108', '4', 'asdihsdfsdf', 3, '', 6, 1),
(18, '2022-04-20 15:33:57.310319', '3', 'Players', 3, '', 6, 1),
(19, '2022-04-20 15:33:57.317133', '2', 'Charts', 3, '', 6, 1),
(20, '2022-04-20 17:22:27.639770', '3', 'daniela95rodriguez@gmail.com', 3, '', 7, 1),
(21, '2022-04-20 22:06:56.938186', '11', 'probando2@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Phone number\", \"Is active\"]}}]', 7, 1),
(22, '2022-04-20 22:53:59.978689', '7', 'Secadores', 1, '[{\"added\": {}}]', 6, 1),
(23, '2022-04-20 22:56:19.656162', '8', 'Compresor', 1, '[{\"added\": {}}]', 8, 1),
(24, '2022-04-20 23:12:08.364391', '8', 'Filtro de aire', 1, '[{\"added\": {}}]', 6, 1),
(25, '2022-04-20 23:12:09.838110', '9', 'INGERSOLL RAND', 1, '[{\"added\": {}}]', 8, 1),
(26, '2022-04-20 23:12:46.343136', '9', 'INGERSOLL RAND', 2, '[{\"changed\": {\"fields\": [\"Imagenes\"]}}]', 8, 1),
(27, '2022-04-23 17:31:48.809592', '35', 'emonrroy@tornilub.com', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Username\", \"Phone number\", \"Company name\", \"Is active\"]}}]', 7, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(9, 'carrito', 'carrito'),
(10, 'carrito', 'cartitem'),
(6, 'categoria', 'categoria'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(8, 'tienda', 'productos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'accounts', '0001_initial', '2022-04-18 19:56:34.185471'),
(2, 'contenttypes', '0001_initial', '2022-04-18 19:56:34.230223'),
(3, 'admin', '0001_initial', '2022-04-18 19:56:34.363680'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-04-18 19:56:34.368640'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-04-18 19:56:34.374662'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-04-18 19:56:34.424054'),
(7, 'auth', '0001_initial', '2022-04-18 19:56:34.647896'),
(8, 'auth', '0002_alter_permission_name_max_length', '2022-04-18 19:56:34.692879'),
(9, 'auth', '0003_alter_user_email_max_length', '2022-04-18 19:56:34.698862'),
(10, 'auth', '0004_alter_user_username_opts', '2022-04-18 19:56:34.704875'),
(11, 'auth', '0005_alter_user_last_login_null', '2022-04-18 19:56:34.710830'),
(12, 'auth', '0006_require_contenttypes_0002', '2022-04-18 19:56:34.713823'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2022-04-18 19:56:34.717812'),
(14, 'auth', '0008_alter_user_username_max_length', '2022-04-18 19:56:34.724793'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2022-04-18 19:56:34.730777'),
(16, 'auth', '0010_alter_group_name_max_length', '2022-04-18 19:56:34.743743'),
(17, 'auth', '0011_update_proxy_permissions', '2022-04-18 19:56:34.751721'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2022-04-18 19:56:34.756708'),
(19, 'categoria', '0001_initial', '2022-04-18 19:56:34.780877'),
(20, 'tienda', '0001_initial', '2022-04-18 19:56:34.842430'),
(21, 'tienda', '0002_productos_numero_parte', '2022-04-18 19:56:34.862404'),
(22, 'tienda', '0003_productos_clicks', '2022-04-18 19:56:34.882351'),
(23, 'carrito', '0001_initial', '2022-04-18 19:56:35.004008'),
(24, 'sessions', '0001_initial', '2022-04-18 19:56:35.037277'),
(25, 'accounts', '0002_alter_user_date_joined_alter_user_last_login', '2022-04-21 02:13:14.884549');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5ursxin2f6tr7cblu8k79eqreop3i3no', 'e30:1nimYV:gKg2Lrp0FNkA_XxhVxxRgAa1VkhTYhz6pTAIegIlmAI', '2022-05-09 00:26:19.309150'),
('7iulhvlldnscdbbuupj0ic9t153p1vco', 'e30:1nhIrI:Y0PqJYNokqvPSdgaih3B8ErUooesmQG6IOO1esKEq2E', '2022-05-04 22:31:36.721745'),
('salzzxkbt81w01akup96oqwt3ch8nejk', 'e30:1nhNS8:1Qr2QUobLMjJDreGSHgpCduV3mCLv-Aya0v201Lfuck', '2022-05-05 03:25:56.782828'),
('uobd559fo1v6qswkgw4mj5itkw71ykry', 'e30:1nhNJl:H9Vyi46kYIcybHTEiDxxwM0ResKPOKni2DSFGo8jF9I', '2022-05-05 03:17:17.717106');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tienda_productos`
--

CREATE TABLE `tienda_productos` (
  `id` bigint(20) NOT NULL,
  `nombre_producto` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `precio` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `imagenes` varchar(100) NOT NULL,
  `create_date` date NOT NULL,
  `last_edit` date NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `numero_parte` varchar(50) NOT NULL,
  `clicks` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tienda_productos`
--

INSERT INTO `tienda_productos` (`id`, `nombre_producto`, `slug`, `descripcion`, `precio`, `cantidad`, `stock`, `activo`, `imagenes`, `create_date`, `last_edit`, `category_id`, `numero_parte`, `clicks`) VALUES
(8, 'Compresor', 'compresor', 'Compresor amarillo', 200, 1, 2, 1, 'photos/productos/td_GG5HF2C_Llkesj2.png', '2022-04-20', '2022-04-20', 7, 'RRP500', 11),
(9, 'INGERSOLL RAND', 'ingersoll-rand', 'Compresor de tornillo de BAJA PRESIÓN (SOPLADOR) ROBOX energy ofrece una mayor eficacia debido a una compresión interna junto con el motor de imanes permanentes patentado por ROBUSCHI, este acoplamiento mejora la eficacia frente a la transmisión por correa\r\nProducto de ÚLTIMA TECNOLOGÍA, disponible para Venezuela \r\nsolicite su catalogo', 300, 5, 5, 1, 'photos/productos/IMG_20190919_103633.jpg', '2022-04-20', '2022-04-20', 8, '9056189', 5);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `accounts_user`
--
ALTER TABLE `accounts_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `carrito_carrito`
--
ALTER TABLE `carrito_carrito`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `carrito_cartitem`
--
ALTER TABLE `carrito_cartitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `carrito_cartitem_carrito_id_e61e0689_fk_carrito_carrito_id` (`carrito_id`),
  ADD KEY `carrito_cartitem_product_id_f6bee1b8_fk_tienda_productos_id` (`product_id`);

--
-- Indices de la tabla `categoria_categoria`
--
ALTER TABLE `categoria_categoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `categoria_nombre` (`categoria_nombre`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `tienda_productos`
--
ALTER TABLE `tienda_productos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre_producto` (`nombre_producto`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `tienda_productos_category_id_cfb09c9b_fk_categoria_categoria_id` (`category_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `accounts_user`
--
ALTER TABLE `accounts_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `carrito_carrito`
--
ALTER TABLE `carrito_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `carrito_cartitem`
--
ALTER TABLE `carrito_cartitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `categoria_categoria`
--
ALTER TABLE `categoria_categoria`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `tienda_productos`
--
ALTER TABLE `tienda_productos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `carrito_cartitem`
--
ALTER TABLE `carrito_cartitem`
  ADD CONSTRAINT `carrito_cartitem_carrito_id_e61e0689_fk_carrito_carrito_id` FOREIGN KEY (`carrito_id`) REFERENCES `carrito_carrito` (`id`),
  ADD CONSTRAINT `carrito_cartitem_product_id_f6bee1b8_fk_tienda_productos_id` FOREIGN KEY (`product_id`) REFERENCES `tienda_productos` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Filtros para la tabla `tienda_productos`
--
ALTER TABLE `tienda_productos`
  ADD CONSTRAINT `tienda_productos_category_id_cfb09c9b_fk_categoria_categoria_id` FOREIGN KEY (`category_id`) REFERENCES `categoria_categoria` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
