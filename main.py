import sys
import pygame
import os
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

class GameState:
    PLAYING = "playing"
    GAME_OVER = "game_over"

SCORE_FILE = "high_score.txt"

def load_high_score():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, 'r') as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

def save_high_score(score):
    with open(SCORE_FILE, 'w') as f:
        f.write(str(score))

def draw_text(screen, text, size, x, y, color="white"):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def reset_game():
    # Clear all sprite groups
    for group in [updatable, drawable, asteroids, shots]:
        group.empty()
    
    # Create new player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    return player, asteroid_field

def main():
    global updatable, drawable, asteroids, shots

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0
    
    # Game state and scoring
    game_state = GameState.PLAYING
    score = 0
    high_score = load_high_score()

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
            elif event.type == pygame.KEYDOWN:
                if game_state == GameState.GAME_OVER and event.key == pygame.K_r:
                    # Restart game
                    game_state = GameState.PLAYING
                    score = 0
                    player, asteroid_field = reset_game()
        
        screen.fill("black")

        if game_state == GameState.PLAYING:
            fps = clock.tick(60) # 60 FPS -> will pause the game until 1/60 seconds have passed
            dt = fps / 1000 # convert milliseconds to seconds

            updatable.update(dt)

            # Check collisions
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    # Update high score if needed
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)
                    game_state = GameState.GAME_OVER
                    break
                for bullet in shots:
                    if asteroid.collides_with(bullet):
                        bullet.kill()
                        asteroid.split()
                        # Add points based on asteroid size
                        points = 100 if asteroid.radius <= ASTEROID_MIN_RADIUS else 50 if asteroid.radius <= ASTEROID_MIN_RADIUS * 2 else 20
                        score += points

            for obj in drawable:
                obj.draw(screen)
            
            # Draw current score and high score during gameplay
            draw_text(screen, f"Score: {score}", 36, 100, 30)
            draw_text(screen, f"High Score: {high_score}", 36, 100, 70)
            
        elif game_state == GameState.GAME_OVER:
            # Draw game over screen
            draw_text(screen, "GAME OVER", 72, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, "red")
            draw_text(screen, f"Final Score: {score}", 48, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
            draw_text(screen, f"High Score: {high_score}", 48, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text(screen, "Press R to Restart", 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

        pygame.display.flip()

if __name__ == "__main__":
    main()
