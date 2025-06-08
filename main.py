#Incorporamos un menú inicial 
from  blackjack import jugar_blackjack

def menu():
    while True:
        print("\n ***MENÚ PRINCIPAL***")
        print("1. Jugar al Blackjack")
        print("2. Test: ¿Qué tipo de estudiante sos?")
        print("3. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            jugar_blackjack()
        elif opcion == "2":
            jugar_test_personalidad()
        elif opcion == "3":
            print("👋 ¡Gracias por jugar!")
            break
        else:
            print("❌ Opción inválida. Probá de nuevo.")

if __name__ == "__main__":
    menu()