from game.cell import Cell
class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)]

    def calculate_word_value(self, word):
        value = 0
        for cell in word:
            value += cell.calculate_value()
        for cell in word:
            if cell.multiplier_type == 'word':
                value *= cell.multiplier
                cell.multiplier = 1
        return value

    def validate_word_inside_board(self, word, location, orientation):
        if orientation == "H":
            return len(word) <= len(self.grid) - location[0]
        else:
            return len(word) <= len(self.grid) - location[1]

        
    def word_out_of_board(self, word, location, orientation):
        if orientation == "H":
            if len(word) > len(self.grid) - location[0]:
                return False 
            for i in range(len(word)):
                if self.grid[location[0] + i][location[1]].value != '':
                    return False 
        else: 
            if len(word) > len(self.grid) - location[1]:
                return False 
            for i in range(len(word)):
                if self.grid[location[0]][location[1] + i].value != '':
                    return False
        return True
    
    def validate_word_place_board(self, word, location, orientation):
        pass 

    def board_is_empty(self):
        for row in self.grid:
            for tile in row:
                if tile is not None:
                    return False
        return True
    @staticmethod

    def validate_len_of_word_in_board(self, word, location, orientation):
        location_x = location[0]
        location_y = location[1]
        len_word = len(word)
        if orientation == 'H':
            if location_x + len_word > 15:
                return False
            else:
                return True
        else:
            if location_y + len_word > 15:
                return False
            else:
                return True