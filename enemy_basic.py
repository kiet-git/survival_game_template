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
        super().__init__(x, y, SQUARE_SIZE, BLUE)
        self.speed_x = random.choice([-ENEMY_SPEED, ENEMY_SPEED])
        self.speed_y = random.choice([-ENEMY_SPEED, ENEMY_SPEED])

    def update(self):
        self.move()
        self.bounce()

    def bounce(self):
        if self.x + self.size >= WIDTH or self.x <= 0:
            self.speed_x = -self.speed_x
        if self.y + self.size >= HEIGHT or self.y <= 0:
            self.speed_y = -self.speed_y

def create_basic_enemies(num_enemies):
    enemies = []
    for i in range(num_enemies):
        x = random.randint(0, WIDTH - SQUARE_SIZE)
        y = random.randint(0, HEIGHT - SQUARE_SIZE)
        enemies.append(BasicEnemy(x, y))
    return enemies

def update_basic_enemies(enemies):
    for enemy in enemies:
        enemy.update()

def spawn_basic_enemy(enemies, max_enemies):
    if len(enemies) < max_enemies and random.random() < 0.02:
        x = random.randint(0, WIDTH - SQUARE_SIZE)
        y = random.randint(0, HEIGHT - SQUARE_SIZE)
        enemies.append(BasicEnemy(x, y))