# Reglas
# 1. Pedir nombre del operador (solo letras).

# 2. Menú repetitivo hasta salir:
# 1. Reservar turno
# 2. Cancelar turno (por nombre)
# 3. Ver agenda del día
# 4. Ver resumen general
# 5. Cerrar sistema

# 3. Reservar:
#  - Elegir día (1=Lunes, 2=Martes).
#  - Pedir nombre del paciente (solo letras).
#  - Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
#  - Guardar en el primer espacio libre (ej. lunes1, lunes2…).

# 4. Cancelar:
#  - Elegir día.
#  - Pedir nombre del paciente (solo letras).
#  - Si existe, cancelar y dejar el espacio vacío ("").

# 5. Ver agenda del día:
#  - Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.

# 6. Resumen general:
#  - Turnos ocupados y disponibles por día.
#  - Día con más turnos ( - empate).
# Restricciones
# • ❌ No listas, no diccionarios, no sets, no tuplas.
# • ✅ Se permite usar "" como “vacío”.
# • ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).

lunes_1 = ''
lunes_2 = ''
lunes_3 = ''
lunes_4 = ''

martes_1 = ''
martes_2 = ''
martes_3 = ''

operador = input('Ingrese su nombre: ').strip().lower()

while not operador.isalpha():
    print('ERROR. Ingreso un dato no valido')
    operador = input("Ingrese su nombre: ").strip().lower()

while True:
    print('\n 1. Reservar turno')
    print(' 2. Cancelar turno (por nombre)')
    print(' 3. Ver agenda del dia') 
    print(' 4. Ver resumen genearl')
    print(' 5. Cerrar sistema')
#validamos que elija un numero entre 1 y 5
    eleccion = input('Que deseas hacer (1,2,3,4 o 5)?: ').strip()
    while not eleccion.isdigit() or not 1 <= int(eleccion) <= 5:
        print('\nERROR. Ingrese un numero del 1 al 5')
        eleccion = input('Que deseas hacer (1,2,3,4 o 5)?: ').strip()
    eleccion = int(eleccion)

    match eleccion:
        case 1:
            print('=' * 60)
            print('RESERVAR TURNO')
            print('=' * 60)
#El while sirve para validar tambien que ingrese una opcion valida(1 o 2)
            while True:
                dia_eleccion = input('\nQue dia quieres reservar? lunes(1) o martes(2): ').strip()

                if dia_eleccion.isdigit():
                    dia_eleccion = int(dia_eleccion)

                    if dia_eleccion == 1 or dia_eleccion == 2:
                        break
                print('\nERROR. Ingresa solamente 1 o 2')

            if dia_eleccion == 1:
                nombre_dia = input('Introduzca su nombre: ').strip().lower()
                while not nombre_dia.isalpha():
                    print('Error, Introduzca su nombre.')
                    nombre_dia = input('Introduzca su nombre: ').strip().lower()

                print('\nPerfecto, asignando turno...')
