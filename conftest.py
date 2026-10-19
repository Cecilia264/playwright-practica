import os
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.personas_page import PersonasPage
from pages.autores_page import AutoresPage
from pages.libros_pages import LibrosPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    # Ajusta el tamaño de pantalla estándar
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture
def page(context):
    page = context.new_page()
    page.set_default_timeout(10000)
    
    if os.environ.get("CI"):
        # Ejecución automática en GitHub Actions
        page.goto("http://localhost:8000/index.html")
    else:
        # Ejecución local en tu computadora
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        INDEX_PATH = os.path.join(BASE_DIR, "pagina", "index.html")
        page.goto(f"file://{INDEX_PATH}")
        
    return page


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def personas_page(page, login_page):
    login_page.ingresar_credenciales("admin", "1234")
    return PersonasPage(page)


@pytest.fixture
def autores_page(page, login_page):
    login_page.ingresar_credenciales("admin", "1234")
    autores = AutoresPage(page)
    autores.ir_a_autores()
    return autores


@pytest.fixture
def libros_page(page, login_page):
    login_page.ingresar_credenciales("admin", "1234")
    libros = LibrosPage(page)
    libros.ir_a_libros()
    return libros