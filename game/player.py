from game.bagtiles import BagTiles
class Player:
    def _init_(self, score):
        self.score = score
        self.tiles = []
    
    def draw_tiles(self, bag):
        self.tiles = bag.draw_tiles()
   
    def show_score(self):
        return self.score
    
    def get_tiles(self):
        return self.tiles
    
    def play_word(self, word):
        pass