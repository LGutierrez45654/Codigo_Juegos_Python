def jugar():
    Num_Seleccionar = ["1", "-8 y -3", "7", "-3", "6", "-5 y -3"]
    Conjunto_numeros = ["2 y 9", "5 y 8"]
    Opciones = ["Universal", "Disconjunto", "Subconjunto"]

    Puntaje_Inicial = 0

    print("------------¡Bienvenidos!. Leá atentamente las consignas y responda correctamente y ganarás puntos.-------")

    # Pregunta 1.
    Pr = input("¿Cuál de estos números ambos son enteros y al menos uno de los suyos es un número par?\n0: 1\n1:-8 y -3\n2: 7\n3:-3\n4: 6\n5:-5 y -3\n")
    if Pr == Num_Seleccionar[1]:
        print("¡Correcto!")
        Puntaje_Inicial += 10
    else:
        print("¡Incorrecto!")

    # Pregunta 2.
    Pr = input("¿Cuál de estos números es un número par y a su vez es un número natural?\n0: 1\n1:-8 y -3\n2: 7\n3:-3\n4: 6\n5:-5 y -3\n")
    if Pr == Num_Seleccionar[4]:
        print("¡Correcto!")
        Puntaje_Inicial += 10
    else:
        print("¡Incorrecto!")

    # Pregunta 3.
    Pr = input("¿Cuál de estos números es un número entero y ambos son impar?\n0: 1\n1:-8 y -3\n2: 7\n3:-3\n4: 6\n5:-5 y -3\n")
    if Pr == Num_Seleccionar[5]:
        print("¡Correcto!")
        Puntaje_Inicial += 10
    else:
        print("¡Incorrecto!")

    # Pregunta 4.
    Pr = input("¿Cuál es la intersección entre el conjunto A y el conjunto B: Si A = {2.3,5,7,9} Y B= {2,4,6,8,9}?\n0: 2 y 9\n1: 5 y 8\n")
    if Pr == Conjunto_numeros[0]:
        print("¡Correcto!")
        Puntaje_Inicial += 10
    else:
        print("¡Incorrecto!")

    # Pregunta 5.
    Pr = input("Si los elementos de un conjunto pertenecen todos a otro conjunto, a este conjunto se le llama\n0: Universal\n1: Disconjunto\n2: Subconjunto\n")
    if Pr == Opciones[0]:  # La respuesta correcta es "Universal"
        print("¡Correcto!")
        Puntaje_Inicial += 10
    else:
        print("¡Incorrecto!")

    # Calificación final
    if Puntaje_Inicial == 50:
        print(f"Finalizó el juego, tu puntaje final es de {Puntaje_Inicial} puntos. ¡Excelente!")
    elif Puntaje_Inicial == 40:
        print(f"Finalizó el juego, tu puntaje final es de {Puntaje_Inicial} puntos. ¡Muy Bien!")
    elif Puntaje_Inicial == 30:
        print(f"Finalizó el juego, tu puntaje final es de {Puntaje_Inicial} puntos. ¡Bien!")
    elif Puntaje_Inicial == 20:
        print(f"Finalizó el juego, tu puntaje final es de {Puntaje_Inicial} puntos. Regular")
    elif Puntaje_Inicial == 10:
        print(f"Finalizó el juego, tu puntaje final es de {Puntaje_Inicial} puntos. Más suerte para la próxima")
    else:
        print(f"Finalizó el juego, tu puntaje final es de {Puntaje_Inicial} puntos. ¿Siquiera te esforzaste?")

# Bucle para preguntar si el usuario quiere seguir jugando
while True:
    jugar()
    continuar = input("¿Quieres seguir jugando? (si/no): ").strip().lower()
    if continuar != "si":
        print("Juego terminado.")
        break


