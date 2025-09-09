"""
UI module for the Asteroids game.
Handles text rendering and HUD display.
"""
import pygame
from constants import *

class UI:
    def __init__(self):
        pass
    
    def draw_text(self, screen, text, size, x, y, color="white", align="center"):
        """Draw text on screen with specified alignment."""
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        
        if align == "left":
            text_rect.left = x
            text_rect.centery = y
        else:  # center alignment (default)
            text_rect.center = (x, y)
        
        screen.blit(text_surface, text_rect)
    
    def draw_gameplay_hud(self, screen, score, high_score):
        """Draw the HUD during gameplay."""
        self.draw_text(screen, f"Score: {score}", UI_SCORE_FONT_SIZE, UI_SCORE_X_POSITION, UI_SCORE_Y_POSITION, align="left")
        self.draw_text(screen, f"High Score: {high_score}", UI_SCORE_FONT_SIZE, UI_SCORE_X_POSITION, UI_HIGH_SCORE_Y_POSITION, align="left")
    
    def draw_game_over_screen(self, screen, score, high_score):
        """Draw the game over screen."""
        self.draw_text(screen, "GAME OVER", UI_GAME_OVER_TITLE_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - UI_GAME_OVER_Y_OFFSET, "red")
        self.draw_text(screen, f"Final Score: {score}", UI_GAME_OVER_TEXT_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - UI_GAME_OVER_SCORE_Y_OFFSET)
        self.draw_text(screen, f"High Score: {high_score}", UI_GAME_OVER_TEXT_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.draw_text(screen, "Press R to Restart", UI_GAME_OVER_INSTRUCTION_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + UI_GAME_OVER_INSTRUCTION_Y_OFFSET)
