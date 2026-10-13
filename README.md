# 📚 Proyecto de QA Automation - Sistema de Gestión de Biblioteca

Este proyecto es un entorno de pruebas automatizadas end-to-end (E2E) desarrollado para validar las funcionalidades de una aplicación web de gestión de biblioteca (SUT - *System Under Test*). 

El proyecto implementa las mejores prácticas de automatización en la industria, utilizando la arquitectura **Page Object Model (POM)** para garantizar un código mantenible, escalable y limpio.

---

## 🛠️ Tecnologías y Herramientas Utilizadas

* **Lenguaje de Programación:** Python 3.13+
* **Framework de Automatización:** Playwright
* **Test Runner & Assertions:** Pytest
* **Patrón de Diseño:** Page Object Model (POM)
* **Control de Versiones:** Git & GitHub
* **Desarrollo Web (SUT):** HTML5, CSS3, JavaScript (LocalStorage)

---

## 📁 Estructura del Proyecto

* **`pages/`**: Implementación de Page Object Model. Contiene los elementos y acciones por pantalla (`login_page.py`, `personas_page.py`).
* **`tests/`**: Casos de prueba automatizados con Pytest y configuración de fixtures globales en `conftest.py`.
* **`pagina/`**: Código fuente del Sistema Bajo Prueba (`index.html`, `biblioteca.html`, `app.js`, `estilos.css`).
* **`casos-de-prueba.md`**: Especificación de casos de prueba manuales y diseñados.
* **`reporte-de-bugs.md`**: Reporte de incidencias y hallazgos encontrados en la aplicación.

---

## 🧪 Casos de Prueba Cubiertos

Actualmente el proyecto cuenta con **8 casos de prueba automatizados** en verde (PASS):

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

---

## 🚀 Cómo Ejecutar el Proyecto Localmente

* **Clonar el repositorio:** `git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git`
* **Entrar a la carpeta:** `cd TU_REPOSITORIO`
* **Crear entorno virtual:** `python -m venv venv`
* **Activar entorno virtual (PowerShell):** `.\venv\Scripts\Activate.ps1`
* **Instalar dependencias:** `pip install -r requirements.txt`
* **Instalar navegadores de Playwright:** `playwright install`
* **Ejecutar las pruebas automatizadas:** `python -m pytest -v`

---

## 👩‍💻 Autora
* **Cecilia Cometto**