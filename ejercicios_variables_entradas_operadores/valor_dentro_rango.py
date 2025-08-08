VALOR_MINIMO = 0
VALOR_MAXIMO = 10

valor_ingresado = int(input(f"Ingresa un número dentro del rango {VALOR_MINIMO} y {VALOR_MAXIMO}: "))

es_valido = (valor_ingresado >= VALOR_MINIMO and valor_ingresado <= VALOR_MAXIMO)

print(f"El valor ingresado esta dentro del rango?: {es_valido}")