from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # locators (elementos de la pantalla)
        self.usuario_input = page.locator("#usuario")
        self.password_input = page.locator("#password")
        self.btn_ingresar = page.get_by_role("button", name="Ingresar")
        self.mensaje_error = page.locator("#mensajeLogin")
        self.titulo_biblioteca = page.locator("#paginaBiblioteca")

    def ingresar_credenciales(self, usuario:str, password:str):
        self.usuario_input.fill(usuario)
        self.password_input.fill(password)
        self.btn_ingresar.click()

    # validaciones sencillas sobre la pantalla de login
    def verificar_mensaje_error(self, texto_esperado: str):
        expect(self.mensaje_error).to_have_text(texto_esperado)

    def verificar_campo_usuario_invalido(self):
        assert self.usuario_input.evaluate("(element) => !element.checkValidity()")

    def verificar_campo_password_invalido(self):
        assert self.password_input.evaluate("(element) => !element.checkValidity()")
