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

