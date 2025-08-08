
nombre = str(input("Ingresa tu nombre completo: "))
apellido = str(input("Ingresa tu apellido completo: "))
empresa = str(input("Ingresa el nombre de tu empres: "))
nombre_formateado = nombre.replace(" ",".").lower()
apellido_formateado = apellido.replace(" ", ".").lower()
empresa_formateado = empresa.replace(" ","").lower()

print(f"Tu email empresarial es: {nombre_formateado}.{apellido_formateado}@{empresa_formateado}.com.mx")