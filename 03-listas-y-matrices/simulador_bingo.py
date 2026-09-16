import random

numeros = random.sample(range(5,50),25)

carton = []

for i in range(0,25, 5):
    carton.append(numeros[i:i+5])

sorteo = random.sample(range(1, 51), 50)

bingo = False
cantidad = 0

while not bingo:

    numero = sorteo[cantidad]
    cantidad += 1
    print("\nSalió:", numero)

    for fila in carton:
        for i in range(5):
            if fila[i] == numero:
                fila[i] = 'X'

    for fila in carton:
        for casillero in fila:
            print(casillero, end=' ')
        print('')

    #esto revisa filas
    for fila in carton:
        if all(numero == "X" for numero in fila):   #all() sirve para ver que se cumpla todo lo que esta adentro del parentesis 
            bingo = True

    #esto las columnas
    for columna in range(5):
        if all(carton[fila][columna] == "X" for fila in range(5)):
            bingo = True

    # revisa las diagonales
    if all(carton[i][i] == "X" for i in range(5)):
        bingo = True

    if all(carton[i][4-i] == "X" for i in range(5)):
        bingo = True


print("\n¡BINGO!")
print("Números sorteados:", cantidad)