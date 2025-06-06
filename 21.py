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

mano = [] #acá voy a guardar las cartas de los jugadores y acumular sus puntos.

def sacar_carta(): #función para sacar cartas aleatorias
    carta_random=random.choice(cartas)
    mano.append(carta_random) 
    return(carta_random)

def sumar_mano():
    return sum(mano)


def recorrer_arbol(arbol_juego, primera_vez=False):
    if arbol_juego[1]==[] and arbol_juego[2]==[]: #condición para detectar hojas #además es el caso de corte para la recursión
        print("No hay mas nodos")
    
    else:
        if primera_vez:
            print(arbol_juego[0]) #si es la primera mano imprimo el nodo padre y reparto 2
            sacar_carta()
            sacar_carta()

        print(f"Puntos totales: {sumar_mano()}.") #sumo las cartas de la mano.
        empezar=input(f"¿Quieres pedir otra carta (1)?, o 'Plantarte'(2)?")
        
        if empezar == "1": #si el usuario "pide" carta:
            print(f"Te tocó un {sacar_carta()}.")
            recorrer_arbol(arbol_juego[1]) #recorro recursivamente el subárbol izquierdo

        elif empezar == "2":
            recorrer_arbol(arbol_juego[2]) #recorro el subárbol derecho (plantarse)
            
recorrer_arbol(arbol_juego, primera_vez=True)
