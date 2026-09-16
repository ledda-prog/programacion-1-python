# Ejercicio 1— “Caja del Kiosco” 
# Objetivo: Simular una compra con validaciones y cálculo de total. 
# Requisitos:
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). 
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while). 
# 3. Por cada producto (usar for): 
#    -Pedir precio (entero, validar .isdigit()). 
#    -Pedir si tiene  descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula). 
#    -Si tiene  descuento: aplicar 10% al precio de ese producto. 
# 4. Al final mostrar: 
#    -Total sin descuentos 
#    -Total con descuentos 
#    -Ahorro total 
#    -Promedio por producto (usar float y formatear con :.2f, ejem: 
#       x = 3.14159 
#       print(f"{x:.2f}"))


nombre = ''

#pedimos nombre dentro del while y validamos datos con .isalpha()
while nombre == '' or not nombre.isalpha():
    nombre = input('Cual es su nombre?: ').lower().strip()

    if nombre == '' or not nombre.isalpha():
        print('ERROR. INGRESO UN DATO INVALIDO')
print(f'\nBienvenido/a {nombre}')

numero = ''

while not numero.isdigit() or int(numero) <= 0:
    numero = input('\nCuantos productos desea comprar?: ')

    if not numero.isdigit() or int(numero) <= 0:
        print('ERROR. INGRESO UN DATO NO NUMERICO')

numero = int(numero)

#En este for vamos a pedir precio, descuento y validar que los datos sean correctos

totalSinDescuento = 0
totalConDescuento = 0
descripcionProductos = ""
for i in range(numero):
    precio = ''

    while not precio.isdigit() or int(precio) <= 0:
        precio = input(f'\n¿Cuál es el precio del producto {i + 1}?: ')

        if not precio.isdigit() or int(precio) <= 0:
            print('ERROR. Ingrese un valor entero positivo')
    precio = int(precio)
    totalSinDescuento += precio

    respuesta = ''
    while respuesta not in ("s", "n"):
        respuesta = input('El producto tiene descuento?: s/n  ').lower().strip()

        if respuesta not in ("s", "n"):
            print("ERROR. Ingreso un dato invalido.")

    if respuesta == 's':
        precioConDescuento = precio - precio * 0.10
    else:
        precioConDescuento = precio

    totalConDescuento += precioConDescuento
    descripcionProductos += f"Producto {i + 1} - Precio: {precio}  Descuento (S/N): {respuesta.upper()}\n"
ahorroTotal = totalSinDescuento - totalConDescuento
promedio = float(totalConDescuento / numero)

print()
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {numero}")
print(descripcionProductos, end="")
print(f"\nTotal sin descuentos: ${totalSinDescuento}")
print(f"Total con descuentos: ${totalConDescuento:.2f}")
print(f"Ahorro: ${ahorroTotal:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")