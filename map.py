from settings import *

# Text display of map
text_map = [
'WWWWWWWWWWWW',
'W.......W..W',
'W.W.WWW.WW.W',
'W..........W',
'WW.WW...W..W',
'W.....W.WW.W',
'W.W...W....W',
'WWWWWWWWWWWW'
]

# Converte text map to set of tiles
world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
