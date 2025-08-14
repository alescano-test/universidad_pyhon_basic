print('\n Estaciones del año en el que te encuentras')

mes = int(input('\nIngresa el número de mes del año en el que te encuentras (1 a 12): '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    print('Estación desconocida.')

print(f'La estación para el mes proporcionado {mes} es {estacion}.')