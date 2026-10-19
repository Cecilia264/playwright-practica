import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.personas_page import PersonasPage
from pages.autores_page import AutoresPage
from pages.libros_pages import LibrosPage
import os


import os
import pytest

@pytest.fixture
def page(context):
    page = context.new_page()
    
    # Si estamos corriendo en GitHub Actions (CI)
    if os.environ.get("CI"):
        page.goto("http://localhost:8000/index.html")
    else:
        # Ejecución local en Windows
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        INDEX_PATH = os.path.join(BASE_DIR, "pagina", "index.html")
        page.goto(f"file://{INDEX_PATH}")
        
    return page


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("http://127.0.0.1:5500/pagina/index.html")

        yield page

        browser.close()


@pytest.fixture
def login_page(page):
    # le pasamos la pagina abierta a nuestra clase LoginPage
    return LoginPage(page)  # crea el objeto


@pytest.fixture
def personas_page(page, login_page):
    # inicia sesion primero para poder esta en la pantalla de la biblioteca
    login_page.ingresar_credenciales("admin", "1234") # aqui se inicia sesion atomaticamente
    return PersonasPage(page)


@pytest.fixture
def autores_page(page, login_page):
    login_page.ingresar_credenciales("admin", "1234")
    autores = AutoresPage(page)
    autores.ir_a_autores()  # inicia sesion y navega directo a la pestaña de Autores
    return autores


@pytest.fixture
def libros_page(page, login_page):
    login_page.ingresar_credenciales("admin", "1234")
    libros = LibrosPage(page)
    libros.ir_a_libros()
    return libros