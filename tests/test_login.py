from playwright.sync_api import expect


### TC-001 - Login con credenciales válidas
def test_login_credenciales_validas(login_page):
    login_page.ingresar_credenciales("admin", "1234")
    expect(login_page.titulo_biblioteca).to_be_visible()

    
### TC-002 - Login con usuario incorrecto
def test_login_usuario_incorrecto(login_page):
    login_page.ingresar_credenciales("usuario_inexistente", "1234")
    login_page.verificar_mensaje_error("Usuario o contraseña incorrectos.")

    
### TC-003 - Login con contraseña incorrecta
def test_login_contraseña_incorrecta(login_page):
    login_page.ingresar_credenciales("admin", "contraseña_incorrecta")
    login_page.verificar_mensaje_error("Usuario o contraseña incorrectos.")


### TC-004 - Login con campos vacíos
def test_login_campos_vacios(login_page):
    login_page.ingresar_credenciales("", "")

    login_page.verificar_campo_usuario_invalido()
    login_page.verificar_campo_password_invalido()
    expect(login_page.titulo_biblioteca).not_to_be_visible()


### TC-005 - Usuario vacío y contraseña válida
def test_login_usuario_vacio_contraseña_correcta(login_page):
    login_page.ingresar_credenciales("", "1234")

    login_page.verificar_campo_usuario_invalido()
    expect(login_page.titulo_biblioteca).not_to_be_visible()


### TC-006 - Usuario válido y contraseña vacía
def test_login_usuario_valido_contraseña_vacia(login_page):
    login_page.ingresar_credenciales("admin", "")

    login_page.verificar_campo_password_invalido()
    expect(login_page.titulo_biblioteca).not_to_be_visible()