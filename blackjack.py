import random
#Arbol binario donde cada rama presenta una decisión: pedir carta o plantarse

arbol_juego = [
    "Empezar juego",
    ["Pedir carta", 
        ["Pedir carta", 
            ["Pedir carta", ["Pedir carta", [], []], ["Plantarse", [], []]], 
            ["Plantarse", [], []]
        ], 
        ["Plantarse", [], []]
    ],
    ["Plantarse", [], []]
]



palos= ["♥", "♦", "♣", "♠"]
cartas= [1,2,3,4,5,6,7,8,9,10]


mano = [] #guardo y acumulo puntos de usuario

def sacar_carta(): #función para sacar cartas aleatorias
    carta_random = random.choice(cartas)
    palo_random = random.choice(palos)
    carta_str = f"{carta_random} {palo_random}"
    mano.append(carta_random) 
    return carta_str

def sumar_mano():
    return sum(mano)


def recorrer_arbol(arbol_juego, primera_mano=False):

    if arbol_juego[1]==[] and arbol_juego[2]==[]: # caso de corte para la recursión
        print("\n🛑 No hay más nodos.\n")
    
    else:
        if primera_mano:
            print(f"\n🎲 {arbol_juego[0]}") 
            print(f"Te tocó {sacar_carta()} y un {sacar_carta()}.")

        print(f"Puntos totales: {sumar_mano()}.") #sumo las cartas de la mano.
        empezar=input(f"¿Quieres pedir otra carta (1)?, o 'Plantarte'(2)? ")

        if empezar == "1": 
            print(f"Te tocó un {sacar_carta()}.")

            if sumar_mano()>21: #verifica si se pasa de 21
                print(f"💥 ¡Te pasaste! Perdiste con {sumar_mano()} puntos.")
                return

            recorrer_arbol(arbol_juego[1]) #Al recorrer recursivamente va a ir sacando cartas y sumándolas.

        elif empezar == "2":
            print(f"Te plantaste con {sumar_mano()} puntos.")
            mostrar_puntuaciones(sumar_mano())

##Simulando que la casa ""juega".
#función que genere un valor entre 15 y 22 para simular partida de la casa.
def puntos_de_la_casa():
    return random.randint(15,22)

def mostrar_puntuaciones(puntos):
    casa = puntos_de_la_casa() #guardo el valor de la función en la variable casa, asi no la llamo ochenta veces.
    print(f"La casa hizo {casa} puntos.")
    if casa>21: print(f"Ganaste! la casa se pasó con {casa}")
    if puntos > 21: print(f"Te pasaste con {puntos}")
    elif puntos > casa: print(f"Ganaste con {puntos}")
    elif puntos == casa: print("Empate. La casa gana")
    else: print(f"Perdiste con {puntos}")

def jugar_blackjack():
    while True:
        mano.clear()  # Vaciar la mano antes de cada nuevo juego
        recorrer_arbol(arbol_juego, primera_mano=True)  # Iniciar un nuevo juego

        while True:
            respuesta = input("¿Querés jugar otra vez? (si/no): ").lower()
            if respuesta == "si":
                break  # salir del bucle interno y volver a jugar
            elif respuesta == "no":
                print("¡Gracias por jugar!")
                return  # salir por completo
            else:
                print("Entrada no válida. Por favor responde 'si' o 'no'.")


#analisis del arbol

def contar_nodos(arbol):
    if arbol == []:
        return 0
    return 1 + contar_nodos(arbol[1]) + contar_nodos(arbol[2])

def calcular_altura(arbol):
    if arbol == []:
        return 0
    return 1 + max(calcular_altura(arbol[1]), calcular_altura(arbol[2]))

def contar_hojas(arbol):
    if arbol[1] == [] and arbol[2] == []:
        return 1
    return contar_hojas(arbol[1]) + contar_hojas(arbol[2])


print("\n📊 Análisis del árbol:")
print(f"- Nodos totales: {contar_nodos(arbol_juego)}")     
print(f"- Altura del árbol: {calcular_altura(arbol_juego)}")  
print(f"- Total de hojas: {contar_hojas(arbol_juego)}")   



