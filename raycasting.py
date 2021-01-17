import pygame
from settings import *
from map import world_map
import math

def ray_casting(window, playerPosition, playerAngle):
    # Choose angle
    currentAngle = playerAngle - FOV/2
    # For every ray
    for ray in range(NUM_RAYS):
        # Calcualte sin and cos
        sin_a = math.sin(currentAngle)
        cos_a = math.cos(currentAngle)
        # For max depth
        for depth in range(MAX_DEPTH):
            # Increase position of point
            x = playerPosition.x + depth * cos_a
            y = playerPosition.y + depth * sin_a
            # If hits any square
            if (x // TILE_SIZE * TILE_SIZE, y // TILE_SIZE * TILE_SIZE) in world_map:
                # Remove bulb effect of view
                depth *= math.cos(playerAngle - currentAngle)
                # Calculate height of rectangle to draw
                projectionHeight = PROJECTION_COEFFIENCE / depth
                # Calculate color based on distance
                color = 255 / (1 + depth**2 * .0002)
                # Draw rectangle
                pygame.draw.rect(window, (color, color, color), (ray * SCALE, HEIGHT/2 - projectionHeight // 2, SCALE, projectionHeight))
                break
        # Uncomment to see all rays
        #pygame.draw.line(window, RED, playerPosition, (x, y), 2)
        currentAngle += DELTA_ANGLE
