# Multi-Enemy Survival Game

This project is a simple 2D survival game created using Pygame. The player must avoid different types of enemies while trying to survive as long as possible.

## Project Structure

The game is divided into five Python files:

1. `game_setup.py`: Initializes the game environment and defines shared constants and base classes.
2. `player.py`: Defines the Player class, manages score, and handles win/lose conditions.
3. `enemy_basic.py`: Implements a basic enemy type with simple movement patterns.
4. `enemy_advanced.py`: Implements an advanced enemy type with more complex behavior.
5. `main_game.py`: Contains the main game loop, rendering, and overall game flow.

## Prerequisites

To run this game, you need to have Python and Pygame installed on your system.

1. Python 3.x: Download and install from [python.org](https://www.python.org/downloads/)
2. Pygame: Install using pip by running the following command in your terminal or command prompt:

   ```
   pip install pygame
   ```

## How to Run the Game

1. Ensure all five Python files (`game_setup.py`, `player.py`, `enemy_basic.py`, `enemy_advanced.py`, and `main_game.py`) are in the same directory.

2. Open a terminal or command prompt and navigate to the directory containing the game files.

3. Run the following command:

   ```
   python main_game.py
   ```

4. The game window should appear, and you can start playing!

## Game Controls

- Use the arrow keys to move the player (red square) around the screen.
- Avoid colliding with the basic enemies (blue squares) and advanced enemies (purple squares).
- Try to survive as long as possible to achieve a high score!

## Customization

Feel free to modify the game parameters in the various files to change the game's behavior:

- Adjust enemy speeds, spawn rates, or movement patterns.
- Change the size of the game window or game objects.
- Add new types of enemies or power-ups.

Enjoy the game and happy coding!