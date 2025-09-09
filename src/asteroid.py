import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, DEFAULT_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    # Split the asteroid into two smaller asteroids:
    # - Large asteroids will be split into two medium asteroids; 
    # - Medium asteroids split into two small asteroids
    # - Small asteroids disappear when destroyed
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(ASTEROID_SPLIT_ANGLE_MIN, ASTEROID_SPLIT_ANGLE_MAX)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * ASTEROID_SPLIT_SPEED_MULTIPLIER
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * ASTEROID_SPLIT_SPEED_MULTIPLIER
