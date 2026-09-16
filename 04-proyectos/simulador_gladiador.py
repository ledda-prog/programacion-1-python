# Ejercicio 5 — “Escape Room:"La Arena del
# Gladiador"
# 1. Descripción del Escenario
#   Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un
#   usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El
#   objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.
#   Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de
#   control (if/elif/else), ciclos (while y for) y validación de datos estricta.

# 2. Requerimientos Técnicos
#   A. Tipos de Datos
#   Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:
#       • String: Para el nombre del jugador.
#       • Int: Para los Puntos de Vida (HP) y cantidad de pociones.
#       • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5).
#       • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.

#   B. Reglas de Validación (¡Importante!)
#       • No está permitido usar bloques try / except.
#       • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.
#       • Para validar números, debes usar el método .isdigit() dentro de un ciclo while.

# 3. Flujo del Programa
#   Paso 1: Configuración del Personaje
#      El programa inicia pidiendo el nombre del Gladiador.
#          • Validación: El nombre solo puede contener letras. Si el usuario ingresa números,
#            símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a preguntar hasta que sea válido.

#   Paso 2: Inicialización de Estadísticas
#       El programa debe definir las variables iniciales (sin preguntar al usuario):
#           • Vida del Gladiador: 100 (int)
#           • Vida del Enemigo: 100 (int)
#           • Pociones de Vida: 3 (int)
#           • Daño base "Ataque Pesado": 15 (int)
#           • Daño base del enemigo: 12 (int)
#           • Turno Gladiador : True (booleano)

#   Paso 3: El Ciclo de Combate
#       El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 puntos de vida.
#       Turno del Jugador:
#       Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3
#       opciones:
#           1. Ataque Pesado
#           2. Ráfaga Veloz (Requiere uso de for)
#           3. Curar
#       • Validación del Menú: El programa debe pedir la opción al usuario. 
#           1. Verificar que lo ingresado sea un número (.isdigit()).
#           2. Verificar que el número sea 1, 2 o 3. o Si falla alguna validación, mostrar mensaje de error y volver a pedir.

#       Lógica de las Acciones:
#           Acción A: Ataque Pesado (Opción 1)
#               • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).
#               • Resta el daño a la vida del enemigo.
#               • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
#           Acción B: Ráfaga Veloz (Opción 2)
#               • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.
#               • El bucle debe repetirse 3 veces (usando range).
#               • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.
#               • Muestra el mensaje: " > Golpe conectado por 5 de daño".
#           Acción C: Curar (Opción 3)
#               • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
#               • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el enemigo ataca igual).

#       Turno del Enemigo:
#           Justo después de tu acción, el enemigo ataca automáticamente.
#               • Resta el daño base del enemigo (12) a tu vida.
#               • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"
#   Paso 4: Fin del Juego
#       Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:
#           • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
#           • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate." 

import shutil
ancho = shutil.get_terminal_size().columns

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_g = True
golpe_critico = 1.5

print('Iniciando juego...'.center(ancho))
print('=' * ancho)
print('GLADIADOR, LA  VENGANZA DEL CAIDO'.center(ancho))
print('=' * ancho)
print('\nHISTORIA.'.center(ancho))
print('\nSos un soldado de la antigua Roma, y te hicieron prisionero por una causa injusta, ahora te toca pelear en el coliseo para seguir viviendo....')
print()
print('=' * ancho)

#validamos nombre
nombre = input('Como te llamas gladiador?: ').strip().lower()
while not nombre.isalpha():
    print('Error, solo se permiten letras')
    nombre = input('Solo dime como te llamas: ').strip().lower()
print(f'\nBienvenido {nombre}')
print('=' * ancho)

print('\nViejo prisionero: Acaso no eres algo de Maximo Decimo Meridio?')
s_n = input('si - no: ').strip().lower()

while not s_n.isalpha() or (s_n != 'si' and s_n != 'no'):
    print('Viejo prisionero: Solo dime si lo eres o no.')
    s_n = input('si - no: ').strip().lower()

if s_n == 'si':
    print('Viejo prisionero: Jajajajaja, aun recuerdo cuando pelee a su lado, que recuerdos.')
else:
    print('Viejo prisionero: Te pareces un poco a el, es un viejo conocido.')

print('\n***se escuchan pasos a lo lejos***')
print('Guardia: Vos, basura nueva, te toca ir a pelear.')
print('Viejo prisionero: Suerte wey')

#la primer condicion para que funcione el juego
while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_g == True:

        print('-' * ancho)
        print('STATS COMBATE'.center(ancho))
        print(f'HP: {vida_gladiador} | Pociones: {pociones} | Vida enemigo: {vida_enemigo} | Mensaje: Trata de conectar algun golpe critico'.center(ancho))
        print('-' * ancho)
        print()
        print('-' * ancho)
        print('ACCEDIENDO AL MENU'.center(ancho))
        print('-' * ancho)

        print('1. Ataque Pesado (Quita 15HP)'.center(ancho))
        print('2. Rafaga Veloz (3 ataques, 5HP por golpe)'.center(ancho))
        print('3. Pocion (Te cura 30HP)'.center(ancho))

        #pedimos la accion y validamos que sea solo numero entero
        accion = input('\nQue deseas hacer: 1, 2 o 3?: ').strip()

        while not accion.isdigit() or not 1 <= int(accion) <= 3:
            print('Error, solo se acepta: 1, 2 o 3')
            accion = input('Que deseas hacer: 1, 2 o 3?: ').strip()

        accion = int(accion)

        match accion:
            case 1:
                if vida_enemigo < 20:
                    golpe_final = ataque_pesado * golpe_critico
                    print('>¡GOLPE CRÍTICO!')
                else:
                    golpe_final = ataque_pesado
                vida_enemigo -= golpe_final
                print(f'>¡Atacaste al enemigo por {golpe_final} puntos de daño!')

            case 2:
                for golpe in range(3):
                    vida_enemigo -= 5
                    print('> Golpe conectado por 5 de daño')

            case 3:
                if pociones > 0:
                    vida_gladiador += 30
                    pociones -= 1
                    print('>Usaste una pocion')
                else:
                    print('No quedan mas pociones')
        turno_g = False

    if turno_g == False and vida_enemigo > 0:
        print('=' * 30)
        print('>Se viene un ataque del enemigo!!!')
        print('>Te acerto el golpe')
        print(f'>Vida - {ataque_enemigo}HP')
        vida_gladiador -= ataque_enemigo
        turno_g = True

if vida_enemigo <= 0:
    print('=' * ancho)
    print(f'¡VICTORIA! {nombre} ha ganado la batalla.'.center(ancho))
    print('FELICITACIONES MATASTE AL ENEMIGO'.center(ancho))
    print('=' * ancho)
else:
    print('=' * ancho)
    print('DERROTA. Has caído en combate.'.center(ancho))
    print('TE DERROTO EL ENEMIGO. ARMATE MEJOR PARA MAÑANA'.center(ancho))
    print('=' * ancho)