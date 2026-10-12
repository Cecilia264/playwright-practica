import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


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
