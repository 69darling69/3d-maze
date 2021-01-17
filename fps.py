import pygame
from settings import *
# Show FPS on screen

# Initializing font module for text entertaiment
pygame.font.init()
# Choose font for text
FPSfont = pygame.font.SysFont(FPSfontName, FPSsize)

# Draw FPS on screen and return elapsed time
def fpsDrawing(window, clock):
    # Set to text number of frames that can be shown in one sec
    textsurface = FPSfont.render("FPS: " + str(int(clock.get_fps())), False, FPScolor, FPSbackground )
    # Draw text on screen
    window.blit(textsurface, FPSposition)
