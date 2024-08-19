from map import map
from sprites import WhiteTile


def get_tilemap(self, map):
    for r, row in enumerate(map):
        print(r)
        for c, column in enumerate(row):
            WhiteTile(self, c, r)
