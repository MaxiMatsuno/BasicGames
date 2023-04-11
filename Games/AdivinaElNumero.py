import random

print("¡Bienvenido a Adivina el número!")
numero = random.randint(1, 100)

while True:
    try:
        intento = int(input("Ingresa un número entre 1 y 100: "))
    except:
        print("Debes ingresar un número")
        continue
    
    if intento < 1 or intento > 100:
        print("El número debe estar entre 1 y 100")
        continue
    
    if intento == numero:
        print("¡Correcto! ¡Has adivinado el número!")
        break
    
    if intento < numero:
        print("El número es más grande")
    else:
        print("El número es más pequeño")

print("¡Gracias por jugar!")