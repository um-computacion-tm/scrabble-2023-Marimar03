from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(players_count):
            self.players.append(Player(id=index, bag_tiles=self.bag_tiles))
        self.current_player = None
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def validate_word(self, word, location, orientation):
            self.board.validate_word_inside_board(word, location, orientation)
    
    def get_words():
        pass
       
    def put_words():
        pass
