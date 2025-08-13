print('*** Bienvenidos a La Casa de los Espejos ***')

edad = int(input('Cual es tu edad? '))
tienes_miedo_oscuridad = input('Tienes miedo a la oscuridad (Si/No)? ').strip().lower() == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a La Casa de los Espejos.')
else:
    print('No puedes entrar a La Casa de los Espejos.')