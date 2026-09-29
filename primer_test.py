# Abrir index.html
# Comprobar el título
# Hacer login y hacer clic en el botón
# Comprobar que cambió la URL a biblioteca.html
# Comprobar que aparece el texto "Biblioteca"
# Volver atrás
# Comprobar nuevamente que estamos en index.html


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    # Abrir index.html
    page.goto("http://127.0.0.1:5500/pagina/index.html")
    page.wait_for_timeout(500)

    # Comprobar el título
    print(page.title())

    # Hacer login y hacer clic en el botón
    page.locator("#usuario").fill("admin")
    page.locator("#password").fill("1234")
    page.locator("#boton").click()
    page.wait_for_timeout(500)

    # Comprobar que cambió la URL a biblioteca.html
    assert page.url == "http://127.0.0.1:5500/pagina/biblioteca.html"

    # Comprobar que aparece el texto "Biblioteca"                                CON ID
    print(page.locator("#paginaBiblioteca").inner_text())

    # Comprobar que aparece el boton para ir a la seccion de "Cerrar sesión"     CON get_by_role
    assert page.get_by_role("button", name="Cerrar sesión")
    print(page.get_by_role("button", name="Cerrar sesión").inner_text())
    #o sino para que responda True -> print(page.get_by_role("button", name="Cerrar sesión").is_visible())
    assert page.get_by_role("link", name="Personas")  #link es para las etiquetas a

    # Comprobar que aparece el boton de Libros                                  CON get_by_text
    print(page.get_by_text("Libros").first.inner_text())
    assert page.get_by_text("Libros").first.is_visible()

    # Comprobar que aparece el boton de Autores                                 CON get_by_lebel

    # Comprobar que aparezca "ABM de Personas"                                  CON get_by_placeholder
    assert page.get_by_placeholder("Ingrese el nombre").is_visible()
    print(page.get_by_placeholder("Ingrese el nombre").is_visible())

    # Ir a la seccion de ABM de libros
    page.get_by_role("link", name="Libros").click()
    assert page.get_by_text("ABM de Libros").is_visible()

    # Volver atrás hasta la index.html
    page.go_back()
    page.go_back()

    page.wait_for_timeout(500)

    # Comprobar nuevamente que estamos en index.html
    assert page.url == "http://127.0.0.1:5500/pagina/index.html"

    browser.close()



"""with abre un bloque donde p representa la instancia principal de Playwright.
La idea es: “iniciá esto, ejecutá todo lo que está adentro y, cuando termine, encargate de cerrarlo”.
Se utiliza principalmente para no olvidarnos de cerrar los recursos.
No se usa with simplemente para agrupar código, sino para controlar automáticamente el inicio y cierre de Playwright."""

"""Inicia una instancia de Chromium (el motor detrás de Google Chrome y Microsoft Edge). 
        headless=False indica que quieres ver la interfaz gráfica"""

"""que es context: context es básicamente una sesión nueva y aislada del navegador."""

"""# es para referenciar por id"""

#------------------------------------------------------------------------------------------------------------

"""locator
page.locator("#usuario") -> Eso busca el elemento que tenga -> id="usuario

get_by_role()
Busca un elemento por su función/rol.

Por ejemplo, tu botón: <button id="boton">Ingresar</button>
En vez de: page.locator("#boton").click()
podés hacer: page.get_by_role("button", name="Ingresar").click()
Le estás diciendo: Buscá un elemento que sea un button y cuyo nombre sea "Ingresar".

get_by_text()
Busca por el texto que aparece en la página.
Por ejemplo: <h1 id="paginaBiblioteca">Biblioteca</h1>
Podés hacer: page.get_by_text("Biblioteca")
Y para comprobarlo: print(page.get_by_text("Biblioteca").inner_text()) o page.get_by_text("Biblioteca").is_visible()

get_by_label()
Busca un campo utilizando el texto de su <label>.
Si tenés:  <label for="usuario">Usuario</label>
           <input id="usuario">
podés hacer: page.get_by_label("Usuario").fill("admin")
Esto es muy útil porque no necesitás conocer el ID.

get_by_placeholder()
Busca un campo por el texto que aparece como ejemplo dentro del input.
Por ejemplo, si tu HTML tuviera: <input placeholder="Ingrese su usuario">
podrías hacer: page.get_by_placeholder("Ingrese su usuario").fill("admin")
En tu página actual probablemente no tenés placeholders, así que podés agregar uno para practicar.

"""
