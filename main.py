import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group() # group of objects that can be updated
    drawable = pygame.sprite.Group() # group of objects that can be drawn
    asteroids = pygame.sprite.Group() # group of asteroids
    shots = pygame.sprite.Group() # group of shots

    # we are setting the static containers attribute of the Player and Asteroid classes to the above created groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        fps = clock.tick(60) # 60 FPS -> will pause the game until 1/60 seconds have passed
        dt = fps / 1000 # convert milliseconds to seconds

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    bullet.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
