"""
game_setup.py

Main Objective:
This module is responsible for initializing the game environment, defining shared
constants, and creating basic game object classes. Students will learn about:
1. Setting up a Pygame project
2. Defining game constants and configurations
3. Creating a base class for game objects

By the end of this module, students should understand how to structure the
foundational elements of a game and create a flexible base for game objects.
"""

import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Enemy Survival Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)

# Game objects properties
SQUARE_SIZE = 40

# Font for displaying text
font = pygame.font.Font(None, 36)

# Clock for controlling frame rate
clock = pygame.time.Clock()

class GameObject:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def keep_in_bounds(self):
        self.x = max(0, min(self.x, WIDTH - self.size))
        self.y = max(0, min(self.y, HEIGHT - self.size))

def check_collision(obj1, obj2):
    return (obj1.x < obj2.x + obj2.size and
            obj1.x + obj1.size > obj2.x and
            obj1.y < obj2.y + obj2.size and
            obj1.y + obj1.size > obj2.y)

# Game states
PLAYING = 0
GAME_OVER = 1
