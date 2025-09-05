# Asteroids Game

This is a simple Asteroids game implemented in Python using the Pygame library.

## Prerequisites

*   Python 3.x
*   Pygame 2.6.1

## Running the Game

1.  **Clone the repository or download the source code.**
2.  **Install dependencies:**
    Open your terminal or command prompt, navigate to the project directory, and run:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the game:**
    In the same terminal, run:
    ```bash
    python main.py
    ```

## How to Play

### Controls
*   **A** - Rotate spaceship left
*   **D** - Rotate spaceship right  
*   **W** - Move forward (thrust)
*   **S** - Move backward
*   **SPACE** - Shoot

### Game Mechanics
*   Control a triangular spaceship that can rotate and move in any direction
*   Asteroids spawn from the edges of the screen and drift across
*   Colliding with an asteroid ends the game immediately
*   Shooting an asteroid splits it into two smaller asteroids
*   Small asteroids disappear when shot
*   The objective is to survive as long as possible by avoiding and destroying asteroids 