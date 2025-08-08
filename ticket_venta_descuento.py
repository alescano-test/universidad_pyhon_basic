print("*** TICKET DE VENTA ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio platanos: "))
descuento_porcentaje = int(input("Aplicar algún descuento(%)? "))

# Cálculo del subtotal (sin impuestos)
subtotal_compra = precio_leche+precio_pan+precio_lechuga+precio_platanos

# Calcular descuento
descuento = subtotal_compra * (descuento_porcentaje/100)

# Calcular subtotal con descuento 
subtotal_descuento = subtotal_compra - descuento

# Calcular impuestos del subtotal con descuento

impuestos = subtotal_descuento * 0.16

# Cálculo total de la compra (con impuestos)
costo_total = subtotal_descuento + impuestos

print(f"""
Subtotal de la compra: ${subtotal_compra}
Descuento aplicado del ({descuento_porcentaje}%): ${descuento}
Impuesto aplicado del (16%): ${impuestos}
Subtotal con descuento: ${subtotal_descuento}
Costo total de la compra: ${costo_total}
""")