import unittest
from game.cell import Cell
from game.bagtiles import Tile

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type = 'letter')
        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value_letter(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier = 1, multiplier_type = '')
        letter = Tile(letter = 'C', value = 3)

        cell.add_letter(letter = letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier = 2, multiplier_type = 'letter')
        letter = Tile(letter = 'C', value = 3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value_letter(),6,)


if __name__ == '__main__':
    unittest.main()