#confirmamos que no tenga una reserva ya 
                if (nombre_dia == lunes_1 or nombre_dia == lunes_2 or nombre_dia == lunes_3 or nombre_dia == lunes_4):

                    print("error. el paciente ya tiene un turno el lunes.")

                else:
                    if lunes_1 == '':
                        lunes_1 = nombre_dia
                        print('Se le asigno el primer turno: 8:00am')

                    elif lunes_2 == '':
                        lunes_2 = nombre_dia
                        print('Se le asigno el segundo turno: 9:00am')

                    elif lunes_3 == '':
                        lunes_3 = nombre_dia
                        print('Se le asigno el tercer turno: 10:00am')

                    elif lunes_4 == '':
                        lunes_4 = nombre_dia
                        print('Se le asigno el cuarto turno: 11:00am')

                    else:
                        print('Agenda del lunes llena.')
                        print('\nredirigiendo al menu principal...')
            else:
                nombre_dia = input('Introduzca su nombre: ').strip().lower()
                while not nombre_dia.isalpha():
                    print('Error, Introduzca el nombre con el que entro.')
                    nombre_dia = input('Introduzca su nombre: ').strip().lower()

                print('\nPerfecto, asignando turno...')

                if (nombre_dia == martes_1 or nombre_dia == martes_2 or nombre_dia == martes_3):
                    print("error. el paciente ya tiene un turno el martes.")

                else:
                    if martes_1 == '':
                        martes_1 = nombre_dia
                        print('Se le asigno el primer turno: 8:30am')

                    elif martes_2 == '':
                        martes_2 = nombre_dia
                        print('Se le asigno el segundo turno: 9:30am')

                    elif martes_3 == '':
                        martes_3 = nombre_dia
                        print('Se le asigno el tercer turno: 10:30am')

                    else:
                        print('Agenda del martes llena.')
                        print('\nredirigiendo al menu principal...')
        case 2:
            print('=' * 60)
            print('CANCELAR TURNO')
            print('=' * 60)          

            while True:
                dia_eliminar = input('\nQue dia tienes turno? lunes(1) o martes(2): ').strip()

                if dia_eliminar.isdigit():
                    dia_eliminar = int(dia_eliminar)

                    if dia_eliminar == 1 or dia_eliminar == 2:
                        break
                print('\nERROR. Ingresa solamente 1 o 2')
            if dia_eliminar == 1:

                nombre_eliminar = input('Ingrese su nombre: ').strip().lower()

                while not nombre_eliminar.isalpha():
                    print('ERROR. Ingreso un dato no valido')
                    nombre_eliminar = input('Ingrese su nombre: ').strip().lower()

                if (nombre_eliminar == lunes_1 or nombre_eliminar == lunes_2 or
                    nombre_eliminar == lunes_3 or nombre_eliminar == lunes_4):

                    if nombre_eliminar == lunes_1:
                        print('Eliminando turno...')
                        lunes_1 = ''
                        print("turno cancelado correctamente.")

                    elif nombre_eliminar == lunes_2:
                        print('Eliminando turno...')
                        lunes_2 = '' 
                        print("turno cancelado correctamente.")                   

                    elif nombre_eliminar == lunes_3:
                        print('Eliminando turno...')
                        lunes_3 = ''
                        print("turno cancelado correctamente.")

                    elif nombre_eliminar == lunes_4:
                        print('Eliminando turno...')
                        lunes_4 = ''
                        print("turno cancelado correctamente.")

                else:
                    print("error. el paciente no tiene turno el lunes.")

            else:
                nombre_eliminar = input('Ingrese su nombre: ').strip().lower()
                
                while not nombre_eliminar.isalpha():
                    print('ERROR. Ingreso un dato no valido')
                    nombre_eliminar = input('Ingrese su nombre: ').strip().lower()

                if (nombre_eliminar == martes_1 or nombre_eliminar == martes_2 or
                    nombre_eliminar == martes_3):

                    if nombre_eliminar == martes_1:
                        print('Eliminando turno...')
                        martes_1 = ''
                        print("turno cancelado correctamente.")

                    elif nombre_eliminar == martes_2:
                        print('Eliminando turno...')
                        martes_2 = ''      
                        print("turno cancelado correctamente.")              

                    elif nombre_eliminar == martes_3:
                        print('Eliminando turno...')
                        martes_3 = ''
                        print("turno cancelado correctamente.")

                else:
                    print("error. el paciente no tiene turno el martes.")
        case 3:

            print('=' * 60)
            print('VER AGENDA DEL DIA')
            print('=' * 60)

            while True:
                dia_ver = input('\nQue dia desea ver? lunes(1) o martes(2): ').strip()

                if dia_ver.isdigit():
                    dia_ver = int(dia_ver)

                    if dia_ver == 1 or dia_ver == 2:
                        break
                print('\nERROR. Ingresa solamente 1 o 2')

            if dia_ver == 1:
                print('-----LUNES-----')

                if lunes_1 == '':
                    print('Primer turno: (libre)')
                else:
                    print(f'Primer turno: {lunes_1}')

                if lunes_2 == '':
                    print('Segundo turno: (libre)')
                else:
                    print(f'Segundo turno: {lunes_2}')

                if lunes_3 == '':
                    print('Tercer turno: (libre)')
                else:
                    print(f'Tercer turno: {lunes_3}')

                if lunes_4 == '':
                    print('Cuarto turno: (libre)')
                else:
                    print(f'Cuarto turno: {lunes_4}')

            else:
                print('-----MARTES-----')

                if martes_1 == '':
                    print('Primer turno: (libre)')
                else:
                    print(f'Primer turno: {martes_1}')

                if martes_2 == '':
                    print('Segundo turno: (libre)')
                else:
                    print(f'Segundo turno: {martes_2}')

                if martes_3 == '':
                    print('Tercer turno: (libre)')
                else:
                    print(f'Tercer turno: {martes_3}')

        case 4:

            print('=' * 60)
            print('VER RESUMEN GENERAL')
            print('=' * 60)


            lunes = 0
            martes = 0
#contadores para ver cuantos turnos ocupados tienen los dias
            if lunes_1 != '':
                lunes = lunes + 1
            if lunes_2 != '':
                lunes = lunes + 1
            if lunes_3 != '':
                lunes = lunes + 1
            if lunes_4 != '':
                lunes = lunes + 1

            if martes_1 != '':
                martes = martes + 1
            if martes_2 != '':
                martes = martes + 1
            if martes_3 != '':
                martes = martes + 1

            if lunes > martes: 
                print(f'Lunes tiene mas turnos ocupados: Lunes: {lunes}, Martes: {martes}')
            elif lunes < martes:
                print(f'Martes tiene mas turnos ocupados: Martes: {martes}, Lunes: {lunes}')
            else:
                print(f'Estan empatados en los dias ocupados. Lunes: {lunes}, Martes: {martes}')

            libres_lunes = 4 - lunes
            libres_martes = 3 - martes

            print('Turnos libres lunes: ', libres_lunes)
            print('Turnos libres martes: ',libres_martes)

        case 5:
            print('Gracias por elegirnos')
            print('Saliendo...')
            break