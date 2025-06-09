from login import login_user
from register import registro_usuario
from database import crear_admin_por_defecto

crear_admin_por_defecto()

def menu():
    while True:
     print("\n=== MENÚ PRINCIPAL ===")
     print("""
          1 - Iniciar sesión
          2 - Registrarse
          3 - Salir """)
     try:
        elegir_opcion = int(input("Elija una opcion: "))
     except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        continue

     if(elegir_opcion == 1):
       login_user()
     elif(elegir_opcion == 2):
       registro_usuario()
     elif(elegir_opcion == 3):
       print("Hasta Luego")
       break
     else:
      print("Opcion invalida. Intente nuevamente")
      
def main():
    menu()

if __name__ == "__main__":
    main()


