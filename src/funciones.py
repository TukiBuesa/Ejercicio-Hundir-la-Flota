# Scrip 3:  Funciones

import numpy as np
import random
import constantes as cons
from instrucciones_del_juego import *
from main_game_battleship import usuario_tablero, maquina_tablero

def creo_tablero():
    '''
    Función que genera tableros DONDE SE DISPARA
    '''
    tablero = np.empty((len(cons.FILAS), len(cons.COLUMNAS)), str)
    
    return tablero


def introduce_coordenadas(tablero, tipo_tablero):
    '''
    Función que recorre la lista de los barcos, pide coordenadas y valida si es posible colocarlos.
    '''
    for barco in cons.BARCOS_JUEGO:
        while True:
            if tipo_tablero == "jugador":
                print("Vamos a colocar un barco de {}:\n".format(barco))
                pos_x = int(input("Primero dime una fila (entre la 0 y la 9 incluidas): "))
                pos_y = int(input("Ahora dime una columna (entre la 0 y la 9 incluidas): "))
                orientacion = input("¿Quieres colocarlo en vertical (V) o horizontal (H)?:")
                print("Has introducido:\n\tFila: {}\n\tColumna: {}\n\tOrientación:{}\nComprobamos posición.".format(pos_x,pos_y,orientacion))
            else:
                pos_x, pos_y, orientacion = np.random.randint(len(cons.FILAS)), np.random.randint(len(cons.COLUMNAS)), np.random.choice(["V", "H"])          
            valido = comprobar_posicion(pos_x, pos_y, barco, orientacion, tablero)
            if valido:
                tablero = colocar_barcos(pos_x, pos_y, barco, orientacion,tablero)
                break
    if tipo_tablero == "jugador":
        return tablero
    else:
        return "Ya están colocados"


def comprobar_posicion(pos_x, pos_y, barco, orientacion, tablero):
    '''
    Función que comprueba si el barco se puede introducir, que no se salga, ni se superponga a otro
    '''
    if orientacion =="H":
        if pos_x + barco -1 > len(cons.COLUMNAS):
            print("Posicion no valida. Vuelve a intentarlo\n")
            return False
        else:
            cont = pos_y
            while cont < pos_y + barco:
                for i in range(pos_y, pos_y + barco):
                    if tablero[pos_x, i] == " ":
                        print("Check en H: Ya hay un barco en esta posición\n")
                        return False
                        break
                    else:
                        cont += 1
                        print("Ok, vamos a colocarlo\n")
                        return True
    else:
        if pos_y + barco -1 > len(cons.FILAS):
            print("Posicion no valida. Vuelve a intentarlo\n")
            return False
        else:
            cont = pos_x
            while cont < pos_x + barco:
                for i in range(pos_x, pos_x + barco):
                    if tablero[i, pos_y] == " ":
                        print("Check en V: Ya hay un barco en esta posición\n")
                        return False
                        break
                    else:
                        cont += 1
                        print("Ok, vamos a colocarlo\n")
                        return True


def colocar_barcos(pos_x, pos_y, barco, orientacion, tablero):
    '''
    Función para colocar flota una vez comprobado que es posible según las coordenadas dadas
    '''
    if orientacion == "V":
        tablero[pos_x:(pos_x+barco), pos_y] = str(barco)

    else:
        tablero[pos_x, pos_y:(pos_y + barco)] = str(barco) 
    
    return tablero


def disparo(disparo_fila, disparo_columna, tablero, turno):
    '''
    Función que recibe el disparo y comprueba en el tablero que corresponda si está hundido o tocado, en ese caso podrá en el tbalero una 'X' o si es agua pondrá 'A'
    '''
    # Aquí comprueba en el tablero con barcos de la máquina donde ha caido el disparo
    if turno  == "jugador":
        casilla = maquina_tablero[disparo_fila, disparo_columna]  
    
    # Aquí comprueba en el tablero con barcos del usuario donde ha caido el disparo
    else:
        casilla = usuario_tablero[disparo_fila, disparo_columna]  

    # Si cae en el agua
    if casilla == "":                                            
        casilla = "A"
        tablero[disparo_fila, disparo_columna] = casilla
        print("¡Agua!.\n")
        return False 
    
    # Si el barco tiene 1 sóla posición    
    elif casilla == "1":                                         
        casilla = "X"
        tablero[disparo_fila, disparo_columna] = casilla
        
        print("¡Hundido!. ¡Enhorabuena!\nVuelve a disparar\n")
        return True
    
    # Si toca un barco es de 2, 3 o 4
    elif casilla in ["2","3","4"]:                               
        casilla = "X"
        tablero[disparo_fila, disparo_columna] = casilla
        print("¡Tocado!. Dispara de nuevo\n")
        return True
    
    else:
        print("Ya habías disparado a esta coordenada. Vuelve a intentarlo\n")
        return True