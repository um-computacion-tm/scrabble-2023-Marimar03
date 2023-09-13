import unittest
from game.board import Board
from game.bagtiles import Tiles

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
        
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False

    def test_board_is_empty_(self):
        board = Board
        assert board.is_empty == True 

    def test_board_is_not_empty_(self):
        board = Board
        assert board.is_empty == False 

    def test_word_on_empty_board_horizontal_fine(self):
        board = Board()
        word = "FACULTAD"
        location = (7,4)
        orientation = "H"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == True
    
    def test_word_on_empty_board_horizontal_wrong(self):
        board = Board()
        word = "FACULTAD"
        location = (2,4)
        orientation = "H"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == False

    def test_word_on_empty_board_vertical_fine(self):
        board = Board()
        word = "FACULTAD"
        location = (4,7)
        orientation = "V"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == True

    def test_word_on_empty_board_vertical_wrong(self):
        board = Board()
        word = "FACULTAD"
        location = (2,4)
        orientation = "V"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == False

    def test_word_on_not_empty_board_vertical_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tiles("C",1))
        board.grid[8][7].add_letter(Tiles("A",1))
        board.grid[9][7].add_letter(Tiles("S",1))
        board.grid[10][7].add_letter(Tiles("A",1))
        word = "FACULTAD"
        location = (8,6)
        orientation = "V"
        word_is_valid = board.validate_word_place_word(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_not_empty_board_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tiles('C', 1))
        board.grid[7][8].add_letter(Tiles('A', 1)) 
        board.grid[7][9].add_letter(Tiles('S', 1)) 
        board.grid[7][10].add_letter(Tiles('A', 1)) 
        word = "Facultad"
        location = (8, 6)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

if __name__ == '__main__':
    unittest.main()