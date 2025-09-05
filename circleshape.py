import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Default draw method - subclasses should override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
