// ======================================================
// LOGIN
// ======================================================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const usuario = document.getElementById("usuario").value;
        const password = document.getElementById("password").value;

        // Usuario y contraseña de prueba
        if (usuario === "admin" && password === "1234") {

            localStorage.setItem("sesion", "activa");

            window.location.href = "biblioteca.html";

        } else {

            document.getElementById("mensajeLogin").textContent =
                "Usuario o contraseña incorrectos.";
        }

    });

}


// ======================================================
// VERIFICAR SESIÓN
// ======================================================

if (window.location.pathname.includes("biblioteca.html")) {

    if (localStorage.getItem("sesion") !== "activa") {

        window.location.href = "index.html";

    }

}


// ======================================================
// CERRAR SESIÓN
// ======================================================

function cerrarSesion() {

    localStorage.removeItem("sesion");

    window.location.href = "index.html";
}


// ======================================================
// MOSTRAR SECCIONES
// ======================================================

function mostrarSeccion(nombre) {

    const secciones = document.querySelectorAll(".seccion");

    secciones.forEach(function(seccion) {
        seccion.classList.remove("activa");
    });

    document.getElementById(nombre).classList.add("activa");

    // Si entramos a libros, actualizamos los autores
    if (nombre === "libros") {
        cargarAutoresEnSelect();
    }
}


// Mostrar Personas al entrar
if (document.getElementById("personas")) {

    mostrarSeccion("personas");

}


// ======================================================
// PERSONAS
// ======================================================

let personas = JSON.parse(localStorage.getItem("personas")) || [];

let personaEditando = null;


const personaForm = document.getElementById("personaForm");

if (personaForm) {

    personaForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const nombre = document.getElementById("nombrePersona").value;
        const apellido = document.getElementById("apellidoPersona").value;
        const dni = document.getElementById("dniPersona").value;

        if (personaEditando === null) {

            // ALTA
            const nuevaPersona = {
                id: Date.now(),
                nombre: nombre,
                apellido: apellido,
                dni: dni
            };

            personas.push(nuevaPersona);

        } else {

            // MODIFICACIÓN
            const persona = personas.find(
                p => p.id === personaEditando
            );

            persona.nombre = nombre;
            persona.apellido = apellido;
            persona.dni = dni;

            personaEditando = null;

            document.getElementById("btnPersona").textContent =
                "Agregar persona";

            document.getElementById("cancelarPersona").style.display =
                "none";
        }

        guardarPersonas();

        personaForm.reset();

        mostrarPersonas();

    });

}


function guardarPersonas() {

    localStorage.setItem(
        "personas",
        JSON.stringify(personas)
    );

}


function mostrarPersonas() {

    const tabla = document.getElementById("tablaPersonas");

    if (!tabla) return;

    tabla.innerHTML = "";

    personas.forEach(function(persona) {

        const fila = document.createElement("tr");

        fila.innerHTML = `
            <td>${persona.nombre}</td>
            <td>${persona.apellido}</td>
            <td>${persona.dni}</td>

            <td>
                <button class="editar"
                        onclick="editarPersona(${persona.id})">
                    Editar
                </button>

                <button class="eliminar"
                        onclick="eliminarPersona(${persona.id})">
                    Eliminar
                </button>
            </td>
        `;

        tabla.appendChild(fila);

    });

}


function editarPersona(id) {

    const persona = personas.find(
        p => p.id === id
    );

    document.getElementById("nombrePersona").value =
        persona.nombre;

    document.getElementById("apellidoPersona").value =
        persona.apellido;

    document.getElementById("dniPersona").value =
        persona.dni;

    personaEditando = id;

    document.getElementById("btnPersona").textContent =
        "Guardar cambios";

    document.getElementById("cancelarPersona").style.display =
        "block";
}


function eliminarPersona(id) {

    if (confirm("¿Querés eliminar esta persona?")) {

        personas = personas.filter(
            p => p.id !== id
        );

        guardarPersonas();

        mostrarPersonas();
    }

}


function cancelarEdicionPersona() {

    personaEditando = null;

    document.getElementById("personaForm").reset();

    document.getElementById("btnPersona").textContent =
        "Agregar persona";

    document.getElementById("cancelarPersona").style.display =
        "none";
}


mostrarPersonas();


// ======================================================
// AUTORES
// ======================================================

let autores = JSON.parse(localStorage.getItem("autores")) || [];

let autorEditando = null;


const autorForm = document.getElementById("autorForm");

if (autorForm) {

    autorForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const nombre = document.getElementById("nombreAutor").value;
        const apellido = document.getElementById("apellidoAutor").value;

        if (autorEditando === null) {

            // ALTA
            const nuevoAutor = {
                id: Date.now(),
                nombre: nombre,
                apellido: apellido
            };

            autores.push(nuevoAutor);

        } else {

            // MODIFICACIÓN
            const autor = autores.find(
                a => a.id === autorEditando
            );

            autor.nombre = nombre;
            autor.apellido = apellido;

            autorEditando = null;

            document.getElementById("btnAutor").textContent =
                "Agregar autor";

            document.getElementById("cancelarAutor").style.display =
                "none";
        }

        guardarAutores();

        autorForm.reset();

        mostrarAutores();

        cargarAutoresEnSelect();

    });

}


