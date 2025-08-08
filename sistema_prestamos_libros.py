# 1. Si el usuario tiene credencial de estudiante
# 2. El usuario vive a no más de 3km a la redonda.

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial_estudiante = str(input("Cuentas con credencial de estudiante (Si/No)? "))
distancia_biblioteca_km = int(input("A cuantos KM vives de la biblioteca? "))
es_elegible_prestamo = tiene_credencial_estudiante.strip().lower() == "si" or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM

print(f"Eres elegible para préstamo de libro: {es_elegible_prestamo}")