from database import get_connection
import bcrypt
from validaciones import validar_credenciales
from usuario import Administrador, UsuarioEstandar

try:
    conn = get_connection()
    cursor = conn.cursor()
except Exception as e:
    print("Error al obtener los datos:", e)


def login_user():
        
    username = input("Escriba el nombre de usuario")
    password = input("Escriba el nombre de contraseña")
    validar_credenciales(username,password)
    cursor.execute("SELECT passwordHash,role_id_1,email,first_name,last_name FROM usuarios WHERE username = ?", (username,))
    resultado = cursor.fetchone()
    hashed_password_from_db = resultado[0]
    if resultado is None:
        print("Usuario no encontrado.")
    elif bcrypt.checkpw(password.encode(), hashed_password_from_db.encode()):
        role_id = resultado[1]
        email = resultado[2]
        first_name = resultado[3]
        last_name = resultado[4]
        if role_id == 1:
            usuario = Administrador(username, email, first_name, last_name, role_id, cursor,conn)
        else:
            usuario = UsuarioEstandar(username, email, first_name, last_name, role_id, cursor,conn)

        usuario.mostrar_menu()
        
    else:
        print("Contraseña incorrecta.")