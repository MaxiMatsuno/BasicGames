import random

def juego():
    opciones = ['piedra', 'papel', 'tijeras']
    puntaje_usuario = 0
    puntaje_computadora = 0
    
    while True:
        # Preguntar al usuario su elección
        eleccion_usuario = input("Elige entre Piedra, papel o tijeras o (escribe 'salir' para terminar): ").lower()
        if eleccion_usuario == 'salir':
            break
        elif not eleccion_usuario.isalpha() or eleccion_usuario not in opciones:
            print("Opción inválida, por favor digite una de las opciones dadas")
            continue

        # Elegir la elección de la computadora
        eleccion_computadora = random.choice(opciones)
        print("La computadora eligió: " + eleccion_computadora)
        
        # Verificar el resultado
        if eleccion_usuario == eleccion_computadora:
            print("Empate")
        elif eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras':
            print("¡Ganaste!")
            puntaje_usuario += 1
        elif eleccion_usuario == 'papel' and eleccion_computadora == 'piedra':
            print("¡Ganaste!")
            puntaje_usuario += 1
        elif eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel':
            print("¡Ganaste!")
            puntaje_usuario += 1
        else:
            print("¡La computadora ganó!")
            puntaje_computadora += 1
        
        # Imprimir el puntaje
        print("Puntaje: Tú: {}, Computadora: {}".format(puntaje_usuario, puntaje_computadora))

# Iniciar el juego
juego()