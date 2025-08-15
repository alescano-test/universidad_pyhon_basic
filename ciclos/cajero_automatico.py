print('\n~~~ Aplicacion de Cajero Automatico ~~~')
print('\nBivendenido a este cajero super basico! ')

salir = False
saldo = 0.00
DEPOSITO_EXTRACCION_MINIMO = 1

while not salir:
    print('''\nOperaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    #? El socio elige una opció
    opcion = float(input('\nEscoje una opción: '))
    if opcion == 1:
        print(f'\nTu saldo actual es de ${saldo:.2f}')
    #? Si elige retirar
    elif opcion == 2:
        saldo_retira = float(input('\nImporte a retirar $'))
        if saldo_retira <= 0:
            print(f'\nEl minimo a retirar es de ${DEPOSITO_EXTRACCION_MINIMO:.2f}')
        elif saldo_retira > saldo:
            print('\nTu saldo no es suficiente para realizar el retiro.')
        elif saldo_retira <= saldo:
            saldo -= saldo_retira
            print(f'Retiraste ${saldo_retira:.2f}')
            print(f'Saldo actual ${saldo:.2f}\n')
        else:
            print('Error!\n')
    #? Si elige depositar
    elif opcion == 3:
        saldo_ingresa = float(input('\nImporte a depositar $'))
        if saldo_ingresa > 0:
            saldo += saldo_ingresa
            print(f'\nDepositaste ${saldo_ingresa:.2f}')
            print(f'Saldo actual ${saldo:.2f}')
        else:
            print(f'\nEl importe minimo a depositar es de ${DEPOSITO_EXTRACCION_MINIMO:.2f}')
    elif opcion == 4:
        salir = True
    #? Si quiere salir
        print('\nCerrando sesión...')
    else:
    #? Si elige una opción diferente a las del menu
        print('\nElegiste una opción inválida. Reintenta.')
else:
    #? Mensaje de salida
    print('\nGracias por utilizar nuestro servicio. Vuelvas prontos!\n')