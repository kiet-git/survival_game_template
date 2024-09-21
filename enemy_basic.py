"""
enemy_basic.py

Main Objective:
This module defines the basic enemy type. Students will learn about:
1. Creating an enemy class with simple behavior
2. Implementing basic movement patterns
3. Spawning and managing multiple enemies

By the end of this module, students should understand how to create and
manage simple enemy objects in a game.
"""

import random
from game_setup import GameObject, BLUE, WIDTH, HEIGHT, SQUARE_SIZE

ENEMY_SPEED = 2

class BasicEnemy(GameObject):
    def __init__(self, x, y):
        # TODO: Initialize the BasicEnemy object
        # 1. Call the parent class's __init__ method with appropriate arguments
        # 2. Set random initial speeds for x and y directions using ENEMY_SPEED
        #    Hint: Use random.choice([-ENEMY_SPEED, ENEMY_SPEED]) for each direction
        super().__init__(x, y, SQUARE_SIZE, BLUE)
        self.speed_x = random.choice([-ENEMY_SPEED, ENEMY_SPEED])
        self.speed_y = random.choice([-ENEMY_SPEED, ENEMY_SPEED])

    def update(self):
        # TODO: Update the enemy's position
        # 1. Call the move() method to update the enemy's position based on speed
        # 2. Call the bounce() method to handle collision with screen edges
        self.move()
        self.bounce()

    def bounce(self):
        # TODO: Implement bouncing behavior for screen edge collision
        # 1. Check if the enemy has hit the left or right edge of the screen
        #    If so, reverse the x direction speed
        # 2. Check if the enemy has hit the top or bottom edge of the screen
        #    If so, reverse the y direction speed
        if self.x <= 0 or self.x + self.size >= WIDTH:
            self.speed_x = -self.speed_x
        if self.y <= 0 or self.y + self.size >= HEIGHT:
            self.speed_y = -self.speed_y

def create_basic_enemies(num_enemies):
    # TODO: Create a list of BasicEnemy objects
    # 1. Initialize an empty list to store enemies
    # 2. Use a loop to create 'num_enemies' BasicEnemy objects
    #    Position each enemy randomly within the screen boundaries
    # 3. Return the list of enemies
    enemies = []
    for i in range(num_enemies):
        x = random.randint(0, WIDTH - SQUARE_SIZE)
        y = random.randint(0, HEIGHT - SQUARE_SIZE)
        enemies.append(BasicEnemy(x, y))
    return enemies

def update_basic_enemies(enemies):
    # TODO: Update all basic enemies in the list
    # 1. Loop through the enemies list
    # 2. Call the update() method for each enemy
    for enemy in enemies:
        enemy.update()

def spawn_basic_enemy(enemies, max_enemies):
    # TODO: Randomly spawn a new basic enemy
    # 1. Check if the number of enemies is less than max_enemies
    # 2. Generate a random number and check if it's less than 0.02 (2% chance)
    # 3. If both conditions are true, create a new BasicEnemy at a random position
    #    and add it to the enemies list
    if len(enemies) < max_enemies and random.random() < 0.02:
        x = random.randint(0, WIDTH - SQUARE_SIZE)
        y = random.randint(0, HEIGHT - SQUARE_SIZE)
        enemies.append(BasicEnemy(x, y))