import random
#Arbol binario donde cada rama presenta una decisión: pedir carta o plantarse
arbol_juego = [
    "Empezar juego", #nodo padre, empieza el juego y reparte (A) 2 cartas.
    ["Pedir carta", #nodo izq. Pedir carta
        ["Pedir carta",
            ["Pedir carta", [], []],
            ["Plantarse", [], []]
        ],
        ["Plantarse", [], []]
    ],
    ["Plantarse", [], []] #nodo derecho se planta.
]
palos= ["♥", "♦", "♣", "♠"]
cartas= [1,2,3,4,5,6,7,8,9,10]

#Recorrer el arbol para ver que funciona 
""" Estoy en: Empezar juego
1. Ir a la izquierda: Pedir carta
2. Ir a la derecha: Plantarse
Elegí:   
Nodo padre: Primero deberia empezar el juego y repartir 2 cartas.
Hijo izquierdo: Pide carta
HIjo derecho: se planta, no más nodos.
Podria considerarse que sigue la lógica de preorder creo.
 """

def recorrer_arbol(arbol_juego):
    if arbol_juego[1]==[] and arbol_juego[2]==[]: #condición para detectar hojas #además es el caso de corte para la recursión
        print("No hay mas nodos")
    else:
        print(arbol_juego[0]) #imprime el nodo actual. -->empezar juego
        empezar=input(f"Tus cartas son: {(random.choice(cartas)),(random.choice(cartas))}. Puntos totales: (aca iria una funcion que suma). \n ¿Quieres pedir otra (1) carta o plantarte (2?")
        if empezar==1: 
            arbol_juego[1]
            print("Te tocó un (carta). Puntaje total:\n Pedir(1) o Plantarse(2)?")


recorrer_arbol(arbol_juego)