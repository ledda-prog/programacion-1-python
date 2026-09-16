saldo = 50000
while True:
    print('1- Consultar saldo.')
    print('2- Ingresar dinero.')
    print('3- Retirar dinero.')
    print('4- Salir')

    eleccion = input('Ingrese una opcion: ')
    while not eleccion.isdigit():
        print('ERROR.  INGRESASTE UN DATO NO VALIDO')
        eleccion = input('Ingrese una opcion: ')
    eleccion = int(eleccion)

    match eleccion:
        case 1:
            print(saldo)
        case 2:
            ingresar = input('Cuanto quieres ingresar: ')
            while not ingresar.isdigit():
                print('ERROR.  INGRESASTE UN DATO NO VALIDO')
                ingresar = input('Ingrese una opcion: ')
            ingresar = int(ingresar)
            if ingresar >= 0:
                saldo = saldo + ingresar
                print(f'tu saldo es: {saldo}')
        case 3: 
            retirar = input('Cuanto quieres retirar?: ')
            while not retirar.isdigit():
                print('ERROR.  INGRESASTE UN DATO NO VALIDO')
                retirar = input('Ingrese una opcion: ')
            retirar = int(retirar)
            if retirar <= saldo and retirar > 0:
                saldo = saldo - retirar
                print(f'tu saldo es: {saldo}')
            elif retirar > saldo:
                print('ERROR. NO PUEDES RETIRAR MAS DE LO QUE TIENES')
                print(f'tu saldo es: {saldo}')
        case _:
            break