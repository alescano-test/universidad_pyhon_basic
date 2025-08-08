cadena = "Cadena de, ejemplo"
print(f"Cadena original: {cadena}")

# String en mayúsculas y minúsculas
print(f"Cadena en mayúscula: {cadena.upper()}")
print(f"Cadena en minúscula: {cadena.lower()}")

# Limpiar espacios al inicio y al final
cadena_con_espacioes = "   Espacios al inicio y al final   "
print(f"{cadena_con_espacioes.strip()}")

# Largo de una cadena
print(f"Largo de la cadena: {len(cadena)}")

# Substring [inicio:fin (sin incluir fin)]
print(f"Subcadena (del índice 0 al 5): {cadena[0:6]}")

# Substring find()
print(f"Índice de la subcadena 'ejemplo': {cadena.find('ejemplo')}")

#Remplazar una subcadena
print(f"Cadena después de reemplazar 'ejemplo' por 'prueba': {cadena.replace('ejemplo', 'prueba')}")

#Separar subcadenas
print(f"Cadena separada por espacios: {cadena.split(',')}")