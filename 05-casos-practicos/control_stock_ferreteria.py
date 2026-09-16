```python
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
            print('\nCARGA DE HERRAMIENTAS')

            if len(herramientas) > 0:
                print('Ya hay herramientas cargadas')

            else:
                carga_herramienta = input('\nCuantas herramientas deseas cargar?: ').strip()

                while not carga_herramienta.isdigit() or int(carga_herramienta) <= 0:
                    print('Error, ingrese un numero entero positivo')
                    carga_herramienta = input('\nCuantas herramientas deseas cargar?: ').strip()

                carga_herramienta = int(carga_herramienta)

                for cargar in range(carga_herramienta):
                    cargas = input(f'Carga la herramienta n{cargar + 1}: ').strip()

                    while not cargas.replace(" ", "").isalpha() or cargas in herramientas:

                        if cargas == '':
                            print('Error, el nombre no puede estar vacio')

                        elif not cargas.replace(" ", "").isalpha():
                            print('Error de carga, agregue una herramienta valida')

                        elif cargas in herramientas:
                            print('Error, la herramienta ya esta cargada')

                        cargas = input(f'Carga la herramienta n{cargar + 1}: ').strip()

                    herramientas.append(cargas)
                    print('Herramienta cargada correctamente')

                print('\nHerramientas cargadas:')

                for i in range(len(herramientas)):
                    print(f'{i + 1}- {herramientas[i]}')

        case 2:
            print('\nVAMOS A CARGAR EL STOCK')

            if len(herramientas) == 0:
                print('Primero debe cargar herramientas')

            elif len(stock) > 0:
                print('El stock inicial ya fue cargado')

            else:
                for i in range(len(herramientas)):
                    cargar_stock = input(f'Herramienta: {herramientas[i]}, Stock: ').strip()

                    while not cargar_stock.isdigit():
                        print('Error, ingrese un numero entero positivo o cero')
                        cargar_stock = input(f'Herramienta: {herramientas[i]}, Stock: ').strip()

                    cargar_stock = int(cargar_stock)
                    stock.append(cargar_stock)

                    print('Stock agregado correctamente')
                    print(f'Herramienta: {herramientas[i]}, Stock: {stock[i]}')

        case 3:
            print('\nVER STOCK')

            if len(herramientas) == 0:
                print('No hay herramientas cargadas')

            elif len(stock) != len(herramientas):
                print('Todavia no se cargo el stock de todas las herramientas')

            else:
                for ver in range(len(herramientas)):
                    print(f'Herramienta: {herramientas[ver]}, Stock: {stock[ver]}')

        case 4:
            print('\nCONSULTAR STOCK')

            if len(herramientas) == 0:
                print('No hay herramientas cargadas')

            else:
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
            print('\nSIN STOCK')

            if len(herramientas) == 0:
                print('No hay herramientas cargadas')

            elif len(stock) != len(herramientas):
                print('Primero debe cargar el stock de todas las herramientas')

            else:
                hay_agotados = False

                for i in range(len(herramientas)):

                    if stock[i] == 0:
                        print(f'{herramientas[i]}: Sin stock (0)')
                        hay_agotados = True

                if not hay_agotados:
                    print('No hay herramientas agotadas')

        case 6:
            print('\nALTA DE NUEVO PRODUCTO')

            agregar = input('Que herramienta deseas agregar?: ').strip()

            if agregar == '':
                print('Error, nombre vacio')

            elif not agregar.replace(' ', '').isalpha():
                print('Error, nombre invalido')

            elif agregar in herramientas:
                print('Ese producto ya existe')

            else:
                herramientas.append(agregar)

                print('Herramienta agregada con exito')
                print('\nAHORA AGREGAR STOCK')

                stock_agregar = input(f'Cuanto stock tiene {agregar}?: ').strip()

                while not stock_agregar.isdigit():
                    print('ERROR, dato invalido')
                    stock_agregar = input(f'Cuanto stock tiene {agregar}?: ').strip()

                stock_agregar = int(stock_agregar)

                print('Agregando stock...')
                stock.append(stock_agregar)

                print('\nLISTA ACTUALIZADA')

                for ver in range(len(herramientas)):
                    print(f'Herramienta: {herramientas[ver]}, Stock: {stock[ver]}')

        case 7:
            print('\nACTUALIZAR STOCK')

            if not herramientas or len(stock) != len(herramientas):
                print('Primero carga las herramientas y su stock')
                continue

            eleccion = input('Que deseas hacer? Quitar/Agregar: ').strip().lower()

            while eleccion != 'quitar' and eleccion != 'agregar':
                print('Error, solo alguna de esas dos opciones')
                eleccion = input('Que deseas hacer? Quitar/Agregar: ').strip().lower()

            buscar = input('Que herramienta?: ').strip()

            if buscar not in herramientas:
                print('La herramienta no esta registrada')

            else:
                posicion = herramientas.index(buscar)

                cantidad = input('Cantidad: ').strip()

                while not cantidad.isdigit() or int(cantidad) <= 0:
                    print('Ingrese un entero positivo')
                    cantidad = input('Cantidad: ').strip()

                cantidad = int(cantidad)

                if eleccion == 'agregar':
                    stock[posicion] += cantidad
                    print('Stock agregado correctamente')

                elif cantidad > stock[posicion]:
                    print('Stock insuficiente')

                else:
                    stock[posicion] -= cantidad
                    print('Stock retirado correctamente')

                print(f'{buscar}: {stock[posicion]} unidades')

        case 8:
            print('Hasta luego')
            break

