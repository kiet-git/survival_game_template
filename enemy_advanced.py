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
        # TODO: Initialize the AdvancedEnemy object
        # 1. Call the parent class's __init__ method with appropriate arguments
        # 2. Set the initial speed to ADVANCED_ENEMY_SPEED
        # 3. Set a random initial angle (hint: use random.uniform(0, 2 * math.pi))
        # 4. Initialize charge_cooldown and charge_duration to 0
        super().__init__(x, y, SQUARE_SIZE, PURPLE)
        self.speed = ADVANCED_ENEMY_SPEED
        self.angle = random.uniform(0, 2 * math.pi)
        self.charge_cooldown = 0
        self.charge_duration = CHARGE_DURATION

    def update(self, player):
        # TODO: Update the advanced enemy's state and position
        # 1. Check if the enemy is currently charging (charge_duration > 0)
        #    If so, call self.charge(player)
        # 2. If not charging, check if charge is ready (charge_cooldown == 0)
        #    If ready, call self.prepare_charge(player)
        # 3. If not charging and not ready, call self.move_random()
        #    and decrease charge_cooldown by 1
        # 4. Finally, call self.keep_in_bounds() to ensure the enemy stays on screen
        if self.charge_duration > 0:
            self.charge(player)
        elif self.charge_cooldown == 0:
            self.prepare_charge(player)
        else:
            self.move_random()
            self.charge_cooldown -= 1

        self.keep_in_bounds()

    def move_random(self):
        # TODO: Implement random movement for the advanced enemy
        # 1. Slightly adjust the angle (hint: use random.uniform(-0.1, 0.1))
        # 2. Calculate new speed_x and speed_y using math.cos and math.sin
        # 3. Call self.move() to update the position
        self.angle += random.uniform(-0.1, 0.1)
        self.speed_x = self.speed * math.cos(self.angle)
        self.speed_y = self.speed * math.sin(self.angle)
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