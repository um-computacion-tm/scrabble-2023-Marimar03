from game.bagtiles import BagTiles
class Player:
    def __init__(self, name, score, number, bag_tiles):
            self.name = name
            self.score = score
            self.number = number
            self.tile = [] 
            self.bag_tiles = bag_tiles 

    def add_tiles(self, Tile):
        self.tile.extend(Tile)
   
    def show_score(self):
        return self.score
    
    def get_tiles(self):
        return self.tile
    
    def play_word(Exception):
        pass