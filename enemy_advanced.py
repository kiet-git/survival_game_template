"""
enemy_advanced.py

Main Objective:
This module defines an advanced enemy type with more complex behavior.
Students will learn about:
1. Creating an enemy class with advanced behavior
2. Implementing more complex movement patterns
3. Adding special abilities to enemies

By the end of this module, students should understand how to create
more sophisticated enemy types and implement varied game mechanics.
"""

import random
import math
from game_setup import GameObject, PURPLE, WIDTH, HEIGHT, SQUARE_SIZE

ADVANCED_ENEMY_SPEED = 1.5
CHARGE_SPEED = 5
CHARGE_DURATION = 60  # frames

class AdvancedEnemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, SQUARE_SIZE, PURPLE)
        self.speed = ADVANCED_ENEMY_SPEED
        self.angle = random.uniform(0, 2 * math.pi)
        self.charge_duration = 0
        self.charge_cooldown = CHARGE_DURATION

    def update(self, player):
        if self.charge_duration > 0:
            self.charge(player)
        elif self.charge_cooldown > 0:
            self.charge_cooldown -= 1
        else:
            self.move_random()
            self.charge_cooldown -= 1
        self.keep_in_bounds()

    def move_random(self):
        self.angle += random.uniform(-0.1, 0.1)
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.move()

    def prepare_charge(self, player):
        # TODO: Prepare the enemy for a charge attack
        # 1. Generate a random number and check if it's less than 0.02 (2% chance)
        # 2. If true, calculate the direction to the player (dx and dy)
        # 3. Calculate the distance to the player
        # 4. Set speed_x and speed_y for the charge (use CHARGE_SPEED)
        # 5. Set charge_duration to CHARGE_DURATION
        pass

    def charge(self, player):
        # TODO: Implement the charge attack
        # 1. Call self.move() to continue the charge
        # 2. Decrease charge_duration by 1
        # 3. If charge_duration reaches 0, set charge_cooldown to 120 (2 seconds at 60 FPS)
        pass

def create_advanced_enemies(num_enemies):
    # TODO: Create a list of AdvancedEnemy objects
    # 1. Initialize an empty list to store enemies
    # 2. Use a loop to create 'num_enemies' AdvancedEnemy objects
    #    Position each enemy randomly within the screen boundaries
    # 3. Return the list of enemies
    pass

def update_advanced_enemies(enemies, player):
    # TODO: Update all advanced enemies in the list
    # 1. Loop through the enemies list
    # 2. Call the update() method for each enemy, passing the player object
    pass

def spawn_advanced_enemy(enemies, max_enemies):
    # TODO: Randomly spawn a new advanced enemy
    # 1. Check if the number of enemies is less than max_enemies
    # 2. Generate a random number and check if it's less than 0.01 (1% chance)
    # 3. If both conditions are true, create a new AdvancedEnemy at a random position
    #    and add it to the enemies list
    pass