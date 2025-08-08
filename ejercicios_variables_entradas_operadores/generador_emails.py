# Crear un programa que genere un email a partir de los siguientes datos
#Resultado esperado: miguel.alejandro.lescano@tsoftglobal.com.ar
nombre_completo = 'Miguel Alejandro Lescano Andrada'
empresa = 'Tsoft Global'
dominio = '.com.ar'
print('*** Generador de emails ***')
print('Nombre de usuario:', nombre_completo)
print('Extensión de dominio:', dominio)
print('Dominio de email normalizado:', '@tsoftglobal.com.ar')
nombre_normalizado = nombre_completo.replace(' ','.').lower()
empresa_normalizada= empresa.replace(' ','').lower()
email_final = nombre_normalizado+'@'+empresa_normalizada+dominio
print(f'Email final generado: {email_final}')