"""
Main game class for the Asteroids game.
Handles game state, collision detection, and game loop logic.
"""
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score_manager import ScoreManager
from ui import UI

class GameState:
    PLAYING = "playing"
    GAME_OVER = "game_over"

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids")
        self.clock = pygame.time.Clock()
        
        # Game components
        self.score_manager = ScoreManager()
        self.ui = UI()
        self.game_state = GameState.PLAYING
        
        # Sprite groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        
        # Set up sprite containers
        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable,)
        Shot.containers = (self.shots, self.updatable, self.drawable)
        
        # Initialize game objects
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroid_field = AsteroidField()
    
    def reset_game(self):
        """Reset the game to initial state."""
        # Clear all sprite groups
        for group in [self.updatable, self.drawable, self.asteroids, self.shots]:
            group.empty()
        
        # Reset score
        self.score_manager.reset_score()
        
        # Create new game objects
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroid_field = AsteroidField()
        
        # Reset game state
        self.game_state = GameState.PLAYING
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if self.game_state == GameState.GAME_OVER and event.key == pygame.K_r:
                    self.reset_game()
        return True
    
    def check_collisions(self):
        """Check for collisions between game objects."""
        # Check player-asteroid collisions
        for asteroid in self.asteroids:
            if asteroid.collides_with(self.player):
                self.score_manager.update_high_score()
                self.game_state = GameState.GAME_OVER
                return
        
        # Check bullet-asteroid collisions (use copy to avoid modification during iteration)
        for asteroid in list(self.asteroids):
            for bullet in list(self.shots):
                if asteroid.collides_with(bullet):
                    bullet.kill()
                    # Get points BEFORE splitting (which kills the asteroid)
                    self.score_manager.add_points_for_asteroid(asteroid.radius)
                    asteroid.split()
                    break  # Exit bullet loop since asteroid is destroyed
    
    def update_gameplay(self, dt):
        """Update game objects during gameplay."""
        self.updatable.update(dt)
        self.check_collisions()
    
    def draw_gameplay(self):
        """Draw gameplay elements."""
        for obj in self.drawable:
            obj.draw(self.screen)
        self.ui.draw_gameplay_hud(self.screen, self.score_manager.score, self.score_manager.high_score)
    
    def draw_game_over(self):
        """Draw game over screen."""
        self.ui.draw_game_over_screen(self.screen, self.score_manager.score, self.score_manager.high_score)
    
    def run(self):
        """Main game loop."""
        running = True
        
        while running:
            running = self.handle_events()
            if not running:
                break
            
            self.screen.fill("black")
            
            if self.game_state == GameState.PLAYING:
                fps = self.clock.tick(GAME_FPS)
                dt = fps / 1000
                self.update_gameplay(dt)
                self.draw_gameplay()
            elif self.game_state == GameState.GAME_OVER:
                self.clock.tick(GAME_FPS)  # Still maintain framerate
                self.draw_game_over()
            
            pygame.display.flip()
        
        pygame.quit()
