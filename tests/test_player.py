import unittest
from game.player import Player
from game.bagtiles import BagTiles, Tile

class TestPlayer(unittest.TestCase):
    
    def test_init(self): #OK
        bag_tiles = BagTiles()
        player = Player('juanita', 0, 0, bag_tiles)
        self.assertEqual(player.name, 'juanita')
        self.assertEqual(player.score, 0)
        self.assertEqual(player.number, 0)
        self.assertEqual(len(player.tiles), 0)

    def test_add_tiles(self): #OK
        bag_tiles = BagTiles()
        player = Player('juanita', 0, 0, bag_tiles)
        tiles=[Tile('A',1),Tile('B',1),Tile('C',1)]
        player.add_tiles(tiles)
        self.assertEqual(len(player.tiles),3)
        self.assertEqual(player.tiles[0].letter,'A')
        self.assertEqual(player.tiles[1].letter,'B')
        self.assertEqual(player.tiles[2].letter,'C')

    def test_show_score(exception):
        pass
    
    def test_get_tiles(exception):
        pass
    
    def test_play_word(exception):
        pass

if __name__ == '__main__':
    unittest.main()