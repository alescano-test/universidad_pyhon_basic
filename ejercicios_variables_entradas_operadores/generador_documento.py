# Sistema generador ID Único
from random import randint
#Con los datos recibidos el sistema deberá realizar lo siguiente

# 1. Del valor recibido de nombre y apellido usar solo las 2 primeras letas de cada una y ponerlas en mayúscula.
# 2. Del valor recibido de año de nacimiento usar solo los 2 últimos números.
# 3. Se deberá generar un valor aleatorio de 4 digitos con ayuda de la función randint
# 4. Concatenar todos los datos obtenidos ejemplo:
# JUAN PEREZ 1995 = JUPE19955902

nombre = str(input("Ingresa tu nombre:"))
apellido = str(input("Ingresa tu apellido:"))
fecha_nac = str(input("Ingresa tu fecha de nacimiento (YYYY):"))

nombre_final = nombre[:2].upper()
apellido_final = apellido[:2].upper()
fecha_nac_final = fecha_nac[-2:]
cod_rand = str(randint(1000,9999))
ID = nombre_final+apellido_final+fecha_nac_final+cod_rand

print(f"Hola {nombre}\n Tu nuevo número de identificación (ID) generado por el sistema es:\n {ID}")
