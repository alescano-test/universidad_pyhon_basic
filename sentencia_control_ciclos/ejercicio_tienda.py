print('*** Sistema de descuento ***')

monto_compra = float(input('Cual fue el monto de tu compra? '))
es_miembro = str(input('Eres miembro de la tienda (Si/No)? ')).lower()
DESCUENTO_10 = monto_compra * 0.10
DESCUENTO_5 = monto_compra * 0.05

if monto_compra >= 1000 and es_miembro == 'si':
    print('Felicidades, has obtenido un desuento del 10%')
    print(f'Monto de la compra: ${monto_compra}')
    print(f'Monto de descuento: ${DESCUENTO_10}')
    print(f'Monto final de la compra: ${monto_compra - DESCUENTO_10}')
elif monto_compra < 1000 and es_miembro == 'si':
    print('Felicidades, has obtenido un desuento del 5%')
    print(f'Monto de la compra: ${monto_compra}')
    print(f'Monto de descuento: ${DESCUENTO_5}')
    print(f'Monto final de la compra: ${monto_compra - DESCUENTO_5}') 
else:
    print('No obtuviste ningún tipo de descuento\n100Te invitamos a hacerte mienbro de la tienda.')
    print(f'Monto final de la compra: ${monto_compra}')
    
    