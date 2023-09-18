import unittest
from game.player import Player
from game.bagtiles import BagTiles

class TestPlayer(unittest.TestCase):
    
    def test_init(self):
        bag_tiles = BagTiles()
        player = Player('juanita', 0, 0, bag_tiles)
        self.assertEqual(player.name, 'juanita')
        self.assertEqual(player.score, 0)
        self.assertEqual(player.number, 0)
        self.assertEqual(len(player.tile), 0)

    def test_add_tiles(self):
        bag_tiles = BagTiles()
        player = Player('juanita', 0, 0, bag_tiles)

        tiles = [Tile('A', 1), Tile('B', 1), Tile('C', 1)]
        player.add_tiles(tiles)

        self.assertEqual(len(player.tile), 3)
        self.assertEqual(player.tile[0].letter, 'A')
        self.assertEqual(player.tile[1].letter, 'B')
        self.assertEqual(player.tile[2].letter, 'C')

if __name__ == '__main__':
    unittest.main()