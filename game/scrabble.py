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
        player1.draw_tiles(self bag_of_tiles.take(7))
        player2.draw_tiles(self bag_of_tiles.take(7))
        print(f"{player1.name}: {player1.get_tiles()}")
        print(f"{player2.name}: {player2.get_tiles()}")

    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player(bag_tiles=self.bag_tiles))
        
        self.current_player = None
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif:
            #index = index del current player + 1
            #len(self.players)
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]
