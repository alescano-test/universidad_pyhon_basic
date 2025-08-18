
#* Sintaxis funcion range
#* inicio - valir inicial
#* fin - valor final, sin incluirlo
#* ingremento - diferencia entre cada número (opcional)

#! range(inicio, fin, incremento)

mensaje = input('\nIngresa el mensaje a repetir: ')
veces = int(input('\nIngresa las veces a repetir: '))

for i in range(veces):
    print(f' {i+1} - {mensaje}')