from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import db, Usuario
from models import db, Paciente
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from functools import wraps
from flask import redirect, session, url_for
from flask import flash, redirect, request, render_template
import re



pymysql.install_as_MySQLdb()

app = Flask(__name__)


app.secret_key = 'clave_secreta_segura'  # Necesaria para sesiones
# Configuración para MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/clinica_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Conectar el `db` importado con la app
db.init_app(app)


# Rutas
@app.route('/')
def index():
    pacientes = Paciente.query.all()
    return render_template('index.html', pacientes=pacientes)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        edad = request.form['edad']
        genero = request.form['genero']
        nuevo = Paciente(nombre=nombre, cedula=cedula, edad=edad, genero=genero)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    paciente = Paciente.query.get_or_404(id)
    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.cedula = request.form['cedula']
        paciente.edad = request.form['edad']
        paciente.genero = request.form['genero']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', paciente=paciente)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for('index'))

# Login y Registro

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena_hash = generate_password_hash(request.form['contrasena_hash'])

        # Validar nombre
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]{3,}$', nombre):
            flash("Nombre inválido. Solo letras y espacios, mínimo 3 caracteres.")
            return redirect('/registro')



        # Validar correo único
        usuario_existente = Usuario.query.filter_by(correo=correo).first()
        if usuario_existente:
            flash("El correo ya está registrado.")
            return redirect('/registro')



        usuario = Usuario(nombre=nombre, correo=correo, contrasena_hash=contrasena_hash)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('registro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena_hash = request.form.get('contrasena_hash')
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and check_password_hash(usuario.contrasena_hash, contrasena_hash):
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            return redirect(url_for('index'))
        else:
            return 'Credenciales inválidas'

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/panel')
@login_required
def panel():
    return f"Bienvenido, {session['usuario_nombre']}!"


# Crear tablas
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
