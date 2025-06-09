import re
from datetime import datetime

def validar_credenciales(username=None, password=None,first_name=None,last_name=None, email=None, fecha_nacimiento=None):
     errores = []
    # Expresión regular para Nombre de Usuario
    # (Ejemplo: alfanumérico, puntos, guiones, entre 4 y 20 caracteres, sin espacios)
     validacion_user = r"^[a-zA-Z0-9._-]{4,20}$"
    # Expresión regular para Contraseña Fuerte
    # (Ejemplo: min 8, max 64, al menos 1 minúscula, 1 mayúscula, 1 número, 1 carácter especial, sin espacios)
     validacion_contraseña = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])[^\s]{8,64}$"
     es_usuario_valido = re.fullmatch(validacion_user, username)
     es_contrasena_valida = re.fullmatch(validacion_contraseña, password)
     
     if not es_usuario_valido:
        errores.append("Error: El nombre de usuario no cumple los requisitos (4-20 caracteres, solo letras, números, puntos, guiones).")
    
     if not es_contrasena_valida:
        errores.append("Error: La contraseña no cumple los requisitos (8-64 caracteres, al menos 1 mayúscula, 1 minúscula, 1 número, 1 carácter especial).")
      
     if first_name is not None:
      if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñüÜ\s'-]{2,50}", first_name):
        errores.append("El nombre no es válido. Solo se permiten letras y espacios, entre 2 y 50 caracteres.")

     if last_name is not None:
      if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñüÜ\s'-]{2,50}", last_name):
        errores.append("El apellido no es válido. Solo se permiten letras y espacios, entre 2 y 50 caracteres.")
    
     if email is not None:
        if not re.fullmatch(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
         errores.append("El email no es válido.")
    
     if fecha_nacimiento is not None:
        try:
            fecha = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
            if fecha > datetime.now().date():
             errores.append("Error: La fecha de nacimiento no puede ser futura.")
        except ValueError:
         errores.append("La fecha de nacimiento debe tener el formato YYYY-MM-DD.")

     return errores