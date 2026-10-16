# 🐛 Reporte de Incidencias (Bugs) - Sistema de Gestión de Biblioteca

Este documento consolida las incidencias y comportamientos anómalos identificados durante las fases de testing exploratorio y automatización de pruebas sobre el Sistema Bajo Prueba (SUT).

---

## 📋 Lista de Incidencias Reportadas

### BUG-001: Permitir registro de persona con DNI duplicado
* **Severidad:** Alta
* **Prioridad:** Alta
* **Módulo:** Personas
* **Descripción:** El sistema permite registrar múltiples personas con el mismo número de DNI, violando la regla de negocio de unicidad de documento de identidad.
* **Pasos para reproducir:**
  1. Navegar al módulo de Personas.
  2. Completar los campos con Nombre: `Juan`, Apellido: `Pérez`, DNI: `12345678`.
  3. Hacer clic en "Agregar persona".
  4. Ingresar una nueva persona con Nombre: `María`, Apellido: `Gómez` y el mismo DNI: `12345678`.
  5. Hacer clic en "Agregar persona".
* **Comportamiento Esperado:** El sistema debe denegar el registro y mostrar un mensaje de error indicando que el DNI ya se encuentra registrado.
* **Comportamiento Observado:** La segunda persona se agrega exitosamente a la tabla con el DNI duplicado.

---

### BUG-002: Ausencia de mensajes de feedback/confirmación al realizar acciones de alta y edición
* **Severidad:** Baja
* **Prioridad:** Baja
* **Módulo:** General (Personas, Autores, Libros)
* **Descripción:** Al dar de alta o guardar la edición de un registro, la aplicación no presenta ningún tipo de mensaje visual (toast, alert o notificación) que confirme que la operación fue exitosa.
* **Pasos para reproducir:**
  1. Completar el formulario de alta en cualquiera de los módulos.
  2. Hacer clic en el botón de agregar/guardar.
* **Comportamiento Esperado:** Se debe mostrar un mensaje emergente o notificación confirmando la acción (ej: *"Persona agregada con éxito"*).
* **Comportamiento Observado:** Los datos se insertan directamente en la tabla sin ningún aviso o feedback visual hacia el usuario.

---

### BUG-003: Ausencia de validación de caracteres numéricos en campos de texto
* **Severidad:** Baja
* **Prioridad:** Baja
* **Módulo:** Personas / Autores
* **Descripción:** Los campos "Nombre" y "Apellido" aceptan números y caracteres especiales sin aplicar ningún tipo de restricción o sanitización.
* **Pasos para reproducir:**
  1. Ir al módulo de Personas o Autores.
  2. Ingresar `123456` en el campo Nombre y `#$%&` en Apellido.
  3. Guardar el registro.
* **Comportamiento Esperado:** El sistema debe validar que solo se ingresen caracteres alfabéticos.
* **Comportamiento Observado:** El registro se guarda y muestra caracteres no válidos en la tabla.