
numerp_filas = int(input('Ingresa el nro de filas que quieres que tenga tu triángulo: '))

for fila in range(1, numerp_filas +1):
    espacios_en_blanco = ' ' * (numerp_filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios_en_blanco}{asteriscos}')