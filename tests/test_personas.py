from playwright.sync_api import expect

### TC-007 - Alta de persona exitosa
def  test_alta_persona_exitosa(personas_page):
    personas_page.agregar_persona("Cecilia", "Cometto", "43770588")
    personas_page.verificar_persona_en_tabla("Cecilia", "Cometto", "43770588")


### TC-008 - Eliminar persona
def test_eliminar_persona(personas_page):
    # 1. agregamos una persona primero
    personas_page.agregar_persona("Juan", "Cometto", "12345678")
    personas_page.verificar_persona_en_tabla("Juan", "Cometto", "12345678")

    # 2. eliminamos especificamente a un persona pasandole su DNI
    personas_page.eliminar_persona("12345678")
    personas_page.verificar_persona_no_esta_en_tabla("Juan")


### TC-009 - Edición de personas exitosa
def test_editar_persona_exitosa(personas_page):
    personas_page.agregar_persona("Julieta", "Garcia", "98765432")
    personas_page.verificar_persona_en_tabla("Julieta", "Garcia", "98765432")

    # editamos especificamente a la persona con DNI 98765432
    personas_page.editar_persona("98765432", "Julieta Victoria", "Garcia", "98765432")

    # verificamos los nuevos datos en la tabla
    personas_page.verificar_persona_en_tabla("Julieta Victoria", "Garcia", "98765432")