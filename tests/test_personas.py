from playwright.sync_api import expect

### TC-007 - Alta de persona exitosa
def  test_alta_persona_exitosa(personas_page):
    personas_page.agregar_persona("Cecilia", "Cometto", "43770588")
    personas_page.verificar_persona_en_tabla("Cecilia", "Cometto", "43770588")


def test_eliminar_persona(personas_page):
    # 1. agregamos una persona primero
    personas_page.agregar_persona("Juan", "Cometto", "12345678")
    personas_page.verificar_persona_en_tabla("Juan", "Cometto", "12345678")

    # 2. la eliminamos y verificamos que la tabla este vacía
    personas_page.eliminar_persona()
    personas_page.verificar_persona_no_esta_en_tabla("12345678")