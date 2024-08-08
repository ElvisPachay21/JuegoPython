from random import randint


def update_score(score, die_value):
    if die_value == 1:
        return 0
    else:
        return score + die_value

def display_scoreboard(player_score, computer_score):
    print()
    print("#" * 20)
    print(f"Puntuación del Jugador: {player_score}")
    print(f"Puntuación de la Computadora: {computer_score}")
    print("#" * 20)
    print()

welcome_message = """
Bienvenido a 'Cerdo', un juego de dados!

En este juego, un usuario y un oponente computarizado
lanzan un dado de 6 caras en cada ronda. Si el valor del
dado es 1, el jugador que lanzó el dado pierde todos sus puntos.
De lo contrario, el jugador suma el valor del dado a sus puntos.
¡El primer jugador en alcanzar 30 puntos gana!
"""
print(welcome_message)


username = input("¿Cuál es tu nombre? ")

player_score = 0
computer_score = 0

while True:
    input(f"Presiona 'Enter' para lanzar el dado, {username}!\n")
    player_die_value = randint(1, 6)
    print(f"{username} lanza un {player_die_value}")
    
    computer_die_value = randint(1, 6)
    print(f"La computadora lanza un {computer_die_value}")

    player_score = update_score(player_score, player_die_value)
    computer_score = update_score(computer_score, computer_die_value)

    display_scoreboard(player_score, computer_score)

    if player_score >= 30:
        print(f"¡{username} gana!")
        break
    elif computer_score >= 30:
        print("¡La computadora gana!")
        break