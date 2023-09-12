from game.cell import Cell
from game.bagtiles import Tiles


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]

def calculate_word_value:(self):
total_value = 0
for cell in word:
    letter_value = cell.letter.value
    total_value += letter_value
return total_value  

def word_inside_board(self):
    pass

def word_out_of_board(self):
    pass

def validate_len_of_word(self, word, location, orientation):
    pass