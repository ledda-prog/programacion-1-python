aula = [['L','L','L','L'],
        ['L','L','L','L'],
        ['L','L','L','L']]

for fila in aula:
    for asiento in fila:
        print(asiento, end=' ')
    print('')
    
while True: # while a_ocupar != -1
    print('')
    a_ocupar_fila = int(input('Ingrese la fila a ocupar, (-1 para detener el programa): '))
    a_ocupar_columna = int(input('Ingrese la columna a ocupar, (-1 para detener el programa): '))
    
    if a_ocupar_fila in range(0,3) and a_ocupar_columna in range(0,4):
        if aula[a_ocupar_fila][a_ocupar_columna] == 'L':
            aula[a_ocupar_fila][a_ocupar_columna] = 'O'
            print('Lugar ocupado correctamente.')
            continue
        else:
            print('Ese lugar ya estaba ocupado.')
            continue
    
    if a_ocupar_fila == -1 or a_ocupar_columna == -1:
        print('Saliendo...')
        break
    
    print('Fila o columna fuera de rango. Fila debe ser un numero entre 0 y 2. Columna debe ser un numero entre 0 y 3.')
    
contador = 0
for fila in aula:
    contador += fila.count('O')

print(f'Hay {contador} asientos ocupados.')

for fila in aula:
    for asiento in fila:
        print(asiento, end=' ')
    print('')
