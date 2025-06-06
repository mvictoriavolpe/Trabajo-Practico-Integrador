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
    carta_random = random.choice(cartas)
    palo_random = random.choice(palos)
    carta_str = f"{carta_random} {palo_random}"
    mano.append(carta_random) 
    return carta_str

def sumar_mano():
    return sum(mano)

def recorrer_arbol(arbol_juego, primera_mano=False):
    if arbol_juego[1]==[] and arbol_juego[2]==[]: #condición para detectar hojas #además es el caso de corte para la recursión
        print("\n🛑 No hay más nodos.\n")
    
    else:
        if primera_mano:
            print(f"\n🎲 {arbol_juego[0]}") #si es la primera mano imprimo el nodo padre y reparto 2
            print(f"Te tocó {sacar_carta()} y un {sacar_carta()}.")

        print(f"Puntos totales: {sumar_mano()}.\n") #sumo las cartas de la mano.
        empezar=input(f"¿Quieres pedir otra carta (1)?, o 'Plantarte'(2)? ")

        if empezar == "1": #si el usuario "pide" carta:
            print(f"\n Te tocó un {sacar_carta()}.\n") #saca 1

            if sumar_mano()>21: #verifica si se pasa de 21
                print(f"💥 ¡Te pasaste! \nPerdiste con {sumar_mano()} puntos.\n")
                return

            recorrer_arbol(arbol_juego[1]) #recorro recursivamente el subárbol izquierdo. Al recorrer recursivamente va a ir sacando cartas y sumándolas.

        elif empezar == "2":
            print(f"\n Te plantaste con {sumar_mano()} puntos.\n")
            recorrer_arbol(arbol_juego[2]) #recorro el subárbol derecho (plantarse). -->para qué? si en plantarse termina.?

recorrer_arbol(arbol_juego, primera_mano=True)
