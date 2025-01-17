"""
player.py

Main Objective:
This module defines the Player class, manages the player's score, and handles
win/lose conditions. Students will learn about:
1. Extending the base GameObject class for specific behavior
2. Implementing player movement and controls
3. Managing game score and win/lose conditions

By the end of this module, students should understand how to create a player
object with custom behavior and manage game outcomes.
"""
import pygame
from game_setup import GameObject, RED, WIDTH, HEIGHT, SQUARE_SIZE

PLAYER_SPEED = 5

class Player(GameObject):
    def __init__(self, x, y):
        # TODO: Initialize the Player object
        # 1. Call the parent class's __init__ method with appropriate arguments
        # 2. Initialize the score attribute to 0
        # 3. Initialize the lives attribute to 3
        pass

    def handle_input(self, keys):
        # TODO: Handle player input to move the player
        # 1. Use the keys parameter (pygame.key.get_pressed()) to check which arrow keys are pressed
        # 2. Set self.speed_x based on left/right arrow keys and PLAYER_SPEED
        # 3. Set self.speed_y based on up/down arrow keys and PLAYER_SPEED
        pass

    def update(self):
        # TODO: Update the player's position
        # 1. Call the move() method to update the player's position based on speed
        # 2. Call the keep_in_bounds() method to ensure the player stays within the screen
        pass

    def increase_score(self, points=1):
        # TODO: Increase the player's score
        # 1. Add the points parameter to the player's score
        pass

    def lose_life(self):
        # TODO: Handle the player losing a life
        # 1. Decrease the player's lives by 1
        # 2. Return True if the player has no lives left, False otherwise
        pass

def create_player():
    # TODO: Create and return a new Player object
    # 1. Return a new Player object positioned at the center of the screen
    pass

def get_score_text(player):
    # TODO: Create and return the score display text
    # 1. Return a formatted string containing the player's score and remaining lives
    pass

def get_game_over_text(player):
    # TODO: Create and return the game over text
    # 1. Return a formatted string displaying "Game Over" and the player's final score
    pass