from playwright.sync_api import Page, expect

class LibrosPage:
    def __init__(self, page: Page):
        self.page = page

        # pestaña/navegacion a Libros
        self.link_libros = page.locator("a", has_text="Libros")

        # campos del formulario de Libros
        self.titulo_input = page.locator("#tituloLibro")
        self.select_autor = page.locator("#autorLibro")  # Dropdown de autores
        self.cantidad_input = page.locator("#cantidadLibro")

        # botón
        self.btn_agregar = page.locator("#btnLibro")

        # tabla
        self.tabla_libros = page.locator("#tablaLibros")


    def ir_a_libros(self):
        self.link_libros.click()


    def agregar_libro(self, titulo: str, autor_texto: str, cantidad: str):
        self.titulo_input.fill(titulo)
        self.select_autor.select_option(label=autor_texto)
        self.cantidad_input.fill(str(cantidad))
        self.btn_agregar.click()


    def verificar_libro_en_tabla(self, titulo: str, autor: str, cantidad: str):
        expect(self.tabla_libros).to_contain_text(titulo)
        expect(self.tabla_libros).to_contain_text(autor)
        expect(self.tabla_libros).to_contain_text(str(cantidad))


    def editar_libro(self, texto_busqueda: str, nuevo_titulo: str, nuevo_autor_texto: str, nueva_cantidad: str):
        fila = self.tabla_libros.locator("tr", has_text=texto_busqueda)
        fila.locator(".editar").click()

        self.titulo_input.fill(nuevo_titulo)
        self.select_autor.select_option(label=nuevo_autor_texto)
        self.cantidad_input.fill(str(nueva_cantidad))
        self.btn_agregar.click()


    def eliminar_libro(self, texto_busqueda: str):
        self.page.once("dialog", lambda dialog: dialog.accept())
        fila = self.tabla_libros.locator("tr", has_text=texto_busqueda)
        fila.locator(".eliminar").click()


    def verificar_libro_no_esta_en_tabla(self, texto: str):
        expect(self.tabla_libros).not_to_contain_text(texto)