import mysql.connector

# ============================
# Conexión a la base de datos
# ============================
def conectar():
    return mysql.connector.connect(
        host="localhost",    # Cambia según tu configuración
        user="root",         # Tu usuario de MySQL
        password="root",     # Tu contraseña de MySQL
        database="sistemadeventasenlinea"  # Nombre de tu base de datos
    )

# ============================
# Funciones de Productos
# ============================

def agregar_producto(nombre, categoria, precio, stock):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'INSERT INTO Productos (Nombre, Categoria, Precio, Stock) VALUES (%s, %s, %s, %s)'
    cursor.execute(consulta, (nombre, categoria, precio, stock))
    conexion.commit()
    print(f"Producto '{nombre}' agregado con éxito.")
    conexion.close()

def ver_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    conexion.close()

def actualizar_producto(ID_Producto, nombre=None, categoria=None, precio=None, stock=None):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "UPDATE Productos SET "
    valores = []
    
    if nombre:
        consulta += "Nombre = %s, "
        valores.append(nombre)
    if categoria:
        consulta += "Categoria = %s, "
        valores.append(categoria)
    if precio:
        consulta += "Precio = %s, "
        valores.append(precio)
    if stock:
        consulta += "Stock = %s, "
        valores.append(stock)

    consulta = consulta.rstrip(", ") + " WHERE ID_Producto = %s"
    valores.append(ID_Producto)
    cursor.execute(consulta, valores)
    conexion.commit()
    print(f"Producto con ID {ID_Producto} actualizado.")
    conexion.close()

def eliminar_producto(ID_Producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Productos WHERE ID_Producto = %s", (ID_Producto,))
    conexion.commit()
    print(f"Producto con ID {ID_Producto} eliminado.")
    conexion.close()

def reporte_producto_mas_vendido():
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Consulta para calcular el producto más vendido
    consulta = """
    SELECT 
        p.ID_Producto, 
        p.Nombre, 
        SUM(d.Cantidad) AS Cantidad_Total
    FROM 
        Detalles_Orden d
    JOIN 
        Productos p ON d.ID_Producto = p.ID_Producto
    GROUP BY 
        p.ID_Producto
    ORDER BY 
        Cantidad_Total DESC
    LIMIT 1;
    """
    
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    
    if resultado:
        print("\n--- Reporte del Producto Más Vendido ---")
        print(f"ID del Producto: {resultado[0]}")
        print(f"Nombre del Producto: {resultado[1]}")
        print(f"Cantidad Total Vendida: {resultado[2]}")
    else:
        print("\nNo se encontraron ventas registradas.")
    
    conexion.close()

def actualizar_precio_producto(ID_Producto, nuevo_precio):
    """Actualiza solo el precio de un producto especificado por su ID."""
    conexion = conectar()
    cursor = conexion.cursor()
    
    try:
        consulta = "UPDATE Productos SET Precio = %s WHERE ID_Producto = %s"
        cursor.execute(consulta, (nuevo_precio, ID_Producto))
        conexion.commit()
        print(f"El precio del producto con ID {ID_Producto} ha sido actualizado a {nuevo_precio}.")
    except mysql.connector.Error as e:
        print(f"Error al actualizar el precio: {e}")
    finally:
        conexion.close()

def buscar_productos(nombre=None, categoria=None, precio_min=None, precio_max=None, stock_min=None, stock_max=None):
    conexion = conectar()
    cursor = conexion.cursor()
    
    consulta = "SELECT * FROM Productos WHERE 1=1"
    valores = []
    
    if nombre:
        consulta += " AND Nombre LIKE %s"
        valores.append(f"%{nombre}%")
    if categoria:
        consulta += " AND Categoria = %s"
        valores.append(categoria)
    if precio_min is not None:
        consulta += " AND Precio >= %s"
        valores.append(precio_min)
    if precio_max is not None:
        consulta += " AND Precio <= %s"
        valores.append(precio_max)
    if stock_min is not None:
        consulta += " AND Stock >= %s"
        valores.append(stock_min)
    if stock_max is not None:
        consulta += " AND Stock <= %s"
        valores.append(stock_max)
    
    cursor.execute(consulta, valores)
    resultados = cursor.fetchall()
    
    if resultados:
        print(f"{'ID':<5} {'Nombre':<20} {'Categoría':<15} {'Precio':<10} {'Stock':<10}")
        print("-" * 60)
        for producto in resultados:
            print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<15} {producto[3]:<10} {producto[4]:<10}")
    else:
        print("No se encontraron productos que coincidan con los criterios.")
    
    conexion.close()


