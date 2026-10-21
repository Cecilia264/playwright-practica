# 📚 Proyecto de QA Automation - Sistema de Gestión de Biblioteca

Este proyecto es una suite de pruebas automatizadas end-to-end (E2E) desarrollada para validar las funcionalidades de una aplicación web de gestión de biblioteca (SUT - *System Under Test*). 

El proyecto implementa las mejores prácticas de la industria, utilizando la arquitectura **Page Object Model (POM)** para garantizar un código mantenible y limpio, junto con un pipeline de **Integración Continua (CI/CD)** para ejecución automática.

---

## 🛠️ Tecnologías y Herramientas Utilizadas

- **Lenguaje de Programación:** Python 3.11+
- **Framework de Automatización:** Playwright
- **Test Runner & Assertions:** Pytest (`pytest-playwright`)
- **Patrón de Diseño:** Page Object Model (POM)
- **Integración Continua (CI/CD):** GitHub Actions
- **Control de Versiones:** Git & GitHub
- **Desarrollo Web (SUT):** HTML5, CSS3, JavaScript (LocalStorage)

---

## 🔄 Integración Continua (CI/CD)

El repositorio cuenta con una integración automática mediante **GitHub Actions** (`.github/workflows/playwright.yml`). 

Cada vez que se realiza un `push` o `pull request` a la rama principal (`main`), el pipeline de CI/CD:
1. Levanta un entorno Linux (`ubuntu-latest`) en la nube.
2. Instala Python, Playwright y sus navegadores headless.
3. Inicia un servidor web local HTTP para servir la aplicación.
4. Ejecuta la suite de 15 pruebas E2E de forma totalmente automatizada.

---

## 📁 Estructura del Proyecto

- **`.github/workflows/`**: Configuración del pipeline de CI/CD (`playwright.yml`).
- **`pages/`**: Implementación de Page Object Model (`login_page.py`, `personas_page.py`, `autores_page.py`, `libros_page.py`).
- **`tests/`**: Casos de prueba automatizados con Pytest (`test_login.py`, `test_personas.py`, `test_autores.py`, `test_libros.py`).
- **`pagina/`**: Código fuente del Sistema Bajo Prueba (`index.html`, `biblioteca.html`, `app.js`, `estilos.css`).
- **`docs/`**: Documentación técnica del proyecto (`casos-de-prueba.md`, `reporte-de-bugs.md`).
- **`conftest.py`**: Fixtures globales y soporte de navegación dual para entornos Local y CI/CD.

---

## 🧪 Casos de Prueba Cubiertos

Actualmente el proyecto cuenta con **15 casos de prueba automatizados** en verde (PASS):

### 🔑 Módulo de Login (`test_login.py`)
- **TC-001:** Login exitoso con credenciales válidas.
- **TC-002:** Rechazo de acceso con usuario inexistente.
- **TC-003:** Rechazo de acceso con contraseña incorrecta.
- **TC-004:** Validación de campos obligatorios cuando ambos están vacíos.
- **TC-005:** Validación de campo obligatorio con usuario vacío.
- **TC-006:** Validación de campo obligatorio con contraseña vacía.

### 👤 Módulo de Personas (`test_personas.py`)
- **TC-007:** Alta exitosa de una persona y verificación de presencia en la tabla.
- **TC-008:** Baja de una persona, manejo de alerta `confirm` de JavaScript y verificación de eliminación en la tabla.
- **TC-009:** Edición exitosa de datos de una persona en la tabla.

### ✍️ Módulo de Autores (`test_autores.py`)
- **TC-010:** Alta exitosa de un autor.
- **TC-011:** Baja de un autor con confirmación de alerta.
- **TC-012:** Edición exitosa de un autor existente.

### 📖 Módulo de Libros (`test_libros.py`)
- **TC-013:** Alta exitosa de un libro con selección de autor desde dropdown y cantidad.
- **TC-014:** Edición exitosa de datos de un libro en la tabla.
- **TC-015:** Baja de un libro registrado.

---

## 🚀 Cómo Ejecutar el Proyecto Localmente

- **Clonar el repositorio:** `git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git`
- **Entrar a la carpeta:** `cd TU_REPOSITORIO`
- **Crear entorno virtual:** `python -m venv venv`
- **Activar entorno virtual (PowerShell):** `.\venv\Scripts\Activate.ps1`
- **Instalar dependencias:** `pip install -r requirements.txt`
- **Instalar navegadores de Playwright:** `python -m playwright install`
- **Ejecutar las pruebas automatizadas:** `python -m pytest tests/ -v`

---

## 👩‍💻 Autora
- **Cecilia Cometto** - QA Automation Engineer / Tester