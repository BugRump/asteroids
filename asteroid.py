import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            aa = random.uniform(20, 50)
            nav1 = self.velocity.rotate(aa)
            nav2 = self.velocity.rotate(-aa)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid1.velocity = nav1 * 1.2
            new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid2.velocity = nav2 * 1.2

