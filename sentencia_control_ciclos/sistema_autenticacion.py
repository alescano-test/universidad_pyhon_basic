print('\n Sistema de Autenticacion')

USUARIO = 'Usuario'
PASS = 'PaSSw0rD'

usuario_ingreso = input('Ingresa tu usuario: ')
pass_ingreso = input('Ingresa tu password: ')
mensaje = None

if USUARIO == usuario_ingreso and PASS == pass_ingreso:
    mensaje = 'Bienvenido al sistema'
elif PASS == pass_ingreso:
    mensaje = 'Usuario inválido'
elif USUARIO == usuario_ingreso:
    mensaje = 'Password inválido'
else:
    mensaje = 'Usuario y password inválidos'

print(f'{mensaje}.')