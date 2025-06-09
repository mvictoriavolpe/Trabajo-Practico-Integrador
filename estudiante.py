# Cada nodo tiene: [Pregunta o Resultado, Rama Izquierda (respuesta 1), Rama Derecha (respuesta 2)]
arbol_estudiante = [
    #Primera pregunta raiz para dividir entre dos tipos de estudiantes
    "¿Te organizas para estudiar?",
    [  # izquierda = opción 1 = SI
        "¿Te organizás con un horario fijo?",
        ["Sos un/a estudiante ORGANIZADO/A ", [], []],
        ["Sos un/a estudiante RESPONSABLE pero IMPROVISADOR/A ", [], []]
    ],
    [  # derecha = opción 2 = NO
        "¿Te cuesta mantener la atención?",
        ["Sos un/a estudiante ANSIOSO/A ", [], []],
        ["Sos un/a estudiante RELAJADO/A ", [], []]
    ]
]
def recorrer_test(arbol):
    if arbol[1] == [] and arbol[2] == []:
        print(f"\n Resultado: {arbol[0]}")
        return

    print(f"\n {arbol[0]}")
    print("Opción 1) SI")
    print("Opción 2) NO")
    eleccion = input("Elegí 1 o 2: ")

    if eleccion == "1":
        recorrer_test(arbol[1])
    elif eleccion == "2":
        recorrer_test(arbol[2])
    else:
        print(" Entrada inválida. Probá de nuevo.")
        recorrer_test(arbol)  # Reintento

def test_estudiante():
    print("***Que tipo de estudiante sos***")
    recorrer_test(arbol_estudiante)