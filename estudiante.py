# Supongamos que este es el árbol de decisiones del test de personalidad
# Estructura: [pregunta, rama_izquierda (sí), rama_derecha (no)]

test_arbol = [
    "¿Te gusta estudiar en grupo?",
    [
        "¿Preferís materias prácticas?",
        "Sos un estudiante colaborativo y práctico.",
        "Sos un estudiante colaborativo, pero te va mejor con lo teórico."
    ],
    [
        "¿Sos muy organizado con tus tiempos?",
        "Sos un estudiante independiente y metódico.",
        "Sos un estudiante creativo y espontáneo."
    ]
]

# --- Función recursiva mejorada para recorrer el árbol y guardar el camino ---
def recorrer_arbol(nodo, camino=None, nivel=0):
    if camino is None:
        camino = []

    if isinstance(nodo, str):
        print("\n🔍 Resultado final:")
        print(f"→ {nodo}")
        print("\n📍 Camino recorrido:")
        for i, paso in enumerate(camino):
            print(f"Nivel {i}: {paso[0]} → {paso[1]}")
        print(f"\n📏 Profundidad total del nodo hoja: {len(camino)}")
        return

    pregunta, izq, der = nodo
    print("\n" + "—" * 40)
    print(f"{'  '*nivel}❓ {pregunta}")
    respuesta = input(f"{'  '*nivel}▶ (s/n): ").lower()

    if respuesta == "s":
        camino.append((pregunta, "Sí"))
        recorrer_arbol(izq, camino, nivel + 1)
    else:
        camino.append((pregunta, "No"))
        recorrer_arbol(der, camino, nivel + 1)

# --- Función para contar nodos del árbol (peso total) ---
def contar_nodos(nodo):
    if isinstance(nodo, str):
        return 1
    pregunta, izq, der = nodo
    return 1 + contar_nodos(izq) + contar_nodos(der)

# --- Función para visualizar el árbol completo con indentación ---
def mostrar_arbol(nodo, nivel=0):
    if isinstance(nodo, str):
        print("  " * nivel + f"🔹 Resultado: {nodo}")
    else:
        pregunta, izq, der = nodo
        print("  " * nivel + f"🔸 Pregunta: {pregunta}")
        mostrar_arbol(izq, nivel + 1)
        mostrar_arbol(der, nivel + 1)

# Ejecutar una demo (en tu programa principal se llamaría con input del usuario)
# mostrar_arbol(test_arbol)
# recorrer_arbol(test_arbol)
# print("🧮 Peso total del árbol:", contar_nodos(test_arbol))
"Funciones añadidas al código: recorrido mejorado, camino, profundidad, visualización y peso del árbol."