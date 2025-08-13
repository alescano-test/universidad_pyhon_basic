print('\nBienvenido al Sistema de Reserva de Hotel')

# Constantes
DIA_CUARTO_VISTA_MAR = 190.50
DIA_CUARTO_SIN_VISTA_MAR = 150.50

# Solicitar datos al usuario
print('\nLos precios por día son los siguientes: ')
print('Cuarto sin vista al mar: $150.50 por día.')
print('Cuarto con vista al mar: $190.50 por día.')
nombre_cliente = input('\nCual es tu nombre? ')
dias_estadia = int(input('Cantidad de días de estadía? '))
vista_mar = input('Quieres un cuarto con vista al mar (Si/No)? ').strip().lower()

# Calcular costo total de la estadía y si tiene vista al mar o no
precio_total_estadia = DIA_CUARTO_VISTA_MAR * dias_estadia if vista_mar == 'si' else DIA_CUARTO_SIN_VISTA_MAR * dias_estadia
vista_al_mar_txt = 'Si' if vista_mar == 'si' else 'No'

print('\n---------- Detalles de la reservación ----------')
print(f'Cliente: {nombre_cliente}')
print(f'Días de estadía: {dias_estadia}')
print(f'Costo total: ${precio_total_estadia:.2f}')
print(f'Habitación con vista al mar: {vista_al_mar_txt}')