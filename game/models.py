import random
class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    def get_letter(self):
        return self.letter

    def get_value(self):
        return self.value


class BagTiles:
    def __init__(self):
        self.tiles = []
        self.tile_count = {}
        self.tile_scores = {
            'A': 1, 'B': 3, 'C': 3, 'CH': 5, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 
            'H': 4, 'I': 1, 'J': 8, 'L': 1, 'LL': 8, 'M': 3, 'N': 1, 'Ñ': 8, 
            'O': 1, 'P': 3, 'Q': 5, 'R': 1, 'RR': 8,  'S': 1, 'T': 1, 'U': 1, 
            'V': 4, 'X': 8, 'Y': 4, 'Z': 10, #diccionario de letras y su valor de puntos
        }
        self.initialize_tiles()

    def initialize_tiles(self):
        for letter, count in self.tile_scores.items():
            for _ in range(count):
                self.tiles.append(Tile(letter, self.tile_scores[letter]))
                if letter in self.tile_count:
                    self.tile_count[letter] += 1
                else:
                    self.tile_count[letter] = 1

        #agregar los 2 comodines 
        for _ in range(2):
            self.tiles.append(Tile('?', 0))

        random.shuffle(self.tiles) #mezcla aleatoriamente las fichas


    def __init__(self):     #lo hizo el profe
        self.tiles = [
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
            Tile('A', 1),
        ]
        random.shuffle(self.tiles) #lo hizo el profe

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles
        
    def put(self, tiles):
        self.tiles.extend(tiles)