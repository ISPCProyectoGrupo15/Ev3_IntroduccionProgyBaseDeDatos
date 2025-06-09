import pyodbc
import bcrypt

server = 'Juan\\SQLEXPRESS'
database = 'login_register'

conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

def get_connection():
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print("Error al conectar:", e)
        raise
    
def crear_admin_por_defecto():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE role_id_1 = 1")
        existe_admin = cursor.fetchone()

        if not existe_admin:
            username = "admin"
            email = "admin@correo.com"
            first_name = "Admin"
            last_name = "Principal"
            password_plana = "admin123??"

            password_hash = bcrypt.hashpw(password_plana.encode('utf-8'), bcrypt.gensalt())
            rol = 1

            cursor.execute("""
                INSERT INTO usuarios (username, email, first_name, last_name, passwordHash, role_id_1)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (username, email, first_name, last_name, password_hash, rol))

            conn.commit()
            print("✔ Usuario administrador creado por defecto")
        else:
            print("✔ Ya existe un usuario administrador.")

    except Exception as e:
        print(f"Error al crear el admin por defecto: {e}")
        if conn:
            conn.rollback() # Si hay un error, deshacemos cambios
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()