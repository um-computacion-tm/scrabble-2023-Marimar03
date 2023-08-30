from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles
class ScrabbleGame:
    def _init_(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())
        player1 = Player("Jugador 1")
        player2 = Player("Jugador 2")
        player1.draw_tiles(bag_of_tiles.take(7))
        player2.draw_tiles(bag_of_tiles.take(7))
        print(f"{player1.name}: {player1.get_tiles()}")
        print(f"{player2.name}: {player2.get_tiles()}")