# 🏥 MedReserve – Sistema de Gestión de Citas Médicas

Proyecto universitario para el curso **Tecnologías de Backend** – Universidad Latina de Costa Rica.  
Desarrollado con **Flask (Python)**, **MySQL**, y frontend HTML/CSS.  

---

## 📋 Descripción

**MedReserve** es una aplicación web diseñada para gestionar pacientes y sus citas médicas. Incluye funcionalidades de autenticación, control de roles (administrador y usuario), operaciones CRUD y conexión a base de datos relacional.

---

## 🚀 Tecnologías utilizadas

- **Backend:** Flask (Python)
- **Base de Datos:** MySQL
- **Frontend:** HTML5, CSS3 (Bootstrap opcional)
- **ORM inicial:** SQLAlchemy (migrado a MySQL con `mysql-connector-python`)
- **Control de sesiones:** Flask Session

---

## 🧩 Funcionalidades principales

- Registro e inicio de sesión de usuarios
- Validación de credenciales con hash seguro
- CRUD completo de pacientes
- Control de acceso según rol de usuario
- Protección de rutas con decoradores (`@login_required`)
- Comunicación frontend-backend
- Migración de SQLAlchemy a consultas MySQL nativas

---

## ⚙️ Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/medreserve.git
cd medreserve
```

2. Instala los requerimientos:

```bash
pip install -r requirements.txt
```

3. Configura la base de datos (MySQL Workbench):

```sql
CREATE DATABASE medreserve_db;
```

4. Modifica tu archivo `config.py` o `app.py` con tus credenciales de base de datos.

5. Ejecuta la aplicación:

```bash
python app.py
```

Accede desde `http://localhost:5000`.

---

## 🔐 Control de roles

- `admin`: Acceso completo al sistema.
- `usuario`: Solo visualización de sus propios datos.

---

## 👨‍💻 Autores

- Melvin Josue Alfaro Porras  
- Profesor: Mario Vargas Montes

---

## 📁 Estructura del proyecto

```
📦medreserve
 ┣ 📂templates
 ┣ 📂static
 ┣ 📄app.py
 ┣ 📄db_config.py
 ┣ 📄requirements.txt
 ┗ 📄README.md
```

---

## 📸 Capturas de pantalla

> Agrega aquí imágenes del sistema en funcionamiento o la URL del despliegue (si aplica).

---

## 📜 Licencia

Proyecto de uso educativo – Universidad Latina.