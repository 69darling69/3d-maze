import pygame
from settings import *
# Show FPS on screen
# Past this code into draw loop
# elapsedTime, frameTime = fpsDrawing(frameTime, window)

# Initializing font module for text entertaiment
pygame.font.init()
# Time elapsed per one frame
frameTime = pygame.time.get_ticks()
# Time per last frame (im milliseconds)
elapsedTime = 1000/FPS
# Choose font for text
FPSfont = pygame.font.SysFont(FPSfontName, FPSsize)

# Draw FPS on screen and return elapsed time
def fpsDrawing(elapsedTime, window):
    # Finds elapsed since last frame
    frameTime = pygame.time.get_ticks() - elapsedTime
    # Set to text number of frames that can be shown in one sec
    textsurface = FPSfont.render("FPS: " + str(1000//frameTime), False, FPScolor)
    # Draw text on screen
    window.blit(textsurface, FPSposition)
    # Return new frame time
    return 1000//frameTime, pygame.time.get_ticks()
