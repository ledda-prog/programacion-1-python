carrito = 0

while True:
    print('\n1. Agregar Hamburguesa ($4500)')
    print('2. Agregar Papas Fritas ($2000)')
    print('3. Agregar Bebida ($1500)')
    print('4. Pagar el pedido (Cierra el ticket)') 
    print('5. Cancelar pedido y salir')

#validamos que el dato sea correcto
    eleccion = input('ingrese una opcion: ')
    while not eleccion.isdigit() or not (1 <= int(eleccion) <= 5):
        print('ERROR.  INGRESASTE UN DATO NO VALIDO')
        eleccion = input('Ingrese una opcion: ')
    eleccion = int(eleccion)

    match eleccion:
        case 1:
            carrito = carrito + 4500
            print(f'\nHamburguesa añadida, su total es de: ${carrito}')
        case 2:
            carrito = carrito + 2000
            print(f'\nPapas fritas añadidas, su total es de: ${carrito}')
        case 3:
            carrito = carrito + 1500
            print(f'\nBebida añadida, su total es de: ${carrito}')
        case 4:
            while True:
                efectivo = input('Ingrese el efectivo: ')
    
                while not efectivo.isdigit():
                    print('ERROR. Ingrese un monto entero.')
                    efectivo = input('Ingrese el efectivo: ')
    
                efectivo = int(efectivo)
    
                if efectivo >= carrito:
                    vuelto = efectivo - carrito
                    print(f'Pago realizado. Vuelto: ${vuelto}')
                    carrito = 0
                    break
                else:
                    print('ERROR. El efectivo no alcanza. Intente nuevamente.')

        case 5:
            break