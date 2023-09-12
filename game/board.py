from game.cell import Cell
from game.bagtiles import Tiles

class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)
        ]

    def calculate_word_value(self, word):
        total_value = 0
        for row in self.grid:
            for cell in row:
                if cell.letter:
                    letter_value = cell.letter.value
                    total_value += letter_value
        return total_value

    def validate_word_inside_board(self, word, location, orientation):
        if orientation == "H":
            return len(word) <= len(self.grid) - location[0]
        else:
            return len(word) <= len(self.grid) - location[1]
        
    def word_out_of_board(self):
        pass

    def validate_len_of_word(self, word, location, orientation):
        pass