function guardarAutores() {

    localStorage.setItem(
        "autores",
        JSON.stringify(autores)
    );

}


function mostrarAutores() {

    const tabla = document.getElementById("tablaAutores");

    if (!tabla) return;

    tabla.innerHTML = "";

    autores.forEach(function(autor) {

        const fila = document.createElement("tr");

        fila.innerHTML = `
            <td>${autor.nombre}</td>
            <td>${autor.apellido}</td>

            <td>
                <button class="editar"
                        onclick="editarAutor(${autor.id})">
                    Editar
                </button>

                <button class="eliminar"
                        onclick="eliminarAutor(${autor.id})">
                    Eliminar
                </button>
            </td>
        `;

        tabla.appendChild(fila);

    });

}


function editarAutor(id) {

    const autor = autores.find(
        a => a.id === id
    );

    document.getElementById("nombreAutor").value =
        autor.nombre;

    document.getElementById("apellidoAutor").value =
        autor.apellido;

    autorEditando = id;

    document.getElementById("btnAutor").textContent =
        "Guardar cambios";

    document.getElementById("cancelarAutor").style.display =
        "block";
}


function eliminarAutor(id) {

    if (confirm("¿Querés eliminar este autor?")) {

        autores = autores.filter(
            a => a.id !== id
        );

        guardarAutores();

        mostrarAutores();

        cargarAutoresEnSelect();
    }

}


function cancelarEdicionAutor() {

    autorEditando = null;

    document.getElementById("autorForm").reset();

    document.getElementById("btnAutor").textContent =
        "Agregar autor";

    document.getElementById("cancelarAutor").style.display =
        "none";
}


mostrarAutores();


// ======================================================
// LIBROS
// ======================================================

let libros = JSON.parse(localStorage.getItem("libros")) || [];

let libroEditando = null;


const libroForm = document.getElementById("libroForm");

if (libroForm) {

    libroForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const titulo = document.getElementById("tituloLibro").value;
        const autorId = Number(
            document.getElementById("autorLibro").value
        );
        const cantidad = Number(
            document.getElementById("cantidadLibro").value
        );

        if (libroEditando === null) {

            // ALTA
            const nuevoLibro = {
                id: Date.now(),
                titulo: titulo,
                autorId: autorId,
                cantidad: cantidad
            };

            libros.push(nuevoLibro);

        } else {

            // MODIFICACIÓN
            const libro = libros.find(
                l => l.id === libroEditando
            );

            libro.titulo = titulo;
            libro.autorId = autorId;
            libro.cantidad = cantidad;

            libroEditando = null;

            document.getElementById("btnLibro").textContent =
                "Agregar libro";

            document.getElementById("cancelarLibro").style.display =
                "none";
        }

        guardarLibros();

        libroForm.reset();

        mostrarLibros();

    });

}


function guardarLibros() {

    localStorage.setItem(
        "libros",
        JSON.stringify(libros)
    );

}


function cargarAutoresEnSelect() {

    const select = document.getElementById("autorLibro");

    if (!select) return;

    select.innerHTML =
        '<option value="">Seleccionar autor</option>';

    autores.forEach(function(autor) {

        const option = document.createElement("option");

        option.value = autor.id;

        option.textContent =
            autor.nombre + " " + autor.apellido;

        select.appendChild(option);

    });

}


function mostrarLibros() {

    const tabla = document.getElementById("tablaLibros");

    if (!tabla) return;

    tabla.innerHTML = "";

    libros.forEach(function(libro) {

        const autor = autores.find(
            a => a.id === libro.autorId
        );

        let nombreAutor = "Sin autor";

        if (autor) {
            nombreAutor =
                autor.nombre + " " + autor.apellido;
        }

        const fila = document.createElement("tr");

        fila.innerHTML = `
            <td>${libro.titulo}</td>
            <td>${nombreAutor}</td>
            <td>${libro.cantidad}</td>

            <td>
                <button class="editar"
                        onclick="editarLibro(${libro.id})">
                    Editar
                </button>

                <button class="eliminar"
                        onclick="eliminarLibro(${libro.id})">
                    Eliminar
                </button>
            </td>
        `;

        tabla.appendChild(fila);

    });

}


function editarLibro(id) {

    const libro = libros.find(
        l => l.id === id
    );

    cargarAutoresEnSelect();

    document.getElementById("tituloLibro").value =
        libro.titulo;

    document.getElementById("autorLibro").value =
        libro.autorId;

    document.getElementById("cantidadLibro").value =
        libro.cantidad;

    libroEditando = id;

    document.getElementById("btnLibro").textContent =
        "Guardar cambios";

    document.getElementById("cancelarLibro").style.display =
        "block";
}


function eliminarLibro(id) {

    if (confirm("¿Querés eliminar este libro?")) {

        libros = libros.filter(
            l => l.id !== id
        );

        guardarLibros();

        mostrarLibros();
    }

}


function cancelarEdicionLibro() {

    libroEditando = null;

    document.getElementById("libroForm").reset();

    document.getElementById("btnLibro").textContent =
        "Agregar libro";

    document.getElementById("cancelarLibro").style.display =
        "none";
}


cargarAutoresEnSelect();

mostrarLibros();