# ============================
# Funciones de Clientes
# ============================

def registrar_cliente(Nombre, Email, Direccion, Telefono):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'INSERT INTO Clientes (Nombre, Email, Direccion, Telefono) VALUES (%s, %s, %s, %s)'
    cursor.execute(consulta, (Nombre, Email, Direccion, Telefono))
    conexion.commit()
    print(f"Cliente '{Nombre}' registrado con éxito.")
    conexion.close()

def ver_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
    conexion.close()

def buscar_clientes(nombre=None, email=None):
    conexion = conectar()
    cursor = conexion.cursor()
    
    consulta = "SELECT * FROM Clientes WHERE 1=1"
    valores = []
    
    if nombre:
        consulta += " AND Nombre LIKE %s"
        valores.append(f"%{nombre}%")
    if email:
        consulta += " AND Email LIKE %s"
        valores.append(f"%{email}%")
    
    cursor.execute(consulta, valores)
    resultados = cursor.fetchall()
    
    if resultados:
        print(f"{'ID':<5} {'Nombre':<20} {'Email':<25} {'Dirección':<40} {'Teléfono':<15}")
        print("-" * 100)
        for cliente in resultados:
            print(f"{cliente[0]:<5} {cliente[1]:<20} {cliente[2]:<25} {cliente[3]:<40} {cliente[4]:<15}")
    else:
        print("No se encontraron clientes que coincidan con los criterios.")
    
    conexion.close()

def actualizar_cliente(ID_Cliente, Nombre=None, Email=None, Direccion=None, Telefono=None):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "UPDATE Clientes SET "
    valores = []
    
    if Nombre:
        consulta += "Nombre = %s, "
        valores.append(Nombre)
    if Email:
        consulta += "Email = %s, "
        valores.append(Email)
    if Direccion:
        consulta += "Direccion = %s, "
        valores.append(Direccion)
    if Telefono:
        consulta += "Telefono = %s, "
        valores.append(Telefono)

    consulta = consulta.rstrip(", ") + " WHERE ID_Cliente = %s"
    valores.append(ID_Cliente)
    cursor.execute(consulta, valores)
    conexion.commit()
    print(f"Cliente con ID {ID_Cliente} actualizado.")
    conexion.close()

# ============================
# Funciones de Órdenes
# ============================

def registrar_orden(ID_Cliente, Fecha, Detalles):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        consulta_orden = 'INSERT INTO Ordenes (ID_Cliente, Fecha) VALUES (%s, %s)'
        cursor.execute(consulta_orden, (ID_Cliente, Fecha))
        conexion.commit()
        
        ID_Orden = cursor.lastrowid
        
        consulta_stock = 'SELECT Stock FROM Productos WHERE ID_Producto = %s FOR UPDATE'
        consulta_actualizar_stock = 'UPDATE Productos SET Stock = Stock - %s WHERE ID_Producto = %s'
        consulta_detalle = 'INSERT INTO Detalles_Orden (ID_Orden, ID_Producto, Cantidad) VALUES (%s, %s, %s)'
        
        for detalle in Detalles:
            ID_Producto = detalle['ID_Producto']
            Cantidad = int(detalle['Cantidad'])
            
            cursor.execute(consulta_stock, (ID_Producto,))
            resultado = cursor.fetchone()
            
            if resultado is None:
                print(f"Error: El producto con ID {ID_Producto} no existe.")
                continue
            
            stock_disponible = resultado[0]
            
            if Cantidad > stock_disponible:
                print(f"Stock insuficiente para el producto {ID_Producto}. Disponible: {stock_disponible}, requerido: {Cantidad}.")
                continue
            
            cursor.execute(consulta_detalle, (ID_Orden, ID_Producto, Cantidad))
            cursor.execute(consulta_actualizar_stock, (Cantidad, ID_Producto))
        
        conexion.commit()
        print(f"Orden registrada con éxito. ID de la orden: {ID_Orden}")
    except mysql.connector.Error as e:
        print(f"Error al registrar la orden: {e}")
        conexion.rollback()
    finally:
        conexion.close()

