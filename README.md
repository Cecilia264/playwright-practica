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

* **`pages/`**: Implementación de Page Object Model. Contiene los elementos y acciones por pantalla (`login_page.py`, `personas_page.py`, `autores_page.py`, `libros_page.py`).
* **`tests/`**: Casos de prueba automatizados con Pytest y configuración de fixtures globales en `conftest.py`.
* **`pagina/`**: Código fuente del Sistema Bajo Prueba (`index.html`, `biblioteca.html`, `app.js`, `estilos.css`).
* **`docs/`**: Documentación técnica del proyecto (`casos-de-prueba.md`, `reporte-de-bugs.md`).

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