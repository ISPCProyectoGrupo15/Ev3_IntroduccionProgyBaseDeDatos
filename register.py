from database import get_connection
from validaciones import validar_credenciales
import bcrypt

conn = get_connection()
cursor = conn.cursor()

def usuario_o_email_existe(username, email):
    cursor.execute("SELECT * FROM usuarios WHERE username = ? OR email = ?", (username, email))
    resultado = cursor.fetchone()
    return resultado is not None

def registro_usuario():
    role_id_estandar = 2
    first_name = input("Ingrese su nombre: ")
    last_name = input("Ingrese su Apellido: ")
    email = input("Ingrese su email: ")
    username = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (formato: YYYY-MM-DD): ")
    
    errores = validar_credenciales(username, password, first_name, last_name, email, fecha_nacimiento)
    if errores:
        print("No se pudo registrar por los siguientes errores:")
        for error in errores:
            print("-", error)
        return 
    
    if usuario_o_email_existe(username,email):
        print("El nombre de usuario o email ya están registrados. Intente con otros.")
    else:
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        cursor.execute("""
        INSERT INTO usuarios (username, passwordHash, first_name, last_name, email, fecha_nacimiento, role_id_1)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",(username, password_hash, first_name, last_name, email, fecha_nacimiento, role_id_estandar))
        conn.commit()
        print("Usuario registrado correctamente.")