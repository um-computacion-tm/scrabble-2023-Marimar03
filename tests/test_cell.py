import unittest
from game.cell import Cell
from game.bagtiles import Tile
from game.board import Board

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type = 'letter')
        self.assertEqual(cell.multiplier,2,)
        self.assertEqual(cell.multiplier_type,'letter',)
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0,)

    def test_add_letter(self):
        cell = Cell(multiplier = 1, multiplier_type = '')
        letter = Tile(letter = 'C', value = 3)
        cell.add_letter(letter = letter)
        self.assertEqual(cell.letter, letter)


    def test_cell_letter_multiplier(self): #OK
        cell = Cell(multiplier = 2, multiplier_type = 'letter')
        letter = Tile(letter = 'C', value = 3)
        cell.add_letter(letter = letter)
        self.assertEqual(cell.calculate_value(),6,)
        
    def test_cell_word_multiplier(self): #OK
        cell_1 = Cell(multiplier = 1, multiplier_type = 'letter')
        cell_1.add_letter(Tile('H', 4)) 
        cell_2 = Cell(multiplier = 1, multiplier_type = 'letter')
        cell_2.add_letter(Tile('O', 1))
        cell_3 = Cell(multiplier = 3, multiplier_type = 'word')
        cell_3.add_letter(Tile('L', 1))
        cell_4 = Cell(multiplier = 1, multiplier_type = 'letter')
        cell_4.add_letter(Tile('A', 1))
        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value,21)
    
    def test_cell_letter_n_word_multiplier(self): #OK
        cell_1 = Cell(multiplier = 2, multiplier_type = 'letter')
        cell_1.add_letter(Tile('H', 4)) 
        cell_2 = Cell(multiplier = 1, multiplier_type = 'letter')
        cell_2.add_letter(Tile('O', 1))
        cell_3 = Cell(multiplier = 3, multiplier_type = 'word')
        cell_3.add_letter(Tile('L', 1))
        cell_4 = Cell(multiplier = 1, multiplier_type = 'letter')
        cell_4.add_letter(Tile('A', 1))
        word = [cell_1, cell_2, cell_3, cell_4]
        value=Board().calculate_word_value(word)
        self.assertEqual(value,33)

    def test_cell_multiplier_desactivate(self): #OK
        cell_1 = Cell(multiplier=1,multiplier_type='letter')
        cell_1.add_letter(Tile('H', 4)) 
        cell_2 = Cell(multiplier=1,multiplier_type='letter')
        cell_2.add_letter(Tile('O', 1))
        cell_3 = Cell(multiplier=3,multiplier_type='word')
        cell_3.add_letter(Tile('L', 1))
        cell_4 = Cell(multiplier=1,multiplier_type='letter')
        cell_4.add_letter(Tile('A', 1))
        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value,21)
        value2=Board().calculate_word_value(word)
        self.assertEqual(value2,7)

if __name__ == '__main__':
    unittest.main()