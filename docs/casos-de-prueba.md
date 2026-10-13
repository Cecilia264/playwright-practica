# Casos de Prueba - Biblioteca

## Login

### TC-001 - Login con credenciales válidas
**Precondición:** El usuario se encuentra en la pantalla de login.

**Datos de prueba:** 
- Usuario: admin
- Contraseña: 1234

**Pasos:**
1. Ingresar el usuario `admin`.
2. Ingresar la contraseña `1234`.
3. Presionar el botón "Ingresar".

**Resultado esperado:** 
El sistema debe permitir el acceso y mostrar la página de la biblioteca.

**Resultado obtenido:** 
El sistema permite el acceso y muestra la página de la biblioteca.

**Estado:** 
PASS


### TC-002 - Login con usuario incorrecto
**Precondición:** El usuario se encuentra en la pantalla de login.

**Datos de prueba:** 
- Usuario: usuario_inexitente
- Contraseña: 1234

**Pasos:**
1. Ingresar un usuario inexistente.
2. Ingresar la contraseña `1234`.
3. Presionar el botón "Ingresar".

**Resultado esperado:** 
El sistema debe rechazar el acceso e informar que las credenciales son incorrectas.

**Resultado obtenido:** 
El sistema rechaza el acceso y muestra el mensaje "Usuario o contraseña incorrectos."

**Estado:** 
PASS


### TC-003 - Login con contraseña incorrecta
**Precondición:** El usuario se encuentra en la pantalla de login.

**Datos de prueba:** 
- Usuario: admin
- Contraseña: contraseña_incorrecta

**Pasos:**
1. Ingresar el usuario `admin`.
2. Ingresar una contraseña incorrecta.
3. Presionar el botón "Ingresar".

**Resultado esperado:** 
El sistema debe rechazar el acceso e informar que las credenciales son incorrectas.

**Resultado obtenido:** 
El sistema rechaza el acceso y muestra el mensaje "Usuario o contraseña incorrectos."

**Estado:** 
PASS


### TC-004 - Login con campos vacíos
**Precondición:** El usuario se encuentre en la pantalla de login.

**Pasos:**
1. No ingresar usuario.
2. No ingresar contraseña.
3. Presionar el botón "Ingresar".

**Resultado esperado:** 
El sistema no debe permitir el acceso y debe solicitar completar los campos obligatorios.

**Resultado obtenido:** 
El sistema no permite continuar con los campos vacíos y muestra el mensaje "Rellene este campo" en los campos obligatorios.

**Estado:** 
PASS


### TC-005 - Usuario vacío y contraseña válida
**Precondición:** El usuario se encuentre en la pantalla de login.

**Pasos:**
1. No ingresar usuario.
2. Ingresar la contraseña `1234`.
3. Presionar el botón "Ingresar".

**Resultado esperado:** 
El sistema no debe permitir el acceso y debe solicitar completar los campos obligatorios.

**Resultado obtenido:** 
El sistema no permite continuar con el campo correspondiente vacío

**Estado:** 
PASS


### TC-006 - Usuario válido y contraseña vacía
**Precondición:** El usuario se encuentre en la pantalla de login.

**Pasos:**
1. Ingresar el usuario `admin`.
2. No ingresar contraseña.
3. Presionar el botón "Ingresar".

**Resultado esperado:** 
El sistema no debe permitir el acceso y debe solicitar completar los campos obligatorios.

**Resultado obtenido:** 
El sistema no permite continuar con el campo correspondiente vacío

**Estado:** 
PASS


### TC-007 - Alta de persona exitosa
**Precondición:** El usuario ha iniciado sesión correctamente y se encuentra en la pantalla de Biblioteca.

**Pasos:**
1. Completar el campo "Nombre" con un valor válido (ej: "Cecilia").
2. Completar el campo "Apellido" con un valor válido (ej: "Cometto").
3. Completar el campo "DNI" con un valor válido (ej: "43770588").
4. Hacer clic en el botón "Agregar persona".

**Resultado Esperado:** Se agrega una nueva fila en la tabla de personas con los datos ingresados.

**Estado:** 
PASS


### TC-008 - Baja/Eliminación de persona
**Precondición:** Existe al menos una persona registrada en la tabla.

**Pasos:**
1. Ubicar la fila de la persona a eliminar mediante su DNI o Nombre.
2. Hacer clic en el botón "Eliminar" correspondiente a esa fila.
3. Aceptar la alerta emergente de confirmación de JavaScript.

**Resultado Esperado:** La persona seleccionada se elimina y ya no figura visible en la tabla.


### TC-009 - Edición de persona exitosa
**Precondición:** Existe al menos una persona registrada en la tabla.

**Pasos:**
1. Ubicar la fila de la persona a modificar mediante su DNI o Nombre.
2. Hacer clic en el botón "Editar" de esa fila.
3. Modificar los campos en el formulario con los nuevos datos (Nombre, Apellido, DNI).
4. Hacer clic en el botón "Guardar" / "Agregar persona".

**Resultado Esperado:** La fila correspondiente en la tabla se actualiza mostrando los datos modificados.

**Estado:** 
PASS