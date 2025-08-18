from random import randint
print('\n"¡Que la suerte te acompañe en cada paso que des!\n')

#* REGLAS GLOBALES
MAXIMO_PARTIDAS = 5
RANDOM_MAX = 100

#* OPORTUNIDADES
intentos_restantes = MAXIMO_PARTIDAS

#* NÚMERO SECRETO
numero_secreto = randint(0, RANDOM_MAX)
adivinanza = None


while adivinanza != numero_secreto:
    adivinanza = int(input(f'Adivina el número secreto entre 0 y {RANDOM_MAX} en un máximo de {intentos_restantes} intentos: '))

    #! Ayuda al jugador.
    if adivinanza < numero_secreto:
        intentos_restantes -= 1
        print('El número secreto es mayor.')
    elif adivinanza > numero_secreto:
        intentos_restantes -= 1
        print('El numero secreto es menor.')
else:
    #! Fin
    print(f'\nFelicidades lograste resolverlo en {5 - intentos_restantes} intentos.')