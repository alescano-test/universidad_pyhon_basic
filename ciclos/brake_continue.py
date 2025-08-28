print('\nPalabra break y continue')

print('\nBuscar el primer número par y finalizar el for.')
for i in range(1,10):
    if i % 2 == 0:
        print(f'Se encontro: {i} - Rompe al encontrar el primer número par.')
        break
    
print('\nSi se encuentra numero impar (no hacer nada y continuar con el siguiente ciclo).')
for i in range(1,10):
    if i % 2 == 1:
        continue
    print(f'{i}')