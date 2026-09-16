# Ejercicio 4 — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
# limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.

# Variables iniciales (NO se piden por teclado)
#   • energia = 100
#   • tiempo = 12
#   • cerraduras_abiertas = 0
#   • alarma = False
#   • codigo_parcial = ""

# Validaciones obligatorias
#   • No usar try/except
#   • Pedir nombre del agente y validar con .isalpha() en un while.
#   • Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
#   • El juego debe funcionar con estructuras secuenciales, condicionales y
# repetitivas (puede usar funciones propias del lenguaje como .lower(), len(),
# formateo, etc.).

# Regla anti-spam (muy importante)
# Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al iniciar:
# ✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
#   • se cobra el costo normal (-20 energía, -2 tiempo),
#   • NO abre cerradura, y se activa la alarma automáticamente (alarma = True) porque “la cerradura se trabó”.
# Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”

# Menú de acciones (se repite mientras el juego siga)
# El juego continúa mientras:
#   • energia > 0, tiempo > 0, cerraduras_abiertas < 3
#   • y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú:
# 1. Forzar cerradura (costo: -20 energía, -2 tiempo)
#   • Si la energía está por debajo de 40, hay “riesgo de alarma”:
#   • pedir un número 1-3 (validado). Si elige 3 → alarma=True.
#   • Si no hay alarma, abre 1 cerradura.
#   • Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre.

# 2. Hackear panel (costo: -10 energía, -3 tiempo)
#   • Debe usar un for de 4 pasos mostrando progreso.
#   • En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
#   • Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan.

# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)

# Regla de bloqueo por alarma
#   • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema se bloquea y se pierde.
# Condiciones de fin
#   • Si cerraduras_abiertas == 3 → VICTORIA
#   • Si energia <= 0 o tiempo <= 0 → DERROTA
#   • Si se bloquea por alarma → DERROTA (bloqueo)

# importamos shutil para mejorar lo visual(no altera el codigo)
import shutil
ancho = shutil.get_terminal_size().columns

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzadas_seguidas = 0

print('Iniciando juego...'.center(ancho))
print('=' * ancho)
print('ESCAPE ROOM. LA BOVEDA'.center(ancho))
print('=' * ancho)
print('\nHISTORIA.'.center(ancho))
print('\nSos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados. ' \
'Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.')
print()
print('=' * ancho)

#pedimos y validamos el nombre que sea solo letras
nombre = input('Como se va a llamar tu personaje?: ').strip().lower()
while not nombre.isalpha():
    print('Error, solo se permiten letras')
    nombre = input('Como se va a llamar tu personaje?: ').strip().lower()
print(f'\nBienvenido {nombre}')

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print('-' * ancho)
    print('ESTADO ACTUAL'.center(ancho))
    print(f'Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}'.center(ancho))
    print('-' * ancho)
    print()
    print('-' * ancho)
    print('ACCEDIENDO AL MENU'.center(ancho))
    print('-' * ancho)

    print('1. Forzar cerradura (costo: -20 energía, -2 tiempo)'.center(ancho))
    print('2. Hackear panel (costo: -10 energía, -3 tiempo)'.center(ancho))
    print('3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)'.center(ancho))

#pedimos la accion y validamos que sea solo numero entero
    accion = input('\nQue deseas hacer: 1, 2 o 3?: ').strip()

    while not accion.isdigit() or not 1 <= int(accion) <= 3:
        print('Error, solo se acepta: 1, 2 o 3')
        accion = input('Que deseas hacer: 1, 2 o 3?: ').strip()

    accion = int(accion)

    match accion:
        case 1:
            print('Forzando cerradura...'.center(ancho))
            print('Energia: ', energia, ' - 20')
            energia -= 20
            print('Energia actual: ', energia)
            print('Tiempo: ', tiempo, ' - 2')
            tiempo -= 2
            print('Tiempo actual: ', tiempo)
            forzadas_seguidas += 1

            if energia > 0 and tiempo > 0:
                if forzadas_seguidas >= 3:
                    alarma = True
                    print('ALARMA ACTIVADA POR FORZAR 3 VECES SEGUIDAS'.center(ancho))

                elif energia < 40:
                    num_alarma = input("elija 1, 2 o 3: ").strip()

                    while not num_alarma.isdigit() or not 1 <= int(num_alarma) <= 3:
                        print("error: elija un numero del 1 al 3.")
                        num_alarma = input("elija 1, 2 o 3: ").strip()

                    num_alarma = int(num_alarma)

                    if num_alarma == 3:
                        alarma = True
                    else:
                        cerraduras_abiertas += 1

                else:
                    cerraduras_abiertas += 1

        case 2:
            print('Hackeando sistema...'.center(ancho))
            print('Energia: ', energia, ' - 10')
            energia -= 10
            print('Energia actual: ', energia)
        
            print('Tiempo: ', tiempo, ' - 3')
            tiempo -= 3
            print('Tiempo actual: ', tiempo)
        
            forzadas_seguidas = 0
        
            if energia > 0 and tiempo > 0:
                codigo_hack = 'utnmdz26'
        
                for pasos in range(4):
                    codigo_parcial += codigo_hack[len(codigo_parcial)]
                    print(f'C0dig0: {codigo_parcial}'.center(ancho))
        
                if len(codigo_parcial) >= 8:
                    print(f'C0dig0 hackeado: {codigo_parcial}'.center(ancho))
                    print('CERRADURA ABIERTA'.center(ancho))
                    cerraduras_abiertas += 1
                    codigo_parcial = ''

        case 3:
            print('Descansando...'.center(ancho))
            print('Energia: ', energia, ' + 15')

            energia += 15

            if energia > 100:
                energia = 100

            print('Energia actual: ', energia)

            print('Tiempo: ', tiempo, ' - 1')
            tiempo -= 1
            print('Tiempo actual: ', tiempo)

            forzadas_seguidas = 0

            if alarma == True:
                print('-10 de energia por tener la alarma encendida')
                energia -= 10
                print('Energia actual: ', energia)

    
    if cerraduras_abiertas == 3:
        print('=' * ancho)
        print('GANASTE, PUDISTE ABRIR LA BOVEDA'.center(ancho))
        print('=' * ancho)
        break

    elif alarma == True and tiempo <= 3:
        print('=' * ancho)
        print('PERDISTE, LA ALARMA BLOQUEO EL SISTEMA'.center(ancho))
        print('=' * ancho)
        break

    elif tiempo <= 0:
        print('=' * ancho)
        print('PERDISTE, SE TE AGOTO EL TIEMPO'.center(ancho))
        print('=' * ancho)
        break

    elif energia <= 0:
        print('=' * ancho)
        print('PERDISTE, SE TE AGOTO LA ENERGIA'.center(ancho))
        print('=' * ancho)
        break
