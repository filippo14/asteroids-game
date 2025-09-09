"""
Score management module for the Asteroids game.
Handles loading, saving, and calculating scores.
"""
import os
from constants import ASTEROID_MIN_RADIUS

SCORE_FILE = "high_score.txt"

class ScoreManager:
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()
    
    def load_high_score(self):
        """Load the high score from file."""
        if os.path.exists(SCORE_FILE):
            try:
                with open(SCORE_FILE, 'r') as f:
                    return int(f.read().strip())
            except:
                return 0
        return 0
    
    def save_high_score(self):
        """Save the current high score to file."""
        with open(SCORE_FILE, 'w') as f:
            f.write(str(self.high_score))
    
    def add_points_for_asteroid(self, asteroid_radius):
        """Add points based on asteroid size."""
        if asteroid_radius <= ASTEROID_MIN_RADIUS:
            points = SCORE_SMALL_ASTEROID
        elif asteroid_radius <= ASTEROID_MIN_RADIUS * 2:
            points = SCORE_MEDIUM_ASTEROID
        else:
            points = SCORE_LARGE_ASTEROID
        
        self.score += points
        return points
    
    def reset_score(self):
        """Reset the current score to 0."""
        self.score = 0
    
    def update_high_score(self):
        """Update high score if current score is higher."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
            return True
        return False
