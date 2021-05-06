"""
The main file of Perils of Emisia game.
"""

import pygame
from model import MapMode, BattleMode
from controller import MapController, BattleController
from view import HeroView, ViewActive
import characters

# Initiates Pygame module
pygame.init()

# Set up classes
map_model = MapMode()
map_controller = MapController(map_model)
view = ViewActive()
hero = characters.MainCharacter()

# Set the pygame screen size
screen = pygame.display.set_mode((988, 739))

# Set the hero image and background images
player = pygame.image.load('Images/Warrior.png').convert_alpha()
map_background = pygame.image.load('Images/Emisia.jpg').convert()
battle_background = pygame.image.load('Images/battle.png').convert()

while map_model.running:
    # Map Mode
    if map_model.current_location == -1:
        # Prepare what will be on screen each frame
        view.show_map_frame(screen, map_model.stat_visibility, hero, map_model, map_background, player)

        # Quit function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map_model.running = False
            # Player inputs
            movement = map_controller.move_control(event)
            CHECK_STATS = map_controller.show_stats(event)

            # When map_model.stat_visibility is 1, hero stats are visible on screen.
        if CHECK_STATS == 1 or 2:
            map_model.change_stat_visibility(CHECK_STATS)

        # Hero movements handled here
        map_model.check_borders()
        map_model.move_result(movement[0], movement[1])

        # Check if hero is on an encounter site
        touch = map_model.check_touch()
        if touch[0]:
            # Check which monster is encountered
            map_model.current_location = touch[1]
            # Setup for the battle
            current_battle = BattleMode(map_model.current_location)
            battle_controller = BattleController(current_battle)
            current_enemy = current_battle.current_enemy
            enemy_image = pygame.image.load(current_enemy.image).convert()

            pygame.time.wait(1000)
    # Battle Mode
    else:
        view.battle_screen(screen, battle_background, player, hero,\
             current_enemy, enemy_image, map_model.stat_visibility)

        map_model.reset_current_action()

        # Get player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map_model.running = False
            action = battle_controller.action_chioce(event, map_model.stat_visibility)
            if action is not None:
                map_model.current_action = action

        #The result of the player's action
        if map_model.current_action is not None:
            if map_model.current_action == "sword" or "fireball":
                if map_model.current_action not in ["sword", "fireball"]:
                    print("")
                # If hero attacked.
                else:
                    hero_damage = hero.attack(map_model.current_action)
                    result = current_enemy.damaged(hero_damage)
                    view.hero_damage(screen, map_model.current_action, hero_damage)
                    # If hero killed the monster.
                    if result[0] == "Battle Over":
                        hero.post_battle(result[1])
                        map_model.monster_defeated(map_model.current_location)
                        # If it was final battle with demon.
                        if map_model.check_final_battle(map_model.current_location):
                            map_model.running = view.win(screen, map_background,\
                                 player, map_model)

                        map_model.current_location = -1
                    # If hero is still alive
                    elif result[0] == "battle not over":
                        enemy_damage = current_enemy.attack()
                        view.monster_damage(screen, current_enemy.name, enemy_damage)
                        DAMAGED_RESULT = hero.damaged(enemy_damage)
                        # If monster killed the hero
                        if DAMAGED_RESULT == "Defeated":
                            map_model.running = view.defeated(screen,\
                                 map_background, player, map_model)
            # If player tried to escape
            if map_model.current_action == "escape":
                ESCAPE = hero.escape(current_enemy.escape_chance)
                # If successfully escaped
                if ESCAPE:
                    view.escape_success(screen)
                    map_model.current_location = -1
                    map_model.move_result(30, 30)
                    continue
                # If couldn't escape
                view.escape_fail(screen)
                enemy_damage = current_enemy.attack()
                view.monster_damage(screen, current_enemy.name, enemy_damage)
                DAMAGED_RESULT = hero.damaged(enemy_damage)
                # if monster killed the hero
                if DAMAGED_RESULT == "Defeated":
                    map_model.running = view.defeated(screen, map_background, player,\
                         map_model) 
            # Stat visibility
            if map_model.current_action == 1 or 2:
                map_model.change_stat_visibility(map_model.current_action)