def ver_ordenes():
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = '''
    SELECT o.ID_Orden, c.ID_Cliente, o.Fecha
    FROM Ordenes o
    JOIN Clientes c ON o.ID_Cliente = c.ID_Cliente
    '''
    cursor.execute(consulta)
    ordenes = cursor.fetchall()
    for orden in ordenes:
        print(f"ID_Orden: {orden[0]}, ID_Cliente: {orden[1]}, Fecha: {orden[2]}")
    conexion.close()

def ver_ordenes_por_cliente(ID_Cliente):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = '''
    SELECT o.ID_Orden, o.Fecha
    FROM Ordenes o
    WHERE o.ID_Cliente = %s
    '''
    cursor.execute(consulta, (ID_Cliente,))
    ordenes = cursor.fetchall()
    for orden in ordenes:
        print(f"ID_Orden: {orden[0]}, Fecha: {orden[1]}")
    conexion.close()

# ============================
# Funciones del Menú
# ============================

#Menú de agregación de productos

def menu_agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría: ")
    precio = input("Ingrese el precio: ")
    stock = input("Ingrese el stock actual: ")
    agregar_producto(nombre, categoria, precio, stock)

#Menú de modificación de productos

def menu_modificar_producto():
    ver_productos()
    id_producto = input("Ingrese el ID del producto a modificar: ")
    nombre = input("Ingrese el nuevo nombre del producto (deje vacío para no modificar): ")
    categoria = input("Ingrese la nueva categoría (deje vacío para no modificar): ")
    precio = input("Ingrese el nuevo precio (deje vacío para no modificar): ")
    stock = input("Ingrese el nuevo stock (deje vacío para no modificar): ")
    actualizar_producto(
        id_producto,
        nombre or None,
        categoria or None,
        precio or None,
        stock or None
    )

#Menú de modificación de producto por precio

def menu_modificar_precio_producto():
    ver_productos()
    id_producto = input("Ingrese el ID del producto al que desea modificar el precio: ")
    nuevo_precio = input("Ingrese el nuevo precio del producto: ")
    try:
        nuevo_precio = float(nuevo_precio)
        actualizar_precio_producto(id_producto, nuevo_precio)
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para el precio.")

#Menú de búsqueda de productos

def menu_buscar_productos():
    print("\n--- Filtros de búsqueda ---")
    nombre = input("Nombre del producto (opcional): ")
    categoria = input("Categoría del producto (opcional): ")
    precio_min = input("Precio mínimo (opcional): ")
    precio_max = input("Precio máximo (opcional): ")
    stock_min = input("Stock mínimo (opcional): ")
    stock_max = input("Stock máximo (opcional): ")

    buscar_productos(
        nombre=nombre or None,
        categoria=categoria or None,
        precio_min=float(precio_min) if precio_min else None,
        precio_max=float(precio_max) if precio_max else None,
        stock_min=int(stock_min) if stock_min else None,
        stock_max=int(stock_max) if stock_max else None
    )

#Menú de eliminación de productos

def menu_eliminar_producto():
    ver_productos()
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    eliminar_producto(id_producto)

#Menú de agregación de clientes

def menu_registrar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    registrar_cliente(nombre, email, direccion, telefono)

