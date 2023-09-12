def main():
    print("Bienvenido")
    try:
        players_count = int(input("Ingrese la cantidad de jugadores"))
        if players_count <= 1 or players_count > 4:
            raise ValueError 
    except ValueError:
        print("Valor invalido")
    scrabble_game = ScrabbleGame(players_count)