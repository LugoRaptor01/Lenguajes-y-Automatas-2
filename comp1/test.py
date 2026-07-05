def calcular_total(productos):
    total = 0
    for producto in productos:
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        if cantidad >= 3:
            sutotal = precio * cantidad * 0.9
        else:
            subtotal = precio * cantidad
            total = total + subtotal
        return total
productos = [
    {"nombre": "Cuaderno", "precio" : 25, "cantidad" : 2},
    {"nombre": "Lápiz", "precio" : 5, "cantidad" : 4}
]