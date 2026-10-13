from playwright.sync_api import Page, expect

class PersonasPage:
    def __init__(self, page: Page):
        self.page = page

        # campos del formulario
        self.nombre_input = page.locator("#nombrePersona")
        self.apellido_input = page.locator("#apellidoPersona")
        self.dni_input = page.locator("#dniPersona")

        # botones
        self.btn_agregar = page.locator("#btnPersona")
        self.btn_cancelar = page.locator("cancelarPersona")

        # tabla
        self.tabla_personas = page.locator("#tablaPersonas")


    def agregar_persona(self, nombre: str, apellido: str, dni: str):
        self.nombre_input.fill(nombre)
        self.apellido_input.fill(apellido)
        self.dni_input.fill(dni)
        self.btn_agregar.click()


    def verificar_persona_en_tabla(self, nombre: str, apellido: str, dni: str):
        # verifica que la fila con los datos ingresados sea visible en la tabla
        expect(self.tabla_personas).to_contain_text(nombre)
        expect(self.tabla_personas).to_contain_text(apellido)
        expect(self.tabla_personas).to_contain_text(dni)


    def eliminar_persona(self):
        # escuchar la alerta/popup de confirmacion de JS y aceptarla automaticamente
        self.page.once("dialog", lambda dialog: dialog.accept())

        # hacer click en el primer botón "Eliminar" de la tabla
        self.tabla_personas.locator(".eliminar").first.click()


    def verificar_persona_no_esta_en_tabla(self, texto: str):
        # verifica que un nombre, apellido o dni, ya no aparezca en la tabla
        expect(self.tabla_personas).not_to_contain_text(texto)
