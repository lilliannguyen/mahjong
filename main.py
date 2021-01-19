import collections
import random

tile = collections.namedtuple('tile', ['rank', 'suit'])

class RiichiTiles:

    ranks = [str(n) for n in range(1, 10)]
    suits = 'souzu pinzu manzu'.split()

    def __init__(self):
        self._tiles = [tile(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._tiles)

    def __getitem__(self, position):
        return self._tiles[position]

    def shuffle(self):
        return random.shuffle(self._tiles)

my_tiles = RiichiTiles()

print(my_tiles._tiles)

my_tiles.shuffle()

print(my_tiles._tiles)