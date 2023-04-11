import random
import string
import time

CHARSET = string.ascii_letters + string.digits + string.punctuation + ' '

# Función para generar una palabra aleatoria
def generate_word():
    length = random.randint(5, 15)  # Elegimos una longitud de entre 5 y 15 caracteres
    return ''.join(random.choice(CHARSET) for i in range(length))

# Función para adivinar la palabra
def guess_word(answer):
    start_time = time.time()        # Tomamos el tiempo de inicio
    low = 0
    high = 1000000
    while low <= high:
        mid = (low + high) // 2
        guess = generate_word()
        if guess == answer:
            end_time = time.time()  # Tomamos el tiempo de finalización
            elapsed_time = end_time - start_time   # Calculamos el tiempo transcurrido
            
            # Calculamos la dificultad de la palabra adivinada
            num_guesses = (high - low) / 2
            if num_guesses == 0:
                difficulty = "Muy fácil"
            elif num_guesses < 10:
                difficulty = "Fácil"
            elif num_guesses < 50:
                difficulty = "Normal"
            elif num_guesses < 100:
                difficulty = "Difícil"
            else:
                difficulty = "Muy difícil"
                
            return guess, elapsed_time, difficulty
        elif guess < answer:
            low = mid + 1
        else:
            high = mid - 1

# Pedimos al usuario que introduzca la palabra a adivinar
while True:
    try:
        answer = input("Introduce una palabra (puede contener letras, espacios, números y símbolos): ")
        if all(ch in CHARSET for ch in answer):
            break
        else:
            print("La palabra contiene caracteres inválidos. Inténtalo de nuevo.")
    except Exception as e:
        print("Ocurrió un error:", e)

# Adivinamos la palabra y mostramos el tiempo transcurrido y la dificultad
try:
    guess, elapsed_time, difficulty = guess_word(answer)
    print("La palabra adivinada es:", guess)
    print("Tiempo transcurrido:", elapsed_time, "segundos")
    print("Dificultad:", difficulty)
except TypeError:
    print("Lo siento, no pude adivinar la palabra.")