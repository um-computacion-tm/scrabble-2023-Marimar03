import unittest

from game.bagtiles import (
    BagTiles,
    Tiles,
)
from unittest.mock import patch

class TestBagTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tiles('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('E', 1)
        self.assertEqual(tile.letter, 'E')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('I', 1)
        self.assertEqual(tile.letter, 'I')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('L', 1)
        self.assertEqual(tile.letter, 'L')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('N', 1)
        self.assertEqual(tile.letter, 'N')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('O', 1)
        self.assertEqual(tile.letter, 'O')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('R', 1)
        self.assertEqual(tile.letter, 'R')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('S', 1)
        self.assertEqual(tile.letter, 'S')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('T', 1)
        self.assertEqual(tile.letter, 'T')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('U', 1)
        self.assertEqual(tile.letter, 'U')
        self.assertEqual(tile.value, 1)
    def test_tile(self):
        tile = Tiles('D', 2)
        self.assertEqual(tile.letter, 'D')
        self.assertEqual(tile.value, 2)
    def test_tile(self):
        tile = Tiles('G', 2)
        self.assertEqual(tile.letter, 'G')
        self.assertEqual(tile.value, 2)
    def test_tile(self):
        tile = Tiles('B', 3)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 3)
    def test_tile(self):
        tile = Tiles('C', 3)
        self.assertEqual(tile.letter, 'C')
        self.assertEqual(tile.value, 3)
    def test_tile(self):
        tile = Tiles('M', 3)
        self.assertEqual(tile.letter, 'M')
        self.assertEqual(tile.value, 3)
    def test_tile(self):
        tile = Tiles('P', 3)
        self.assertEqual(tile.letter, 'P')
        self.assertEqual(tile.value, 3)
    def test_tile(self):
        tile = Tiles('F', 4)
        self.assertEqual(tile.letter, 'F')
        self.assertEqual(tile.value, 4)
    def test_tile(self):
        tile = Tiles('H', 4)
        self.assertEqual(tile.letter, 'H')
        self.assertEqual(tile.value, 4)
    def test_tile(self):
        tile = Tiles('V', 4)
        self.assertEqual(tile.letter, 'V')
        self.assertEqual(tile.value, 4)
    def test_tile(self):
        tile = Tiles('Y', 4)
        self.assertEqual(tile.letter, 'Y')
        self.assertEqual(tile.value, 4)
    def test_tile(self):
        tile = Tiles('Q', 5)
        self.assertEqual(tile.letter, 'Q')
        self.assertEqual(tile.value, 5)
    def test_tile(self):
        tile = Tiles('J', 8)
        self.assertEqual(tile.letter, 'J')
        self.assertEqual(tile.value, 8)    
    def test_tile(self):
        tile = Tiles('Ñ', 8)
        self.assertEqual(tile.letter, 'Ñ')
        self.assertEqual(tile.value, 8)   
    def test_tile(self):
        tile = Tiles('X', 8)
        self.assertEqual(tile.letter, 'X')
        self.assertEqual(tile.value, 8)
    def test_tile(self):
        tile = Tiles('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)    
    def test_tile(self):
        tile = Tiles('CH', 5)
        self.assertEqual(tile.letter, 'CH')
        self.assertEqual(tile.value, 5)
    def test_tile(self):
        tile = Tiles('LL', 8)
        self.assertEqual(tile.letter, 'LL')
        self.assertEqual(tile.value, 8)
    def test_tile(self):
        tile = Tiles('RR', 8)
        self.assertEqual(tile.letter, 'RR')
        self.assertEqual(tile.value, 8)
    def test_tile(self):
        tile = Tiles('?', 0)
        self.assertEqual(tile.letter, '?')
        self.assertEqual(tile.value, 0)
    #lo hizo el profe preguntarle por patch
    @patch('random.shuffle') 
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
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
        tiles = bag.take(7)
        self.assertEqual(
            len(bag.tiles),
            93,
        )
        self.assertEqual(
            len(tiles),
            7,
        )
    
    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tiles('?', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            101,
        )

class TestPlayer(unittest.TestCase):
    def test_init(self):
        pass

if __name__ == '__main__':
    unittest.main()