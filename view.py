import pygame
"""
View component of the Perils of Emisia game
"""
class HeroView():
    """
    Class that holds the written info about the hero

    Attributes:
        model: the character class that holds the info that will be displayed on
            screen.
    """
    pygame.init()

    font_stats = pygame.font.Font('freesansbold.ttf', 16)

    def __init__(self, hero):
        """
        Initial state of MapView class.
        """
        self.hero = hero

    def stats(self):
        """
        Returns a list of info text that is needed during the game.
        """
        text = [f"Current Health: {self.hero.health}",\
            f"Current Mana: {self.hero.mana}",\
            f"Sword Damage: {self.hero.basic_attack_value}",\
            f"Fireball Damage: {self.hero.magic_attack_value}",\
            f"Health Regeneration: {self.hero.hp_regen}",\
            f"Mana Regeneration: {self.hero.mana_regen}",\
            f"Current XP: {self.hero.xp}",\
            f"Level: {self.hero.level}",\
            f"Maximum Health: {self.hero.max_health}",\
            f"Maximum Mana: {self.hero.max_mana}"]
        return text

    def show_stats(self,screen):
        for i in range(10):
                stat_text = self.font_stats.render(self.stats()[i], True, (255,255,255))
                screen.blit(stat_text, (770,200+(16*i)))


class ViewActive():
    
    pygame.init()

    font_fight = pygame.font.Font('freesansbold.ttf', 32)
    font_info = pygame.font.Font('freesansbold.ttf', 20)
    font_stats = pygame.font.Font('freesansbold.ttf', 16)


    # player = pygame.image.load('Images/Warrior.png').convert_alpha()
    # map_background = pygame.image.load('Images/Emisia.jpg').convert()
    press_tab = font_info.render("Press Tab for Stats", True, (84,208,101))
    press_tab = font_info.render("Press Tab for Stats", True, (84,208,101))
    press_a = font_info.render("Press A for Slash", True, (200,200,200))
    press_s = font_info.render("Press S for Fireball (40 Mana)", True, (200,200,200))
    press_e = font_info.render("Press E to Try Escaping", True, (200,200,200))
    lose_text = font_fight.render("YOU DIED", True, (255, 10, 10))
    win_text = font_fight.render("YOU WON", True, (10,200,10))

    def __init__(self):
        pass

    def show_map_frame(self, screen, stat, hero, model, background, player):

        screen.blit(background, (0,0))
        screen.blit(player, (model.location_character))
        screen.blit(self.press_tab, (10,70))

        if stat == 1:
            hero_stats = HeroView(hero)
            hero_stats.show_stats(screen)

        pygame.display.update()

    def battle_screen(self, screen, background, player, hero, enemy, image, stat):
        screen.blit(background, (0,0))
        screen.blit(player, (100,500))
        screen.blit(image, (700,500))
        screen.blit(self.press_a, (40, 650))
        screen.blit(self.press_s, (220, 650))
        screen.blit(self.press_e, (520, 650))
        screen.blit(self.press_tab, (770, 650))

        hero_health_font = self.font_fight.render("Your Health: " +\
             str(hero.health), True, (255,255,255))
        hero_mana_font = self.font_fight.render("Your Mana: "+str(hero.mana),\
             True, (255,255,255))
        enemy_health_font = self.font_fight.render(enemy.name +\
             " Health: " + str(enemy.health), True, (230,20,20))
        screen.blit(hero_mana_font, (50,82))
        screen.blit(hero_health_font, (50,50))
        screen.blit(enemy_health_font, (500, 50))

        if stat == 1:
            hero_stats = HeroView(hero)
            hero_stats.show_stats(screen)

        # New frame
        pygame.display.update()

    def defeated(self,screen, background, player, model):

        screen.blit(background, (0,0))
        screen.blit(player, (model.location_character))
        screen.blit(self.lose_text, (450, 300))
        pygame.display.update()
        pygame.time.wait(7000)
        return False

    def win(self, screen, background, player, model):

        screen.blit(background, (0,0))
        screen.blit(player, (model.location_character))
        screen.blit(self.win_text, (450, 300))
        pygame.display.update()
        pygame.time.wait(10000)
        return False

    def hero_damage(self, screen,action, damage):

        if action == "sword":
            text = self.font_fight.render("Your sword slash dealt " +\
                str(damage) +" damage.", True, (255, 255, 255))
            screen.blit(text, (230,200))
        elif action == "fireball":
            text = self.font_fight.render("Your fireball dealt " + str(damage)\
                + " damage.", True, (255, 255, 255))
            screen.blit(text, (270,200))
        
        pygame.display.update()
        pygame.time.wait(1500)

    def monster_damage(self, screen, name, damage):
        
        text = self.font_fight.render( name + " dealt " +\
                str(damage) +" damage.", True, (255, 255, 255))
        screen.blit(text, (230,260))
        pygame.display.update()
        pygame.time.wait(1500)
    
    def escape_success(self, screen):
        
        text = self.font_fight.render("You successfully escaped!",\
            True, (255, 255, 255))
        screen.blit(text, (230,200))
        pygame.display.update()
        pygame.time.wait(1500)
    
    def escape_fail(self, screen):

        text = self.font_fight.render("You failed to escape!",\
            True, (255, 255, 255))
        screen.blit(text, (230,200))
        pygame.display.update()
        pygame.time.wait(1500)