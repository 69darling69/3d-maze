import pygame
from settings import *

class Player:
    def __init__(self, position, angle, speed):
        self.position = position
        self.speed = speed
        self.angle = angle

    def movement(self, elapsedTime):
        # Set of pressed keys
        keys = pygame.key.get_pressed()
        # If key is pressed, then move
        if keys[pygame.K_w]:
            self.position.y -= self.speed * elapsedTime
        if keys[pygame.K_s]:
            self.position.y += self.speed * elapsedTime
        if keys[pygame.K_a]:
            self.position.x -= self.speed * elapsedTime
        if keys[pygame.K_d]:
            self.position.x += self.speed * elapsedTime
        if keys[pygame.K_LEFT]:
            self.angle -= playerRotationSpeed
        if keys[pygame.K_RIGHT]:
            self.angle += playerRotationSpeed
