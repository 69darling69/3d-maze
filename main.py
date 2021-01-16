import pygame
# Settings file
from settings import *
# Player's class
from player import Player
# FPS drawing
from fps import *

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
    window.fill(WHITE)

    # Physics here
    player.movement(elapsedTime)

    # Draw here
    pygame.draw.circle(window, BLACK, player.position, 10)

    # FPS drawing (don't touch it if you don't know how it's works)
    elapsedTime, frameTime = fpsDrawing(frameTime, window)

    # Draw everything on screen
    pygame.display.flip()

    # Set frames per second
    clock.tick(FPS)
