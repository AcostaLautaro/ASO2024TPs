# Ejercicio: Estadías(2)

**Esquema de BD:**

`ESTADIA<dniCliente, codHotel, cantidadHabitaciones, direccionHotel, ciudadHotel, dniGerente, nombreGerente, nombreCliente, ciudadCliente, fechaInicioHospedaje, cantDiasHospedaje, #Habitacion>`

### Restricciones:
1. Existe un único gerente por hotel. Un gerente puede gerenciar más de un hotel.
2. Un cliente puede realizar la estadía en más de una habitación del mismo hotel en la misma fecha. Para cada habitación puede reservar diferentes cantidades de días.
3. `cantidadHabitaciones` indica la cantidad de habitaciones existentes en un hotel.
4. `codHotel` es único y no se repite en diferentes ciudades.
5. Un cliente puede realizar reservas en diferentes hoteles para la misma fecha.
6. `#Habitacion` puede repetirse en distintos hoteles.
7. En la misma `direccionHotel` de una `ciudadHotel` puede haber más de un hotel funcionando.

---

## Paso 1: Determinar las Dependencias Funcionales (DFs)
A partir del esquema y las restricciones, las dependencias funcionales son:
1. **dniCliente → nombreCliente, ciudadCliente**  
   Cada cliente tiene un nombre y ciudad únicos.
   
2. **codHotel → direccionHotel, ciudadHotel, dniGerente, cantidadHabitaciones**  
   Cada hotel tiene un código único que determina estas características.

3. **dniGerente → nombreGerente**  
   Un gerente tiene un nombre único asociado a su DNI.

4. **(dniCliente, codHotel, #Habitacion) → fechaInicioHospedaje, cantDiasHospedaje**  
   La combinación de cliente, hotel y habitación identifica de manera única la fecha y días de hospedaje.

5. **codHotel, ciudadHotel → direccionHotel**  
   Un código de hotel en una ciudad identifica su dirección.

---

## Paso 2: Determinar las Claves Candidatas
Analizando las dependencias funcionales, las claves candidatas son:
- **(dniCliente, codHotel, #Habitacion)**: Identifica de forma única cada estadía.  
Esta clave se elige como **clave primaria**, ya que permite manejar reservas específicas por habitación y cliente.

---

## Paso 3: Diseño en Tercera Forma Normal (3FN)

### 1FN: Primera Forma Normal
El esquema original ya está en 1FN porque todos los atributos son atómicos.

### 2FN: Segunda Forma Normal
Para eliminar dependencias parciales, dividimos el esquema:
1. **dniCliente → nombreCliente, ciudadCliente** se mueve a la tabla `Clientes`.
2. **codHotel → direccionHotel, ciudadHotel, dniGerente, cantidadHabitaciones** se mueve a `Hoteles`.
3. **dniGerente → nombreGerente** se traslada a `Gerentes`.

### 3FN: Tercera Forma Normal
Eliminamos dependencias transitivas, asegurándonos de que cada atributo no clave dependa únicamente de la clave primaria completa.

---

### Diseño Normalizado en 3FN:
1. **Tabla `Clientes`**
   - **dniCliente** (Clave primaria)
   - nombreCliente  
   - ciudadCliente  

2. **Tabla `Hoteles`**
   - **codHotel** (Clave primaria)
   - direccionHotel  
   - ciudadHotel  
   - dniGerente (Clave foránea a `Gerentes`)  
   - cantidadHabitaciones  

3. **Tabla `Gerentes`**
   - **dniGerente** (Clave primaria)
   - nombreGerente  

4. **Tabla `Estadías`**
   - **dniCliente** (Clave foránea a `Clientes`)  
   - **codHotel** (Clave foránea a `Hoteles`)  
   - **#Habitacion**  
   - fechaInicioHospedaje  
   - cantDiasHospedaje  
   - **Clave primaria compuesta**: (dniCliente, codHotel, #Habitacion)

---

## Justificación del Proceso
El diseño propuesto:
1. **Reduce redundancia**: Centraliza datos como clientes y hoteles en tablas específicas.
2. **Asegura integridad**: Evita inconsistencias al actualizar datos.
3. **Cumple las restricciones**: Respeta todas las reglas planteadas en el enunciado, incluyendo las relaciones entre clientes, hoteles y habitaciones.





