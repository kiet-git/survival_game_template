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
        super().__init__(x, y, SQUARE_SIZE, RED)
        self.score = 0
        self.lives = 3

    def handle_input(self, keys):
        if pygame.key.get_pressed():
            if keys[pygame.K_w]:
                self.speed_y = -PLAYER_SPEED
            if keys[pygame.K_s]:
                self.speed_y = PLAYER_SPEED
            if keys[pygame.K_a]:
                self.speed_x = -PLAYER_SPEED
            if keys[pygame.K_d]:
                self.speed_x = PLAYER_SPEED

    def update(self):
        self.move()
        self.keep_in_bounds()

    def increase_score(self, points=1):
        self.score += points

    def lose_life(self):
        self.lives -= 1
        return self.lives <= 0

def create_player():
    return Player(WIDTH // 2, HEIGHT // 2)

def get_score_text(player):
    return f"Score: {player.score} | Lives: {player.lives}"

def get_game_over_text(player):
    return f"Game Over! Your score: {player.score}"