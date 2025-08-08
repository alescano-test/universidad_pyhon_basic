print("*** TICKET DE VENTA ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pam: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio platanos: "))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_leche+precio_pan+precio_lechuga+precio_platanos

# Cálculo del subtotal (sin impuestos)

impuesto = subtotal * 0.16

# Cálculo total de la compra (con impuestos)

costo_total = subtotal + impuesto

print(f"""
Subtotal: ${subtotal}
Impuesto (16%): ${impuesto}
Costo total de la compra: ${costo_total}
""")