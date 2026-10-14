from pages.autores_page import AutoresPage

### TC-013 - Alta de libro exitosa
def test_alta_libro_exitoso(page, libros_page):
    # 1. Precondicion: crear el autor necesario
    autores = AutoresPage(page)
    autores.ir_a_autores()
    autores.agregar_autor("Jorge Luis", "Borges")

    # 2. ir a Libros y registrar el libro
    libros_page.ir_a_libros()
    libros_page.agregar_libro("Ficciones", "Jorge Luis Borges", "5")

    # 3. validacion
    libros_page.verificar_libro_en_tabla("Ficciones", "Jorge Luis Borges", "5")


### TC-014 - Edición de libro exitosa
def test_editar_libro_exitoso(page, libros_page):
    autores = AutoresPage(page)
    autores.ir_a_autores()
    autores.agregar_autor("Julio", "Cortázar")

    libros_page.ir_a_libros()
    libros_page.agregar_libro("Rayuela", "Julio Cortázar", "3")

    # Editar el libro
    libros_page.editar_libro("Rayuela", "Rayuela (Edición Especial)", "Julio Cortázar", "10")
    libros_page.verificar_libro_en_tabla("Rayuela (Edición Especial)", "Julio Cortázar", "10")


### TC-015 - Eliminar libro
def test_eliminar_libro(page, libros_page):
    autores = AutoresPage(page)
    autores.ir_a_autores()
    autores.agregar_autor("Gabriel", "García Márquez")

    libros_page.ir_a_libros()
    libros_page.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", "2")

    libros_page.eliminar_libro("Cien Años de Soledad")
    libros_page.verificar_libro_no_esta_en_tabla("Cien Años de Soledad")

    