-- Creación de la base de datos
CREATE DATABASE SistemaVentas;
USE SistemaVentas;

-- Tabla Clientes
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    direccion TEXT,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla Productos
CREATE TABLE Productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla Órdenes
CREATE TABLE Ordenes (
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla Detalles de Órdenes
CREATE TABLE Detalles_Orden (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_orden INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Inserción de datos de prueba

-- Insertar clientes
INSERT INTO Clientes (nombre, email, telefono, direccion) VALUES
('Juan Pérez', 'juan.perez@example.com', '123456789', 'Calle Falsa 123'),
('Ana Gómez', 'ana.gomez@example.com', '987654321', 'Avenida Libertador 456');

-- Insertar productos
INSERT INTO Productos (nombre, categoria, precio, stock) VALUES
('Producto A', 'Categoria 1', 19.99, 50),
('Producto B', 'Categoria 2', 9.99, 100);

-- Insertar órdenes
INSERT INTO Ordenes (id_cliente, fecha, total) VALUES
(1, '2024-11-29', 100.50),
(2, '2024-11-28', 49.99);

-- Insertar detalles de órdenes
INSERT INTO Detalles_Orden (id_orden, id_producto, cantidad, subtotal) VALUES
(1, 1, 2, 39.98),
(1, 2, 1, 9.99),
(2, 2, 5, 49.95);
