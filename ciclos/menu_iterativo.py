print('\n~~~ Menu iterativo ~~~\n')

salir = False

while not salir:
    print('''
    1. Crear cuenta.
    2. Elimiar cuenta.
    3. Salir.\n''')

    opcion = int(input('Elige una opción: '))
    if opcion == 1:
        print('\nCreando tu cuenta...\n')
    elif opcion == 2:
        print('\nEliminando tu cuenta...\n')
    elif opcion == 3:
        print('\nSaliendo del sistema...\n')
        salir = True
    else:
        print('\nOpción inválida, elige 1, 2 o 3.')
else:
    print('Terminando le ejecución del código...\n')

