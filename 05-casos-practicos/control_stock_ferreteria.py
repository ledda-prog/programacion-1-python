herramientas = []
stock = []

print('Bienvenido')
while True:

    print('\n1-Carga de herramientas')
    print('2-Cargar stock')
    print('3-Ver stock')
    print('4-Consultar stock')
    print('5-Reporte de agotados')
    print('6-Agregar nuevo producto')
    print('7-Actualizar stock')
    print('8-Salir')

    accion = input('\nQue deseas hacer?: ').strip()
    while not accion.isdigit() or int(accion) <= 0 or int(accion) >= 9:
        print('Error, ingrese un dato valido')
        accion = input('Que deseas hacer?: ').strip()
    accion = int(accion)

    match accion:
        case 1:

            carga_Herramienta = input('\nCuantas herramientas deseas cargar?: ').strip()
            while not carga_Herramienta.isdigit() or int(carga_Herramienta) <= 0:
                print('Error, ingrese un numero entero positivo')
                carga_Herramienta = input('\nCuantas herramientas deseas cargar?: ').strip()
            carga_Herramienta= int(carga_Herramienta)

            for cargar in range(carga_Herramienta):
                cargas = input(f'Carga la herramienta n{cargar + 1}: ').strip()

                while not cargas.replace(" ", "").isalpha():
                    print('Error de carga, agregue una herramienta valida')
                    cargas = input(f'Carga la herramienta n{cargar + 1}: ').strip()

                if cargas in herramientas:
                    print('Error, la herramienta ya esta cargada')
                else:
                    print('Herramienta cargada')
                    herramientas.append(cargas)
                print('\nHerramientas: ', cargas)

        case 2:
            print('\nVamos a cargar el stock')

            for i in range(len(herramientas)):

                cargar_stock = input(f'Herramienta: {herramientas[i]}, Stock: ').strip()
                while not cargar_stock.isdigit() or int(cargar_stock) < 0:
                    print('Error, ingrese un numero entero positivo')
                    cargar_stock = input(f'Herra mienta: {herramientas[i]}, Stock: ').strip()
                cargar_stock = int(cargar_stock)

                stock.append(cargar_stock)
                print('Stock agregado correctamente')
                print(f'Herramienta: {herramientas[i]}, Stock: {stock[i]}')

        case 3:

            for ver in range(len(herramientas)):
                print(f'Herramienta: {herramientas[ver]}, Stock: {stock[ver]}')

        case 4:
            print('\nConsultar stock')

            buscar = input('De que producto deseas buscar stock?: ').strip()
            while not buscar.replace(' ', '').isalpha():
                print('Error, dato invalido')
                buscar = input('De que producto deseas buscar stock?: ').strip()

            if buscar in herramientas:
                posicion = herramientas.index(buscar)

                if posicion < len(stock):
                    print(f'Herramienta: {buscar}, Stock: {stock[posicion]}')
                else:
                    print('Todavia no se cargo el stock de esa herramienta')
            else:
                print('El producto no esta registrado')

        case 5:
            print('Sin stock')

            for i in range(len(herramientas)):
                if stock[i] == 0:
                    print(f'{herramientas[i]}: Sin stock(0)')

        case 6:
            print('ALTA DE NUEVO PRODUCTO')

            agregar = input('Que herramienta deseas agregar?: ').strip()

            if agregar == '':
                print('Error, Nombre vacio')

            elif agregar in herramientas:
                print('Ese producto ya existe')

            elif agregar not in herramientas:
                herramientas.append(agregar)
                print('Herramienta agregada con exito')
                print(herramientas)

                print('\nAHORA AGREGAR STOCK')
                stock_agregar = input(f'Cuanto stock tiene {agregar}?: ').strip()

                while not stock_agregar.isdigit() or int(stock_agregar) < 0:
                    print('ERROR, dato invalido')
                    stock_agregar = input(f'Cuanto stock tiene {agregar}?: ').strip()
                stock_agregar = int(stock_agregar)

                print('Agregando stock...')
                stock.append(stock_agregar)

                for ver in range(len(herramientas)):
                    print(f'Herramienta: {herramientas[ver]}, Stock: {stock[ver]}')

        case 7:
            print('\nACTUALIZAR STOCK')

            if not herramientas or len(stock) != len(herramientas):
                print('Primero cargá las herramientas y su stock')
                continue

            eleccion = input('Que deseas hacer? Quitar/Agregar: ').strip().lower()
            while eleccion != 'quitar' and eleccion != 'agregar':
                print('Error, solo alguna de esas dos opciones')
                eleccion = input('Que deseas hacer? Quitar/Agregar: ').strip().lower()

            buscar = input('Que herramienta?: ').strip()

            if buscar not in herramientas:
                print('La herramienta no está registrada')
            else:
                posicion = herramientas.index(buscar)

                cantidad = input('Cantidad: ').strip()
                while not cantidad.isdigit() or int(cantidad) <= 0:
                    print('Ingrese un entero positivo')
                    cantidad = input('Cantidad: ').strip()
                cantidad = int(cantidad)

                if eleccion == 'agregar':
                    stock[posicion] += cantidad
                elif cantidad > stock[posicion]:
                    print('Stock insuficiente')
                else:
                    stock[posicion] -= cantidad

                print(f'{buscar}: {stock[posicion]} unidades')

        case 8:
            print('Hasta luego')
            break
