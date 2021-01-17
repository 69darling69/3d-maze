import pygame
import math
# Settings file
from settings import *
# Player's class
from player import Player
# FPS drawing
from fps import *
# Map module
from map import world_map
# Ray casting funtion
from raycasting import ray_casting

# Initializing pygame module
pygame.init()
# Initializing pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Initializing pygame clock
clock = pygame.time.Clock()
# Rename window title
pygame.display.set_caption('3D-maze')
# Player object
player = Player(pygame.math.Vector2(WIDTH//2, HEIGHT//2), 0, playerSpeed)

# Infinite game loop
while True:
    # Goes through all events
    for event in pygame.event.get():
        # If window was closed then exit the game
        if event.type == pygame.QUIT:
            exit()

    # Clear screen
    window.fill(BLACK)

    ### Physics here
    player.movement()

    ### Draw here

    # Uncomment to see player
    #pygame.draw.circle(window, WHITE, player.position, 10)

    # Uncomment to see map
    #for x, y in world_map:
    #    pygame.draw.rect(window, BLUE, (x, y, TILE_SIZE, TILE_SIZE), 2)

    # Raycasting draw
    ray_casting(window, player.position, player.angle)

    # Draw FPS on screen
    fpsDrawing(window, clock)

    # Draw everything on screen
    pygame.display.flip()

    # Set frames per second
    clock.tick(FPS)