#Menú de modificación de clientes

def menu_modificar_cliente():
    ver_clientes()
    id_cliente = input("Ingrese el ID del cliente a modificar: ")
    nombre = input("Ingrese el nuevo nombre del cliente (deje vacío para no modificar): ")
    email = input("Ingrese el nuevo email (deje vacío para no modificar): ")
    direccion = input("Ingrese la nueva dirección (deje vacío para no modificar): ")
    telefono = input("Ingrese el nuevo teléfono (deje vacío para no modificar): ")
    actualizar_cliente(
        id_cliente,
        nombre or None,
        email or None,
        direccion or None,
        telefono or None
    )

#Menú de registro de órdenes

def menu_registrar_orden():
    ver_clientes()
    id_cliente = input("Ingrese el ID del cliente: ")
    fecha = input("Ingrese la fecha de la orden (YYYY-MM-DD): ")
    detalles = []
    ver_productos()
    id_producto = input("Ingrese el ID del producto (o 'salir' para finalizar): ")
    cantidad = input("Ingrese la cantidad: ")
    detalles.append({'ID_Producto': id_producto, 'Cantidad': cantidad})
    registrar_orden(id_cliente, fecha, detalles)  

# Menú para productos
def SubMenuProductos():
    Funcionamiento = True
    while Funcionamiento:
        print("\n--- Menú Productos ---")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")  
        print("5. Salir")
        
        opcion = int(input("Elija su opción: "))
        
        if opcion == 1:
            ver_productos()
        elif opcion == 2:
            menu_agregar_producto()
        elif opcion == 3:
            menu_modificar_producto()
        elif opcion == 4:
            menu_eliminar_producto()
        elif opcion == 5:
            print("Saliste del Menú Productos.")
            Funcionamiento = False
        else:
            print("Opción no válida. Intente de nuevo.")

# Menú para clientes
def SubMenuClientes():
    Funcionamiento = True
    while Funcionamiento:
        print("\n--- Menú Clientes ---")
        print("1. Listar clientes")
        print("2. Registrar cliente")
        print("3. Modificar cliente")
        print("4. Salir")
        
        opcion = int(input("Elija su opción: "))
        
        if opcion == 1:
            ver_clientes()
        elif opcion == 2:
            menu_registrar_cliente()
        elif opcion == 3:
            menu_modificar_cliente()
        elif opcion == 4:
            print("Saliste del Menú Clientes.")
            Funcionamiento = False
        else:
            print("Opción no válida. Intente de nuevo.")

# Menú principal
def menu_principal():
    Funcionamiento = True
    while Funcionamiento:
        print("\n--- Menú Principal ---")
        print("1. Para desplegar el menú productos")
        print("2. Para desplegar el menú clientes")
        print("3. Mostrar órdenes registradas")
        print("4. Registrar orden (Comprar)")
        print("5. Buscar productos")
        print("6. Reporte: Producto más vendido")
        print("7. Modificar precio de un producto")
        print("8. Buscar clientes")
        print("9. Ver órdenes de un cliente")
        print("10. Salir")
        
        opcion = input("Elija su opción: ")
        
        if opcion == '1':
            SubMenuProductos()        
        elif opcion == '2':
            SubMenuClientes()
        elif opcion == '3':
            ver_ordenes()
        elif opcion == '4':
            menu_registrar_orden()
        elif opcion == '5':
            menu_buscar_productos()
        elif opcion == '6':
            reporte_producto_mas_vendido()
        elif opcion == '7':
            menu_modificar_precio_producto()
        elif opcion == '8':
            buscar_clientes()
        elif opcion == '9':
            id_cliente = input("Ingrese el ID del cliente para ver sus órdenes: ")
            ver_ordenes_por_cliente(id_cliente)
        elif opcion == '10':
            print("Saliendo del sistema. ¡Hasta pronto!")
            Funcionamiento = False
        else:
            print("Opción no válida. Intente de nuevo.")
