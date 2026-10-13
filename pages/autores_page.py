from playwright.sync_api import Page, expect

class AutoresPage:
    def __init__(self, page: Page):
        self.page = page

        # pestaña/navegación a Autores
        self.link_autores = page.locator("a", has_text="Autores")

        # campos del formulario de Autores
        self.nombre_input = page.locator("#nombreAutor")
        self.apellido_input = page.locator("#apellidoAutor")

        # botón
        self.btn_agregar = page.locator("#btnAutor")

        # tabla
        self.tabla_autores = page.locator("#tablaAutores")


    def ir_a_autores(self):
        self.link_autores.click()

    
    def agregar_autor(self, nombre: str, apellido: str):
        self.nombre_input.fill(nombre)
        self.apellido_input.fill(apellido)
        self.btn_agregar.click()


    def verificar_autor_en_tabla(self, nombre: str, apellido: str):
        expect(self.tabla_autores).to_contain_text(nombre)
        expect(self.tabla_autores).to_contain_text(apellido)


    def eliminar_autor(self, texto_busqueda: str):
        self.page.once("dialog", lambda dialog: dialog.accept())
        fila = self.tabla_autores.locator("tr", has_text=texto_busqueda)
        fila.locator(".eliminar").click()


    def verificar_autor_no_esta_en_tabla(self, texto: str):
        expect(self.tabla_autores).not_to_contain_text(texto)


    def editar_autor(self, texto_busqueda: str, nuevo_nombre: str, nuevo_apellido: str):
        # buscar la fila del autor por nombre/apellido y hace click en editar
        fila = self.tabla_autores.locator("tr", has_text=texto_busqueda)
        fila.locator(".editar").click()

        # completa los nuevos datos y guarda
        self.nombre_input.fill(nuevo_nombre)
        self.apellido_input.fill(nuevo_apellido)
        self.btn_agregar.click()