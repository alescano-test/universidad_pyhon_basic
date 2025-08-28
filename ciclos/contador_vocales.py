print('Contador de vocales')

palabra = 'Palabra con muchas vocales'
vocales = 'aeiouAEIOU'
cantidad_vocales = 0

for letra in palabra:
    if letra in vocales:
        cantidad_vocales += 1
        print(f'Se encontro la vocal {letra}.')

print(f'\nCantidad de vocales encontradas {cantidad_vocales}\n')