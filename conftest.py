import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.personas_page import PersonasPage


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