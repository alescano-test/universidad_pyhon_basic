print('Sistema de calificaciones')

nota = float(input('Proporcion una calificacion entre 0 y 10: '))
letra_nota = None

if nota <= 9 and nota <= 10:
    letra_nota = 'A'
elif nota >= 8 and nota < 9:
    letra_nota = 'B'
elif nota >= 7 and nota < 8:
    letra_nota = 'C' 
elif nota >= 6 and nota <= 7:
    letra_nota = 'D'
elif nota >= 0 and nota < 6:
    letra_nota = 'F'
else:
    letra_nota = 'Calificación incorrecta'

print(f'Calificación de {nota} es equivalente a {letra_nota}.')
