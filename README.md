# Ejercicio-Hundir-la-Flota  :ship: :speedboat: :boat: :anchor:
Entregable del Bootcamp en Data Science en The Bridge | Digital Talent Accelerator (Madrid, SPAIN)

![battleship](hundir-la-flota-juego-de-mesa.jpg)

## Recursos utilizados
- Lenguaje de porgramación -> Python 3.7.4.
- Librerias -> Numpy, Random
- Desarrollo previo en notebook con Visual Studio Code.


## Autora del juego
 Marta Buesa
 
 
## Esquema del juego


## Indicaciones previas y funcionamiento del juego

1. Hay dos jugadores: el ususario y la maquina
2. Juego con 4 tableros. Los **tableros son de 10 filas x 10 columnas** 
3. La flota consta de:
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora
4. Tanto el usuario como la maquina tienen un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se quede sin barcos, y por tanto, pierda.
5. Funciona por turnos y empiezará el usuario.
6. En cada turno se disparas a una coordenada (fila, columna) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la maquina.
7. En los turnos de la maquina, si acierta, también le vuelve a tocar, y dispara a coordenadas aleatorias del tablero del usuario.
8. **El primero que hunda la flota del contrario gana el juego**.
