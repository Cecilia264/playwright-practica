from playwright.sync_api import expect

### TC-010 - Alta de autores exitosa
def test_alta_autor_exitosa(autores_page):
    autores_page.agregar_autor("Gabriel", "Garcia Marquez")
    autores_page.verificar_autor_en_tabla("Gabriel", "Garcia Marquez")
    

### TC-011 - Eliminar autor
def test_eliminar_autor(autores_page):
    autores_page.agregar_autor("Isabel", "Allende")
    autores_page.verificar_autor_en_tabla("Isabel", "Allende")

    autores_page.eliminar_autor("Isabel Allende")
    autores_page.verificar_autor_no_esta_en_tabla("Isabel Allende")


### TC-012 - Edición de autor exitosa
def test_editar_autor_exitoso(autores_page):
    autores_page.agregar_autor("Julio", "Cortazar")
    autores_page.verificar_autor_en_tabla("Julio", "Cortazar")

    # Editamos buscando por "Cortazar"
    autores_page.editar_autor("Cortazar", "Julio Florencio", "Cortázar")
    autores_page.verificar_autor_en_tabla("Julio Florencio", "Cortázar")