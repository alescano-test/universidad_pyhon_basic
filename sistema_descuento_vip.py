print("Sistema de descuentos VIP")

NRO_PRODUCTOS_DESCUENTO = 10
cantidad_productos_comprados = int(input("Cuantos productos compraste hoy? "))
tiene_membresia = str(input("Tiene la membresia de la tienda (Si/No)? "))

es_elegible_descuento_vip = (cantidad_productos_comprados >= NRO_PRODUCTOS_DESCUENTO and tiene_membresia.strip().lower() == "si")
print(f"Tienes acceso al descuento VIP: {es_elegible_descuento_vip}")