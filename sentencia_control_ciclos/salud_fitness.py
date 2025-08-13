print('\n*** Aplicación de Salud y Fitness ***')

#Constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

#Pedir valores al usuario

nombre_usuario = input('\nCual es tu nombre? ')
pasos_diarios = int(input('Cuántos pasos has camindado hoy? '))

#Verificar si el usuario alcanzó la meta de pasos diarios

meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

# Calcular las calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostrar la información

print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas:.2f} kcal')
print(f'Meta de pasos diarios alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIOS} pasos')