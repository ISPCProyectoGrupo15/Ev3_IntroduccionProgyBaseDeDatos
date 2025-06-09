
class Usuario:
    def __init__(self, username, email,first_name,last_name, role_id,cursor,conn):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role_id = role_id
        self.cursor = cursor
        self.conn = conn

    def mostrar_menu(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
    
class Administrador(Usuario):
    
    def mostrar_usuarios_registrados(self):
        self.cursor.execute("""
        SELECT u.user_id, u.username, u.email, r.nombre_rol
        FROM usuarios u
        JOIN rol r ON u.role_id_1 = r.role_id
        """)
        usuarios = self.cursor.fetchall()

        for usuario in usuarios:
            print(f"""
        ID: {usuario[0]}
        Usuario: {usuario[1]}
        Email: {usuario[2]}
        Rol: {usuario[3]}""")
    
    def cambiar_rol_usuario(self):
        
        user_id = input("Ingrese el ID del usuario al que desea cambiar el rol: ")
        self.cursor.execute("SELECT * FROM usuarios WHERE user_id = ?", (user_id,))
        usuario = self.cursor.fetchone()
        
        if usuario is None:
            print("El usuario no existe.")
            return
        
        nuevo_rol = int(input("Ingrese el nuevo rol (1 para Admin, 2 para Usuario Estándar): "))

        self.cursor.execute("UPDATE usuarios SET role_id_1 = ? WHERE user_id = ?", (nuevo_rol, user_id))
        self.conn.commit()
        print("Rol actualizado correctamente.")
        
    def eliminar_usuario(self):
        id_a_eliminar = int(input("Coloque el id del usuario que desea eliminar"))
        
        self.cursor.execute("SELECT 1 FROM usuarios WHERE user_id= ?", (id_a_eliminar,))
        registro = self.cursor.fetchone()
        
        if registro:
            self.cursor.execute("DELETE FROM usuarios WHERE user_id = ?", (id_a_eliminar,))
            self.conn.commit()
            
            print(f"Registro con id {id_a_eliminar} eliminado correctamente.")
        else:
            print(f"No se encontró ningún registro con ID {id_a_eliminar}.")


    def mostrar_menu(self):
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("""
            1 - Mostrar Usuarios Registrados
            2 - Cambiar Rol
            3 - Eliminar
            4 - Volver
            """) 
            try: 
                elegir_opcion = int(input("Elija una opcion: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue 

            if elegir_opcion == 1:
                
                self.mostrar_usuarios_registrados()
                input("Presioná Enter para volver al menú...")
            elif elegir_opcion == 2:
                
                self.cambiar_rol_usuario()
                input("Presiona Enter para volver al menu..")
            elif elegir_opcion == 3:
                self.eliminar_usuario()
                input("Presioná Enter para volver al menú...")
            elif elegir_opcion == 4:
                from main import menu  #  Importación local evita el error circular
                menu()
                break
            else: 
                print("Opción inválida. Intente nuevamente.")

class UsuarioEstandar(Usuario):
    
     def mostrar_menu(self): # Se asume que username, cursor, conn son pasados como argumentos
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("""
            1 - ver datos Personales
            2 - Salir """)
            
            try:
                elegir_opcion = int(input("Elija una opcion: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue

            if elegir_opcion == 1:
                
                self.cursor.execute("SELECT * FROM usuarios WHERE username = ?", (self.username,))
                usuario = self.cursor.fetchone()
                role_id = usuario[7]
                self.cursor.execute("SELECT nombre_rol FROM ROL WHERE role_id = ?", (role_id,))
                obtener_rol = self.cursor.fetchone()
                
                print(f"""--Datos Personales--
                      Nombre: {usuario[3]}
                      Apellido: {usuario[4]}
                      email: {usuario[5]}
                      fecha de nacimiento: {usuario[6]}
                      Rol:{obtener_rol[0]}""")
                
            elif elegir_opcion == 2:
                print(f"Hasta Luegooo ,volve pronto")
                self.cursor.close()
                self.conn.close()
                break
            else:
                print("Opcion invalida. Intente nuevamente")
