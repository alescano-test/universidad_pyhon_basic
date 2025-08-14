print('\nSistema de envíos')

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

print('\nLos precios de los envíos son los siguientes')
print(f'Envío con destino Naional ${TARIFA_NACIONAL:.2f} por Kg.')
print(f'Envío con destino Naional ${TARIFA_INTERNACIONAL:.2f} por Kg.')

destino = input('Cual es el destino del envío (Nacional/Internaional): ').strip().lower()
peso = float(input('Ingresa el peso del paquete a enviar: '))
costo_total = None

if destino == 'nacional':
    costo_total = peso * TARIFA_NACIONAL
elif destino == 'internacional':
    costo_total = peso * TARIFA_INTERNACIONAL
else:
    print('Destino no válido. Ingresa el valor de nacional o internacional.')

if costo_total is not None:
    print(f'El costo de envío del paquete es: ${costo_total:.2f}')