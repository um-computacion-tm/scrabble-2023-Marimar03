import unittest
from game.board import Board
from game.bagtiles import Tile
from game.cell import Cell

class TestBoard(unittest.TestCase): 
    def test_init(self): #OK
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    
    def test_calculate_word_value(self): #NOT OK
        # Crear celdas para la palabra de prueba
        cell1 = Cell(3, 'C')
        cell2 = Cell(1, 'A')
        cell3 = Cell(1, 'S')
        cell4 = Cell(1, 'A')
        word = [cell1, cell2, cell3, cell4]

        # Crear un objeto de la clase Board
        board = Board()

        # Calcular el valor de la palabra y verificar el resultado
        result = board.calculate_word_value(word)
        self.assertEqual(result, 3 + 1 + 1 + 1)
        
    
    def test_word_inside_board(self): #OK
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
        
    def test_word_out_of_board(self): #OK
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False

    def test_board_is_empty(self):
        board = Board()
        assert board.board_is_empty == True

    def test_board_is_not_empty(self): #OK
        board = Board()
        board.grid[7][7].add_letter(Tile("A", 1))
        assert board.board_is_empty() == False

    def test_len_of_word_in_board_x(self): #OK
        board= Board()
        word="facultad"
        location=(5,4)
        orientation='H'
        self.assertEqual(board.validate_len_of_word_in_board(self, word, location, orientation),True)

    def test_len_of_word_in_board_y(self): #OK
        board= Board()
        word="facultad"
        location=(5,4)
        orientation='H'
        self.assertEqual(board.validate_len_of_word_in_board(self, word, location, orientation),True)

    def test_len_of_word_out_of_board_x(self): #OK
        board = Board()
        word = 'facultad'
        location = (10,5)
        orientation = 'H'
        self.assertEqual(board.validate_len_of_word_in_board(self,word,location,orientation),False)

    def test_len_of_word_out_of_board_y(self): #OK
        board = Board()
        word = 'facultad'
        location = (5,10)
        orientation ='V'
        self.assertEqual(board.validate_len_of_word_in_board(self,word,location,orientation),False)

    def test_show_board(self): #OK
        board = Board()
        board.show_board()
        
    def test_show_board_with_word(self): #OK
        board = Board()
        board.grid[7][7].letter = Tile('h',4)
        board.grid[7][8].letter = Tile('o',1)
        board.grid[7][9].letter = Tile('l',1)
        board.grid[7][10].letter = Tile('a',1)

    def test_show_board_with_words(self): #OK
        "1ra palabra"
        board = Board()
        board.grid[7][7].letter = Tile('h',4)
        board.grid[7][8].letter = Tile('o',1)
        board.grid[7][9].letter = Tile('l',1)
        board.grid[7][10].letter = Tile('a',1)
        "2da palabra"
        board = Board()
        board.grid[7][7].letter = Tile('h',4)
        board.grid[8][7].letter = Tile('o',1)
        board.grid[9][7].letter = Tile('l',1)
        board.grid[10][7].letter = Tile('a',1)

if __name__ == '__main__':
    unittest.main()