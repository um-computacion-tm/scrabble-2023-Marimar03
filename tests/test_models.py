import unittest
from game.models import (
    BagTiles,
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


import unittest

class TestBagTiles(unittest.TestCase):
    def test_initialize_tiles(self):
        bag = BagTiles()

        # Verifica que haya 100 fichas en total
        self.assertEqual(len(bag.tiles), 100)
        # Verificar que haya 2 comodines
        self.assertEqual(bag.tile_count['?'], 2)

        #verifica la cantidad de cada letra
        expected_tile_counts = {
            'A': 12, 'B': 2, 'C': 4, 'CH': 1, 'D': 2, 'E': 12, 'F': 1, 'G': 2, 'H': 2,
            'I': 6, 'J': 1, 'L': 4, 'LL': 1, 'M': 2, 'N': 5, 'Ñ': 1, 'O': 8, 'P': 2,
            'Q': 1, 'R': 5, 'RR': 1, 'S': 6, 'T': 4, 'U': 5, 'V': 1, 'X': 1,
            'Y': 1, 'Z': 1,
            }
        for letter, count in expected_tile_counts.items():
            self.assertEqual(bag.tile_count[letter], count)

        #verifica el puntaje de cada letra
        expected_tile_scores = {
            'A': 1, 'B': 3, 'C': 3, 'CH': 5, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
            'I': 1, 'J': 8, 'L': 1, 'LL': 8, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3,
            'Q': 5, 'R': 1, 'RR': 8, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8,
            'Y': 4, 'Z': 10,
        }
        for letter, score in expected_tile_scores.items():
            self.assertEqual(bag.tile_scores[letter], score)

    #lo hizo el profe preguntarle por patch
    @patch('random.shuffle') 
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            5,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )   #lo hizo el profe
    
    
    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            3,
        )
        self.assertEqual(
            len(tiles),
            2,
        )
    
    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            7,
        )

if __name__ == '__main__':
    unittest.main()