import random
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

categories = {"lenguajes": ["pyton"],
              "datos": ["cadena", "entero"],
              "estructuras": ["lista"],
              "palabras clave": ["programa", "variable", "funcion", "bucle"]
}

points = 0

print("¡Bienvenido al Ahorcado!")
print()

for elem in categories:
    print(elem)

print()

category = input("Elegi la categoria ")

while category not in categories:
    print("La categoria no existe, elegi otra")
    category = input("Elegi la categoria ")
word = random.choice(categories[category])

word_pool = random.sample(categories[category], len(categories[category])) ##Me devuelve las palabras dentro de esa categoria pero sin repetir

for word in word_pool:
    print("Nueva ronda")
    print()

    guessed = [] #Movi esto adentro del for para que al iniciar cada ronda se reseteen y no quede lo de la ronda anterior
    attempts = 6

    while (attempts > 0):
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        if "_" not in progress:
            points += 6
            print("!Ganaste!")
            print(f"Tus puntos son: {points}")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
    
        letter = input("Ingresa una letra: ")
    
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif len(letter) != 0 | (letter.lower() >= "a" and letter.lower() <= "z"):
            print("Entrada no valida")
        elif letter in word:
            guessed.append(letter)
            print("!Bien¡ Esa letra esta en la palabra.")
        else:
            guessed.append(letter)
            attempts -=1
            points -= 1
            print("Esa letra no esta en la palabra.")
        
        print()
    else:
        print(f"!Perdiste¡ La palabra era {word}")
        print(f"Tus puntos son: 0")
