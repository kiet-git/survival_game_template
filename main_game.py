"""
main_game.py

Main Objective:
This module implements the main game loop, handles rendering, and manages the
overall flow of the game. Students will learn about:
1. Structuring a game loop
2. Integrating all game components (player, enemies, etc.)
3. Handling game events and user input
4. Rendering game objects and UI elements
5. Managing different game states (playing, game over, etc.)

By the end of this module, students should understand how to bring together
various game elements to create a functional game, manage the game loop,
and handle different game states.
"""

import pygame
import sys
from game_setup import screen, clock, WIDTH, HEIGHT, WHITE, BLACK, font, check_collision, PLAYING, GAME_OVER
from player import create_player, get_score_text, get_game_over_text
from enemy_basic import create_basic_enemies, update_basic_enemies, spawn_basic_enemy
from enemy_advanced import create_advanced_enemies, update_advanced_enemies, spawn_advanced_enemy

def draw_game_objects(player, basic_enemies, advanced_enemies):
    player.draw(screen)
    for enemy in basic_enemies + advanced_enemies:
        enemy.draw(screen)

def draw_ui(player):
    score_text = font.render(get_score_text(player), True, BLACK)
    screen.blit(score_text, (10, 10))

def draw_game_over(player):
    screen.fill(WHITE)
    game_over_text = font.render(get_game_over_text(player), True, BLACK)
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, text_rect)

    restart_text = font.render("Press SPACE to restart", True, BLACK)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_text, restart_rect)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def check_collisions(player, basic_enemies, advanced_enemies):
    for enemy in basic_enemies + advanced_enemies:
        if check_collision(player, enemy):
            return True
    return False

def main():
    player = create_player()
    basic_enemies = create_basic_enemies(3)
    advanced_enemies = create_advanced_enemies(1)
    game_state = PLAYING

    while True:
        if not handle_events():
            break

        keys = pygame.key.get_pressed()

        if game_state == PLAYING:
            screen.fill(WHITE)
            
            player.handle_input(keys)
            player.update()
            update_basic_enemies(basic_enemies)
            update_advanced_enemies(advanced_enemies, player)
            
            spawn_basic_enemy(basic_enemies, 5)
            spawn_advanced_enemy(advanced_enemies, 3)
            
            if check_collisions(player, basic_enemies, advanced_enemies):
                if player.lose_life():
                    game_state = GAME_OVER
            
            player.increase_score()
            
            draw_game_objects(player, basic_enemies, advanced_enemies)
            draw_ui(player)
        
        elif game_state == GAME_OVER:
            draw_game_over(player)
            if keys[pygame.K_SPACE]:
                player = create_player()
                basic_enemies = create_basic_enemies(3)
                advanced_enemies = create_advanced_enemies(1)
                game_state = PLAYING

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
