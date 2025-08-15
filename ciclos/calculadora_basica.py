print('\n~~~ Calculadora ~~~')

salir = False
resultado = 0

while not salir:
    print('''\nOperaciones que puedes realizar:
    1. Sumar 2 valores.
    2. Restar 2 valores.
    3. Multiplicar 2 valores.
    4. Dividir 2 valores.
    5. Salir.
    ''')

    opcion = float(input('Elige una una opción: '))
    #? SUMA
    if opcion == 1:
        print('\nVas a sumar 2 valores:')
        valor_1 = float(input('\nIngresa el primer valor: '))
        valor_2 = float(input('Ingresa el segundo valor: '))
        resultado = valor_1 + valor_2
        print(f'\nEl resultado de la suma es {resultado:.2f}')
    #? RESTA

    elif opcion ==2:
        print('\nVas a restar 2 valores:')
        valor_1 = float(input('\nIngresa el primer valor: '))
        valor_2 = float(input('Ingresa el segundo valor: '))
        resultado = valor_1 - valor_2
        print(f'\nEl resultado de la resta es {resultado:.2f}')

    #? MULTIPLICACION
    elif opcion ==3:
        print('\nVas a multiplicar 2 valores:')
        valor_1 = float(input('\nIngresa el primer valor: '))
        valor_2 = float(input('Ingresa el segundo valor: '))
        resultado = valor_1 * valor_2
        print(f'\nEl resultado de la multiplicación es {resultado:.2f}')
 
    #? DIVISION
    elif opcion ==4:
        print('\nVas a dividir 2 valores:')
        valor_1 = float(input('\nIngresa el primer valor: '))
        valor_2 = float(input('Ingresa el segundo valor: '))
        if valor_2 == 0:
            print('\nNo es posible divivir en cero.')
        else:
            resultado = valor_1 / valor_2
            print(f'\nEl resultado de la división es {resultado:.2f}')
    elif opcion == 5:
        salir = True
        print(f'\nSaliendo de la calculadora.')
    #? OPCION INVALIDA
    else:
        print('\nIngresaste una opción inválida. Reintenta.')
    #? FIN
else:
    print('\nFinalizando aplicación...\n')