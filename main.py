import pygame
from model import MapMode, BattleMode
from controller import MapController, BattleController
from view import MapView
import characters

pygame.init()

map_model = MapMode()
map_controller = MapController(map_model)
map_view = MapView(map_model)
hero = characters.MainCharacter()

font_fight = pygame.font.Font('freesansbold.ttf', 32)
font_info = pygame.font.Font('freesansbold.ttf', 20)
font_stats = pygame.font.Font('freesansbold.ttf', 16)

running = True
stat_visibility = 2
location = -1
screen = pygame.display.set_mode((988, 739))

press_tab = font_info.render("Press Tab for Stats", True, (84,208,101))
press_a = font_info.render("Press A for Slash", True, (200,200,200))
press_s = font_info.render("Press S for Fireball (40 Mana)", True, (200,200,200))
press_e = font_info.render("Press E to Try Escaping", True, (200,200,200))
lose_text = font_fight.render("YOU DIED", True, (255, 10, 10))
win_text = font_fight.render("YOU WON", True, (10,200,10))

player = pygame.image.load('Images/Warrior.png').convert_alpha()
map_background = pygame.image.load('Images/Emisia.jpg').convert()
battle_background = pygame.image.load('Images/battle.png').convert()

while running:
    if location == -1:
        screen.blit(map_background, (0,0))
        screen.blit(player, (map_model.location_character))
        screen.blit(press_tab, (10,70))
        
        if stat_visibility == 1:
            for i in range(9):
                stat_text = font_stats.render(map_view.stats(hero)[i], True, (255,255,255))
                screen.blit(stat_text, (770,200+(16*i)))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            movement = map_controller.move_control(event)
            check_stats = map_controller.show_stats(event)
            # switch_fullscreen = map_controller.fullscreen(event)
            # if switch_fullscreen == True:
            #     pygame.display.toggle_fullscreen()
        
            if check_stats == 1:
                stat_visibility = 1
            elif check_stats == 2:
                stat_visibility = 2
                pygame.display.update()

        map_model.check_borders()
        map_model.move_result(movement[0], movement[1])
        
        touch = map_model.check_touch()
        if touch[0] == True:
            location = touch[1]
            current_battle = BattleMode(location)
            battle_controller = BattleController(current_battle)
            current_enemy = current_battle.current_enemy
            enemy_image = pygame.image.load(current_enemy.image).convert()
        
            pygame.time.wait(1000)
    else:
        screen.blit(battle_background, (0,0))
        screen.blit(player, (100,500))
        screen.blit(enemy_image, (700,500))
        
        hero_health_font = font_fight.render("Your Health: " +\
             str(hero.health), True, (255,255,255))
        hero_mana_font = font_fight.render("Your Mana: "+str(hero.mana),\
             True, (255,255,255))
        enemy_health_font = font_fight.render(current_enemy.name +\
             " Health: " + str(current_enemy.health), True, (230,20,20))
        screen.blit(press_a, (40, 650))
        screen.blit(press_s, (220, 650))
        screen.blit(press_e, (520, 650))
        screen.blit(press_tab, (770, 650))
        screen.blit(hero_mana_font, (50,82))
        screen.blit(hero_health_font, (50,50))
        screen.blit(enemy_health_font, (500, 50))

        if stat_visibility == 1:
            for i in range(9):
                stat_text = font_stats.render(map_view.stats(hero)[i], True, (255,255,255))
                screen.blit(stat_text, (770,200+(16*i)))
        
        pygame.display.update()
        
        real_action = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            action = battle_controller.action_chioce(event, stat_visibility)
            if action != None:
                real_action = action
                # print(real_action)
                
        if real_action != None:
            if real_action == "sword" or "fireball":
                if real_action not in ["sword", "fireball"]:
                    print("empty")
                else: 
                    hero_damage = hero.attack(real_action)
                    result = current_enemy.damaged(hero_damage)
                    if result[0] == "Battle Over":
                        hero.post_battle(result[1])
                        hero.level_up()
                        map_model.monster_defeated(location)
                        
                        if map_model.check_final_battle(location):
                            screen.blit(map_background, (0,0))
                            screen.blit(player, (map_model.location_character))
                            screen.blit(win_text, (450, 300))
                            pygame.display.update()
                            pygame.time.wait(10000)
                            running = False
                        
                        location = -1
                    elif result[0] == "battle not over":
                        enemy_damage = current_enemy.attack()
                        damaged_result = hero.damaged(enemy_damage)
                        
                        if damaged_result == "Defeated":
                            screen.blit(map_background, (0,0))
                            screen.blit(player, (map_model.location_character))
                            screen.blit(lose_text, (450, 300))
                            pygame.display.update()
                            pygame.time.wait(10000)
                            running = False
            if real_action == "escape":
                escape = hero.escape(current_enemy.escape_chance)
                if escape == True:
                    location = -1
                    map_model.move_result(30, 30)
                    continue
                enemy_damage = current_enemy.attack()
                damaged_result = hero.damaged(enemy_damage)
                
                if damaged_result == "Defeated":
                    screen.blit(map_background, (0,0))
                    screen.blit(player, (map_model.location_character))
                    screen.blit(lose_text, (450, 300))
                    pygame.display.update()
                    pygame.time.wait(10000)
                    running = False
            if real_action == 1: 
                # print("stats")
                stat_visibility = real_action
            if real_action == 2:
                stat_visibility = real_action
        print(stat_visibility)
            

            
