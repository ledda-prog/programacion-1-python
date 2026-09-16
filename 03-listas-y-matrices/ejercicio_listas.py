productos = []
precios = []
vendidos = []


while True:
    print('\nBuen dia, que deseas hacer?')
    print('\n1- Carga de productos')
    print('2- Carga de ventas del dia')
    print('4- Carga de productos')
    print('5- Carga de productos')
    print('6- Carga de productos')
    print('7- Carga de productos')
    print('8- Carga de productos')
    print('9- Carga de productos')
    accion = input('\n...').strip()

    while not accion.isdigit() or int(accion) < 1 or int(accion) > 9:
        print('Error, ingrese una opcion valida')
        accion = input('Que deseas hacer?: ').strip()
    accion = int(accion)

    match accion:
        case 1:
            print('='*60)
            print('CARGA DE PRODUCTOS')
            print('='*60)
            cargar = input('Cuantos productos se van a cargar?: ').strip()
            while not cargar.isdigit() or int(cargar) <= 0:
                print('Error, ingrese un dato valido')
                cargar = input('Cuantos productos se van a cargar?: ').strip()
            cargar = int(cargar)

            for cargados in range(cargar):

                producto = input('Que producto deseas cargar?: ').strip().lower()
                while not producto.replace(" ", "").isalpha():
                    print('Error, Ingreso un dato erroneo')
                    producto = input('Que producto deseas cargar?: ').strip().lower()

                if producto in productos:
                    print('el articulo ya esta cargado')
                    
                else:
                    productos.append(producto)

                    precio = input(f'Cual es el precio de: {producto}: ').strip()
                    while not precio.isdigit() or int(precio) <= 0:
                        print('Error, ingrese un dato valido')
                        precio = input(f'Cual es el precio de: {producto}: ').strip()
                    precio = int(precio)

                    precios.append(precio)

                    print(f'Producto cargado: {producto} - Precio: ${precio}')

        case 2:
            print()
            print('='*60)
            print('CARGA DE ventas del dia')
            print('='*60)

            