from math import pi, tan
# Window size
WIDTH = 1200
HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player's settings
playerSpeed = .1
playerRotationSpeed = .03

# Frames per second
FPS = 0
FPSposition = (0, 0)
FPScolor = BLACK
FPSbackground = WHITE
FPSsize = 30
FPSfontName = 'Comic Sans MS'

# Map
TILE_SIZE = 100

# Ray casting
FOV = pi / 3
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * tan(FOV/2))
PROJECTION_COEFFIENCE = 3 * DIST * TILE_SIZE
SCALE = WIDTH // NUM_RAYS
