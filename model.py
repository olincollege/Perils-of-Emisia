"""

"""

import pygame
import math
import characters

class MapMode():
    """
    """

    def __init__(self):
        self.start_location = [740,540]
        self.locations = [[740,430],[590,350],[420,570],[610,145], [590,0],\
            [220,0], [395,110], [345,150], [285,270], [210,630], [110,550],\
                 [33,330], [25,100]]
        self.defeated_monsters = []
        self.location_character = self.start_location

    def move_result(self, x_value, y_value):
        self.location_character[0] += x_value
        self.location_character[1] += y_value

    def frames(self, background, player, screen):
        screen.blit(background, (0,0))
        screen.blit(player, \
            (self.location_character[0],self.location_character[1]))
        pygame.display.update()

    def check_touch(self):
        x_1 = self.location_character[0]
        y_1 = self.location_character[1]
        location_number = -1
        for element in self.locations:
            location_number += 1
            x_2 = element[0]
            y_2 = element[1]
            if math.sqrt(((x_1 - x_2)**2)+((y_1 - y_2)**2)) <= 30:
                return [True, location_number]
                    
        return [False, -1]

    def monster_defeated(self, location_number):
        self.locations[location_number] = [10000, 10000]
        return -1



class BattleMode:


    def __init__(self, monster_number):
        self.monster_number = monster_number
        self.monster_manual = {0: characters.GoblinChief(),\
            1: characters.Troll(), 2: characters.Spymaster(),\
            3: characters.EvilRuneSmith(), 4: characters.IceQueen(),\
            5: characters.IceDragon(), 6: characters.IceGiant(),\
            7: characters.GiantSpider(), 8: characters.EvilBannerlord(),\
            9: characters.CorruptedElfKing(),\
            10: characters.CorruptedArchDruid(), 11: characters.OrcWarchief(),\
            12: characters.DemonLord()}
        self.current_enemy = self.monster_manual[self.monster_number]
    