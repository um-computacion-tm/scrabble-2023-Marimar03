import unittest

from game.bagtiles import (BagTiles, Tile)
from unittest.mock import patch

class TestTiles(unittest.TestCase):
   
    def test_tiles(self): #OK
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('E', 1)
        self.assertEqual(tile.letter, 'E')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('O', 1)
        self.assertEqual(tile.letter, 'O')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('I', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('S', 1)
        self.assertEqual(tile.letter, 'S')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('N', 1)
        self.assertEqual(tile.letter, 'N')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('L', 1)
        self.assertEqual(tile.letter, 'L')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('R', 1)
        self.assertEqual(tile.letter, 'R')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('U', 1)
        self.assertEqual(tile.letter, 'U')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('T', 1)
        self.assertEqual(tile.letter, 'T')
        self.assertEqual(tile.value, 1)

    def test_tiles(self):
        tile = Tile('D', 2)
        self.assertEqual(tile.letter, 'D')
        self.assertEqual(tile.value, 2)
    
    def test_tiles(self):
        tile = Tile('G', 2)
        self.assertEqual(tile.letter, 'G')
        self.assertEqual(tile.value, 2)

    def test_tiles(self):
        tile = Tile('C', 3)
        self.assertEqual(tile.letter, 'C')
        self.assertEqual(tile.value, 3)

    def test_tiles(self):
        tile = Tile('B', 3)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 3)
    
    def test_tiles(self):
        tile = Tile('M', 3)
        self.assertEqual(tile.letter, 'M')
        self.assertEqual(tile.value, 3)

    def test_tiles(self):
        tile = Tile('P', 3)
        self.assertEqual(tile.letter, 'P')
        self.assertEqual(tile.value, 3)

    def test_tiles(self):
        tile = Tile('H', 4)
        self.assertEqual(tile.letter, 'H')
        self.assertEqual(tile.value, 4)

    def test_tiles(self):
        tile = Tile('F', 4)
        self.assertEqual(tile.letter, 'F')
        self.assertEqual(tile.value, 4)

    def test_tiles(self):
        tile = Tile('V', 4)
        self.assertEqual(tile.letter, 'V')
        self.assertEqual(tile.value, 4)

    def test_tiles(self):
        tile = Tile('Y', 4)
        self.assertEqual(tile.letter, 'Y')
        self.assertEqual(tile.value, 4)

    def test_tiles(self):
        tile = Tile('Q', 5)
        self.assertEqual(tile.letter, 'Q')
        self.assertEqual(tile.value, 5)

    def test_tiles(self):
        tile = Tile('CH', 5)
        self.assertEqual(tile.letter, 'CH')
        self.assertEqual(tile.value, 5)

    def test_tiles(self):
        tile = Tile('J', 8)
        self.assertEqual(tile.letter, 'J')
        self.assertEqual(tile.value, 8)

    def test_tiles(self):
        tile = Tile('Ñ', 8)
        self.assertEqual(tile.letter, 'Ñ')
        self.assertEqual(tile.value, 8)

    def test_tiles(self):
        tile = Tile('X', 8)
        self.assertEqual(tile.letter, 'X')
        self.assertEqual(tile.value, 8)

    def test_tiles(self):
        tile = Tile('LL', 8)
        self.assertEqual(tile.letter, 'LL')
        self.assertEqual(tile.value, 8)

    def test_tiles(self):
        tile = Tile('RR', 8)
        self.assertEqual(tile.letter, 'RR')
        self.assertEqual(tile.value, 8)

    def test_tiles(self):
        tile = Tile('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)

    def test_tiles(self):
        tile = Tile('?', 0)
        self.assertEqual(tile.letter, '?')
        self.assertEqual(tile.value, 0)

    @patch('random.shuffle') 
    
    def test_bag_tiles(self, patch_shuffle): #OK
        bag = BagTiles()
        self.assertEqual(
            len(bag.tile),
            100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tile,
        )
    
    
    def test_take(self): #OK
        bag = BagTiles()
        tile = bag.take(7)
        self.assertEqual(
            len(bag.tile),
            93,
        )
        self.assertEqual(
            len(tile),
            7,
        )
    
    def test_put(self): #OK
        bag = BagTiles()
        put_tile = [Tile
        ('?', 1)]
        bag.put(put_tile)
        self.assertEqual(
            len(bag.tile),
            101,
        )

class TestPlayer(unittest.TestCase):
    def test_init(self):
        pass

if __name__ == '__main__':
    unittest.main()