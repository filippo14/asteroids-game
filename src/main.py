"""
Entry point for the Asteroids game.
This simplified main.py imports and runs the game using the modular structure.
"""
from game import Game

def main():
    """Main entry point for the game."""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
