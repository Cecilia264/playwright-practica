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