import unittest
from game.board import Board
from game.bagtiles import Tile

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

    def test_board_is_empty(exception): # OK
        board = Board()
        board.board_is_empty() == True 

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
        
if __name__ == '__main__':
    unittest.main()