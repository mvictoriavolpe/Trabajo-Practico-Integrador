# Trabajo-Pr-ctico-Integrador
Tecnicatura Universitaria en Programación
Trabajo Práctico Final – Estructuras de Datos y Python 
Materia: Programación I
Año: 2025
Integrantes del equipo:
Alexia Rubin
María Victoria Volpe


Descripción general
Este trabajo práctico tiene como objetivo aplicar los conocimientos de árboles binarios, listas anidadas y recursividad mediante la creación de dos juegos interactivos. Se trabajó con estructuras lógicas y condicionales, se modelaron decisiones y caminos posibles usando árboles, y se utilizó Python como lenguaje principal para su implementación.

El proyecto incluye:

Un juego de Blackjack simplificado usando un árbol binario de decisiones.

Un test de personalidad tipo revista, que te dice qué tipo de estudiante sos, usando árboles binarios y recorrido recursivo.

Archivos principales
main.py: menú principal del proyecto, permite elegir entre los dos juegos.

blackjack.py: contiene la lógica del juego de Blackjack.

test_estudiante.py: contiene el test de personalidad, estructura de árbol y recorrido recursivo.

README.md: este archivo.

Juego 1: Blackjack con árbol de decisiones
Un clásico juego de cartas donde el jugador arranca con dos cartas y puede pedir más (rama izquierda) o plantarse (rama derecha). Cada decisión recorre el árbol y modifica el estado del juego. Si supera los 21 puntos, pierde.

Temas aplicados:

Árbol binario como lista: [dato, rama_izquierda, rama_derecha]

Condicionales anidados

Uso de funciones auxiliares (sacar_carta, sumar_mano, mostrar_puntuaciones)

Aleatoriedad con random

Lógica de recorrido no recursivo (por decisión del jugador)

Juego 2: ¿Qué tipo de estudiante sos?
Este juego simula un test de personalidad clásico tipo revista, donde cada pregunta lleva a dos posibles respuestas, generando caminos distintos. Al llegar a una hoja del árbol, se revela qué tipo de estudiante sos.

Temas aplicados:

Árbol binario modelado con listas anidadas

Recorrido recursivo

Decisiones binarias

Representación de hojas como resultados finales


Posibles mejoras futuras

Agregar más profundidad a los árboles (más decisiones y resultados).

Incorporar un sistema de puntuación para el test.

Guardar estadísticas de partidas o tipos de estudiantes.



