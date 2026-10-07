from playwright.sync_api import sync_playwright


### TC-001 - Login con credenciales válidas
def test_login_credenciales_validas(page):
    page.locator("#usuario").fill("admin")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Ingresar").click()

    assert page.locator("#paginaBiblioteca").is_visible()

    
### TC-002 - Login con usuario incorrecto
def test_login_usuario_incorrecto(page):
    page.locator("#usuario").fill("usuario_inexistente")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Ingresar").click()

    assert page.get_by_text("Usuario o contraseña incorrectos.").is_visible()


### TC-003 - Login con contraseña incorrecta
def test_login_contraseña_incorrecta(page):
    page.locator("#usuario").fill("admin")
    page.locator("#password").fill("contraseña_incorrecta")
    page.get_by_role("button", name="Ingresar").click()

    assert page.get_by_text("Usuario o contraseña incorrectos.").is_visible()


### TC-004 - Login con campos vacíos
def test_login_campos_vacios(page):
    page.locator("#usuario").fill("")
    page.locator("#password").fill("")
    page.get_by_role("button", name="Ingresar").click()

    assert page.locator("#usuario").evaluate("(element) => !element.checkValidity()")


