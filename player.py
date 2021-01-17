import pygame
import math
from settings import *

class Player:
    def __init__(self, position, angle, speed):
        self.position = position
        self.speed = speed
        self.angle = angle

    def movement(self):
        # Set of pressed keys
        keys = pygame.key.get_pressed()
        # Calculate sin and cos of angle
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        # If key is pressed, then move
        if keys[pygame.K_w]:
            self.position.x += self.speed * cos_a
            self.position.y += self.speed * sin_a
        if keys[pygame.K_s]:
            self.position.x -= self.speed * cos_a
            self.position.y -= self.speed * sin_a
        if keys[pygame.K_a]:
            self.position.x += self.speed * sin_a
            self.position.y -= self.speed * cos_a
        if keys[pygame.K_d]:
            self.position.x -= self.speed * sin_a
            self.position.y += self.speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= playerRotationSpeed
        if keys[pygame.K_RIGHT]:
            self.angle += playerRotationSpeed
