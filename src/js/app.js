    document.getElementById("registroForm").addEventListener("submit", function (e) {
      const nombre = document.querySelector('input[name="nombre"]').value.trim();
      const correo = document.querySelector('input[name="correo"]').value.trim();
      const contrasena = document.querySelector('input[name="contrasena_hash"]').value.trim();

      // Validar nombre (solo letras y espacios)
      const nombreValido = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(nombre);
      if (!nombreValido || nombre.length < 3) {
        alert("El nombre debe contener solo letras y al menos 3 caracteres.");
        e.preventDefault();
        return;
      }

      // Validar correo
      const correoValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo);
      if (!correoValido) {
        alert("Correo electrónico inválido.");
        e.preventDefault();
        return;
      }

      // Validar contraseña
      if (contrasena.length < 6) {
        alert("La contraseña debe tener al menos 6 caracteres.");
        e.preventDefault();
        return;
      }

      // Acá podrías agregar lógica con fetch() para verificar que el correo no exista
      // por ejemplo con un endpoint como /verificar-correo?correo=...

    });