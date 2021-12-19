# Script 4: Main_game_battleship

import numpy as np
import random
import constantes as cons
from instrucciones_del_juego import *
from funciones import *


# 1.INTRO E INSTRUCCIONES

print("------- JUEGO HUNDIR LA FLOTA by MARTA BUESA-------\n")

# Instrucciones del juego 
instrucciones_del_juego_hundir_la_flota()


# 2.COLOCACIÓN BARCOS DEL USUARIO:

# Objeto tablero del usuario
usuario_tablero = creo_tablero()
print("Aquí está tu tablero de usuario para colocar los barcos:\n", usuario_tablero)
print("\nEmpecemos por colocar tu flota: ")

# Introduzca coordenadas para colocar los barcos
introduce_coordenadas(usuario_tablero, "jugador")


# 3.COLOCACIÓN BARCOS DE LA MAQUINA:

# Objeto tablero de la maquina 
maquina_tablero = creo_tablero()

# Se colocan los barcos aleatoriamente en su tablero
introduce_coordenadas(maquina_tablero, "maquina")


# 4.COMIENZA EL JUEGO

# Tableros del usuario y de la maquina para jugar a hundir la flota
usuario_tablero_jugar = creo_tablero()
maquina_tablero_jugar = creo_tablero()

# Se jugará mientras haya alguien vivo
mientras_vivos = True

while mientras_vivos:
    # Turno del jugador
    es_turno = "jugador"
    while es_turno == "jugador":
        print("\n---------- TURNO DEL USUARIO ----------\nPor favor dime la casilla a la que quieres disparar.")
        disparo_fila = int(input("Primero dime una fila (entre la 0 y la 9 incluidas): "))
        while disparo_fila not in cons.FILAS:
            print("Por favor introduce un número correcto")
            disparo_fila = int(input("Dime una fila (entre la 0 y la 9 incluidas): "))
        
        disparo_columna = int(input("Ahora dime una columna (entre la 0 y la 9 incluidas): "))
        while disparo_columna not in cons.COLUMNAS:
            print("Por favor introduce una número correcto")
            disparo_columna = int(input("Dime una columna (entre la 0 y la 9 incluidas): "))
        
        print("Disparo a la casilla: ({}, {})".format(disparo_fila, disparo_columna))
        
        # Se comprueba la coordenada del disparo si hay acierto
        acierto = disparo(disparo_fila, disparo_columna, usuario_tablero_jugar, es_turno)
        print(usuario_tablero_jugar)
        
        # Se revisa si la maquina sigue viva
        if not np.any(np.isin(maquina_tablero, ["1", "2", "3", "4"])):
            print("¡¡¡¡¡¡¡Has hundido la flota de la maquina!!!!!!!\nEres un@ crack, ¡ENHORABUENA!")
            print(usuario_tablero_jugar)
            mientras_vivos = False
            break

        # Cambio de turno      
        if acierto == False:
            es_turno = "maquina"
        
    # Turno de la maquina
    while es_turno == "maquina":
        print("\n---------- TURNO DE LA MÁQUINA ----------\n")
        # Genera coordenadas de disparo aleatoriamente y comprueba si hay acierto
        acierto = disparo(np.random.randint(0, 9), np.random.randint(0, 9), maquina_tablero_jugar,es_turno)
        print(maquina_tablero_jugar)
    
        # Se revisa si el usuario sigue vivo
        if not np.any(np.isin(usuario_tablero, ["1", "2", "3", "4"])):
            print("¡La maquina ha hundido tu flota, usuario!\n\nOoooooooooooh!!!!!!!!!!!!  :( ")
            print(maquina_tablero_jugar)
            mientras_vivos = False
            break
        
        # Cambio de turno     
        if acierto == False:
            es_turno = "jugador"
    
print("\nFIN DE LA PARTIDA.\n\nEspero volver a verte pronto")