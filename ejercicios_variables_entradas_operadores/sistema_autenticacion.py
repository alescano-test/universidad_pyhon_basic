print("***Sistema de autenticación***")

USUARIO = "usuario"
PASSWORD = "password123"

usuario_ingresado = str(input("Ingresa tu usuario: "))
password_ingresada = str(input("Ingresa tu contraseña: "))

es_autentico = (USUARIO == usuario_ingresado.strip()) and (PASSWORD == password_ingresada.strip())

print(f"Ingreso permitido: {es_autentico}")