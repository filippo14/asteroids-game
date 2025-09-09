#!/usr/bin/env python3
"""
Entry point for the Asteroids game.
This file imports and runs the main game from the src directory.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main game
from main import main

if __name__ == "__main__":
    main()
