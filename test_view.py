"""
View component of the Perils of Emisia game
"""
import pygame

class HeroView():
    """
    Class that holds the written info about the hero

    Attributes:
        font_stats: A pygame font.
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
        Returns a list of stat info text.
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
        """
        Writes the desired stats info on the screen

        Args:
            screen: It is the screen component of pygame.
        """
        for i in range(10):
            stat_text = self.font_stats.render(self.stats()[i], True, (255,255,255))
            screen.blit(stat_text, (770,200+(16*i)))


class ViewActive():
    """
    View class that draws all the visuals except hero stats.

    Attributes:
        font_fight: A pygame font with the size of 32.
        font_info: A pygame font with the size of 20.
        font_stats: A pygame font with the size of 16.
        press_tab: A pygame render to be shown during battle.
        press_a: A pygame render to be shown during battle.
        press_s: A pygame render to be shown during battle.
        press_e: A pygame render to be shown during battle.
        lose_text: A pygame render to be shown if you lose the game.
        win_text: A pygame render to be shown if you win the game.
        model: Model class of the main game.
    """
    pygame.init()

    font_fight = pygame.font.Font('freesansbold.ttf', 32)
    font_info = pygame.font.Font('freesansbold.ttf', 20)
    font_stats = pygame.font.Font('freesansbold.ttf', 16)

    press_tab = font_info.render("Press Tab for Stats", True, (84,208,101))
    press_a = font_info.render("Press A for Slash", True, (200,200,200))
    press_s = font_info.render("Press S for Fireball (40 Mana)", True, (200,200,200))
    press_e = font_info.render("Press E to Try Escaping", True, (200,200,200))
    lose_text = font_fight.render("YOU DIED", True, (255, 10, 10))
    win_text = font_fight.render("YOU WON", True, (10,200,10))

    def __init__(self, model):
        """
        I dont know if a __init__ method is necesarry so I made one just
        in case.
        """
        self.model = model


    def show_map_frame(self, screen, hero, background, player):
        """
        Draws each frame of the map phase.

        Args:
            screen: A pygame screen compound
            hero: The character class for the hero
            background: The background image of map
            player: An image representing the hero
        """

        screen.blit(background, (0,0))
        screen.blit(player, (self.model.location_character))
        screen.blit(self.press_tab, (10,70))

        if self.model.stat_visibility == 1:
            hero_stats = HeroView(hero)
            hero_stats.show_stats(screen)

        pygame.display.update()

    def battle_screen(self, screen, background, player, hero, enemy, image):
        """
        Draws each frame of the battle stage

        Args:
            screen: A pygame screen compound
            hero: The character class for the hero
            background: The background image
            player: An image representing the hero
            enemy: A class representing the current enemy
            image: An image representin the current enemy
        """
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

        if self.model.stat_visibility == 1:
            hero_stats = HeroView(hero)
            hero_stats.show_stats(screen)

        # New frame
        pygame.display.update()

    def defeated(self,screen, background, player, model):
        """
        Draws the screen that you see when you lose.

        Args:
            screen: A pygame screen compound
            model: The model class of the game
            background: The background image
            player: An image representing the hero

        Returns:
            Returns False so the game window closes.
        """
        screen.blit(background, (0,0))
        screen.blit(player, (model.location_character))
        screen.blit(self.lose_text, (450, 300))
        pygame.display.update()
        pygame.time.wait(7000)
        return False

    def win(self, screen, background, player, model):
        """
        Draws the screen that you see when you win.

        Args:
            screen: A pygame screen compound
            model: The model class of the game
            background: The background image
            player: An image representing the hero

        Returns:
            Returns False so the game window closes.
        """
        screen.blit(background, (0,0))
        screen.blit(player, (model.location_character))
        screen.blit(self.win_text, (450, 300))
        pygame.display.update()
        pygame.time.wait(10000)
        return False

    def hero_damage(self, screen,action, damage):
        """
        Draws the written description of hero's attack

        Args:
            screen: Pygame screen component.
            action: A string representing which action is taken by the player.
            damage: An integer representing how much damage the hero dealt.
        """
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
        """
        Draws a written description of how much damage the enemy dealt on hero.

        Args:
            screen: Pygame screen component.
            name: A string representin the name of the enemy.
            damage: An integer representin how much damage is dealt on hero.
        """

        text = self.font_fight.render( name + " dealt " +\
                str(damage) +" damage.", True, (255, 255, 255))
        screen.blit(text, (230,260))
        pygame.display.update()
        pygame.time.wait(1500)

    def escape_success(self, screen):
        """
        Draws the information text when the hero successfully escapes
        the battle.

        Args:
            screen: Pygame screen component.
        """
        text = self.font_fight.render("You successfully escaped!",\
            True, (255, 255, 255))
        screen.blit(text, (230,200))
        pygame.display.update()
        pygame.time.wait(1500)

    def escape_fail(self, screen):
        """
        Draws the information text when the hero fails to escape.

        Args:
            screen: Pygame screen component.
        """

        text = self.font_fight.render("You failed to escape!",\
            True, (255, 255, 255))
        screen.blit(text, (230,200))
        pygame.display.update()
        pygame.time.wait(1500)
