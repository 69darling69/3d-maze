import pygame
import math
from settings import *

class Player:
    def __init__(self, position, angle, speed):
        self.position = position
        self.speed = speed
        self.angle = angle

    def movement(self, fps):
        # Set of pressed keys
        keys = pygame.key.get_pressed()
        # Calculate sin and cos of angle
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        # If key is pressed, then move
        velocity = pygame.math.Vector2()
        if keys[pygame.K_w]:
            velocity += (self.speed * cos_a * 1000 / fps, self.speed * sin_a * 1000 / fps)
        if keys[pygame.K_s]:
            velocity += (-self.speed * cos_a * 1000 / fps, -self.speed * sin_a * 1000 / fps)
        if keys[pygame.K_a]:
            velocity += (self.speed * sin_a * 1000 / fps, -self.speed * cos_a * 1000 / fps)
        if keys[pygame.K_d]:
            velocity += (-self.speed * sin_a * 1000 / fps, self.speed * cos_a * 1000 / fps)
        if velocity.length() != 0:
            velocity = velocity.normalize()
        self.position += velocity
        if keys[pygame.K_LEFT]:
            self.angle -= playerRotationSpeed
        if keys[pygame.K_RIGHT]:
            self.angle += playerRotationSpeed
