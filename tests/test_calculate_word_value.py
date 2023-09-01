import unittest
from game.board import calculate_word_value
from game.cell import Cell
from game.bagtiles import Tiles


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(letter=Tiles('C', 1)),
            Cell(letter=Tiles('A', 1)),
            Cell(letter=Tiles('S', 2)),
            Cell(letter=Tiles('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        word = [
            Cell(letter=Tiles('C', 1)),
            Cell(letter=Tiles('A', 1)),
            Cell(
                letter=Tiles('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tiles('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tiles('C', 1)),
            Cell(letter=Tiles('A', 1)),
            Cell(
                letter=Tiles('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tiles('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tiles('C', 1)
            ),
            Cell(letter=Tiles('A', 1)),
            Cell(letter=Tiles('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tiles('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_multiplier_no_active(self):
        word = [
            Cell(letter=Tiles('C', 1)),
            Cell(letter=Tiles('A', 1)),
            Cell(
                letter=Tiles('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tiles('A', 1)),
        ]
        for index in range(4):
            word[index].active = False

        value = calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_word_multiplier_no_active(self):
        word = [
            Cell(letter=Tiles('C', 1)),
            Cell(letter=Tiles('A', 1)),
            Cell(
                letter=Tiles('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tiles('A', 1)),
        ]
        for index in range(4):
            word[index].active = False
        
        value = calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tiles('C', 1)
            ),
            Cell(letter=Tiles('A', 1)),
            Cell(
                letter=Tiles('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tiles('A', 1)),
        ]
        for index in range (4): #2da opcion
            word[index].active = False
        
        value = calculate_word_value(word)
        self.assertEqual(value, 5)

if __name__ == '__main__':
    unittest.main()