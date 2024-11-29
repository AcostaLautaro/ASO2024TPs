
# Justificación del Diseño de la Base de Datos

## Modelo de la Base de Datos

El diseño de la base de datos se realizó para un sistema de ventas en línea, en el que se gestionan tres entidades principales: Productos, Clientes y Órdenes. A continuación, se describe cómo fue estructurada la base de datos y el proceso de normalización.

### Entidades y Relaciones

#### Productos:
- **Descripción:** Esta entidad contiene los detalles de los productos que se venden en el sistema.
- **Atributos:** 
  - ID_Producto (clave primaria)
  - Nombre
  - Categoria
  - Precio
  - Stock

#### Clientes:
- **Descripción:** Esta entidad almacena los datos de los clientes que realizan compras.
- **Atributos:** 
  - ID_Cliente (clave primaria)
  - Nombre
  - Email
  - Direccion
  - Telefono

#### Órdenes:
- **Descripción:** Cada vez que un cliente realiza una compra, se crea una orden, que contiene un conjunto de productos comprados.
- **Atributos:** 
  - ID_Orden (clave primaria)
  - ID_Cliente (clave foránea referenciando a Clientes)
  - Fecha

#### Detalles_Orden:
- **Descripción:** Relaciona los productos con las órdenes, ya que una orden puede contener múltiples productos.
- **Atributos:** 
  - ID_Orden (clave foránea referenciando a Órdenes)
  - ID_Producto (clave foránea referenciando a Productos)
  - Cantidad

#### Relaciones:
- Clientes pueden tener muchas Órdenes, por lo que la relación entre Clientes y Órdenes es de tipo uno a muchos.
- Órdenes pueden contener muchos Productos, y cada Producto puede estar en muchas Órdenes, lo que genera una relación de muchos a muchos entre Órdenes y Productos. Esta relación se resuelve con la tabla Detalles_Orden.

### Proceso de Normalización

#### 1. Primera Forma Normal (1NF)
En esta etapa, se asegura que todas las tablas cumplen con los siguientes requisitos:
- **Dominio de atributos:** Todos los atributos tienen un valor atómico (es decir, no tienen valores repetidos ni conjuntos de valores).
- **Identificación única de filas:** Cada fila en la tabla tiene una clave primaria única.

Para las tablas del sistema de ventas en línea, los atributos son atómicos, y las claves primarias (ID_Producto, ID_Cliente, ID_Orden) identifican de forma única cada registro. Se eliminan los conjuntos de datos repetidos y se aseguraron valores atómicos.

#### 2. Segunda Forma Normal (2NF)
La 2NF requiere que:
1. La base de datos esté en 1NF.
2. Todos los atributos no clave dependan completamente de la clave primaria.

En el diseño actual:
- En la tabla **Productos**, todos los atributos dependen completamente de la clave primaria ID_Producto.
- En la tabla **Clientes**, todos los atributos dependen completamente de la clave primaria ID_Cliente.
- En la tabla **Órdenes**, todos los atributos dependen completamente de la clave primaria ID_Orden.
- En la tabla **Detalles_Orden**, la combinación de ID_Orden y ID_Producto es la clave primaria compuesta, y ambos atributos dependen completamente de esta combinación.

No existen dependencias parciales entre los atributos y las claves primarias, por lo que la base de datos está en 2NF.

#### 3. Tercera Forma Normal (3NF)
La 3NF requiere que:
1. La base de datos esté en 2NF.
2. No haya dependencias transitivas, es decir, no debe haber atributos que dependan de otros atributos no clave.

En nuestro caso:
- En la tabla **Productos**, no hay dependencias transitivas, ya que el precio y el stock dependen solo de ID_Producto.
- En la tabla **Clientes**, los atributos Nombre, Email, Direccion, y Telefono dependen directamente de ID_Cliente, y no de otro atributo.
- En la tabla **Órdenes**, no hay atributos adicionales que dependan de otros atributos no clave.
- En la tabla **Detalles_Orden**, los atributos Cantidad dependen directamente de la combinación de ID_Orden y ID_Producto.

No existen dependencias transitivas, por lo que la base de datos cumple con 3NF.

### Modelo Final de la Base de Datos

#### Tablas:
**Productos**
- ID_Producto (PK)
- Nombre
- Categoria
- Precio
- Stock

**Clientes**
- ID_Cliente (PK)
- Nombre
- Email
- Direccion
- Telefono

**Órdenes**
- ID_Orden (PK)
- ID_Cliente (FK)
- Fecha

**Detalles_Orden**
- ID_Orden (FK)
- ID_Producto (FK)
- Cantidad

#### Relaciones:
- **Clientes (1) → Órdenes (M)**
- **Órdenes (M) → Productos (M)** (a través de Detalles_Orden)
