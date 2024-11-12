import random

def juego_adivinar():
    while True:  # Añadimos un ciclo para repetir el juego si el jugador lo desea
        numero_secreto = random.randint(1, 100)  # Corregir el rango
        intentos = 0
        limite_intentos = 10

        print("\nBienvenido al juego de adivinanzas")
        print(f"Adivina el número entre 1 y 100. Tienes {limite_intentos} intentos.")

        while intentos < limite_intentos:
            intentos += 1
            intento = int(input(f"Intento {intentos}: "))  # Mejorar la legibilidad de la solicitud

            if intento < numero_secreto:
                print("Demasiado bajo.")
            elif intento > numero_secreto:
                print("Demasiado alto.")
            else:
                print(f"¡Perfecto! Lo has adivinado en {intentos} intentos.")
                break  # Termina el juego si adivina correctamente

        if intentos >= limite_intentos and intento != numero_secreto:
            print(f"¡Has perdido!, has agotado tus {limite_intentos} intentos. El número secreto era {numero_secreto}.")
        
        # Preguntar al jugador si desea jugar de nuevo
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (sí/no): ").strip().lower()
        if jugar_de_nuevo != "si":
            print("Fin del Juego")
            break  # Termina el ciclo del juego si el jugador no quiere jugar de nuevo

# Ejecutar el juego
juego_adivinar()
