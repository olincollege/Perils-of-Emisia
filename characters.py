"""
Docstring
"""
from abc import ABC, abstractmethod
import random

class Characters(ABC):
    """

    """

    def __init__(self, model):
        pass

    def attack(self):
        pass

    def damaged(self):
        pass

    def post_battle(self):
        pass


class MainCharacter(Characters):

    def __init__(self):
        self.health = 100
        self.mana = 100
        self.basic_attack_value = 25
        self.magic_attack_value = 40
        self.hp_regen = 30
        self.mana_regen = 30
        self.xp = 0
        self.level = 1
        self.max_health = 100
        self.max_mana = 100
        self.escape_chance = 50
    
    def attack(self, attack_type):
        if attack_type == "sword":
            return random.randint((self.basic_attack_value - 5),\
                (self.basic_attack_value + 5))
        elif attack_type == "fireball" and self.mana >= 40:
            self.mana -= 40
            return random.randint((self.magic_attack_value - 5),\
                (self.magic_attack_value + 5))
        elif attack_type == "fireball" and self.mana < 40:
            return random.randint((self.basic_attack_value - 5),\
                (self.basic_attack_value + 5))

    def damaged(self, value):
        self.health -= value
        if self.health <= 0:
            return "Defeated"
        return "Non-Defeated"

    def post_battle(self, xp):
        self.health += 30
        self.mana += 20
        if self.health > self.max_health:
            self.health = self.max_health
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        self.xp += xp

    def level_up(self):
        if self.xp >= (self.level * 100):
            self.level += 1
            self.max_health += 30
            self.max_mana += 30
            self.basic_attack_value += 10
            self.magic_attack_value += 20
            self.health += 20
            self.mana += 20
            if self.xp >= (self.level * 100):
                self.level_up()
            return True
    
    def escape(self, chance):
        percentage = self.escape_chance + chance
        if percentage >= random.randint(0, 100):
            return True


class Monster(Characters):

    def __init__(self):
        self.health = 100
        self.attack_value = 20
        self.escape_chance = 0
        self.xp = 100

    def attack(self):
        return random.randint((self.attack_value - 5), (self.attack_value + 5))

    def damaged(self, value):
        print(value)
        if value == None:
            pass
        self.health -= value
        if self.health <= 0:
            return ["Battle Over", self.xp]
        return ["battle not over", 0]


class DemonLord(Monster):

    def __init__(self):
        self.name = "Demon Lord"
        self.image = "Images/Demon.png"
        self.health = 300
        self.attack_value = 50
        self.escape_chance = -40
        self.xp = 1000


class CorruptedArchDruid(Monster):

    def __init__(self):
        self.name = "ArchDruid"
        self.image = "Images/Druid.png"
        self.health = 120
        self.attack_value = 30
        self.escape_chance = -20
        self.xp = 100


class CorruptedElfKing(Monster):

    def __init__(self):
        self.name = "Elf Queen"
        self.image = "Images/Elf-King.png"
        self.health = 150
        self.attack_value = 20
        self.escape_chance = 0
        self.xp = 100


class EvilRuneSmith(Monster):

    def __init__(self):
        self.name = "Runesmith"
        self.image = "Images/Dwarf.png"
        self.health = 200
        self.attack_value = 20
        self.escape_chance = 20
        self.xp = 75


class GoblinChief(Monster):

    def __init__(self):
        self.name = "Goblin Chief"
        self.image = "Images/goblin.png"
        self.health = 50
        self.attack_value = 10
        self.escape_chance = -40
        self.xp = 40


class GiantSpider(Monster):

    def __init__(self):
        self.name = "Giant Spider"
        self.image = "Images/Spider.png"
        self.health = 100
        self.attack_value = 25
        self.escape_chance = -50
        self.xp = 50


class EvilBannerlord(Monster):

    def __init__(self):
        self.name = "Bannerlord"
        self.image = "Images/Bannerlord.png"
        self.health = 100
        self.attack_value = 25
        self.escape_chance = 20
        self.xp = 60


class Spymaster(Monster):

    def __init__(self):
        self.name = "Spymaster"
        self.image = "Images/Spymaster.png"
        self.health = 100
        self.attack_value = 20
        self.escape_chance = -40
        self.xp = 60


class IceQueen(Monster):

    def __init__(self):
        self.name = "Ice Queen"
        self.image = "Images/Ice-Queen.png"
        self.health = 150
        self.attack_value = 30
        self.escape_chance = -20
        self.xp = 90


class IceGiant(Monster):

    def __init__(self):
        self.name = "Ice Giant"
        self.image = "Images/Ice-Giant.png"
        self.health = 300
        self.attack_value = 20
        self.escape_chance = 50
        self.xp = 150


class OrcWarchief(Monster):

    def __init__(self):
        self.name = 'Orc Warchief'
        self.image = "Images/Orc.png"
        self.health = 200
        self.attack_value = 30
        self.escape_chance = 20
        self.xp = 100


class IceDragon(Monster):

    def __init__(self):
        self.name = "Ice Dragon"
        self.image = "Images/Dragon.png"
        self.health = 300
        self.attack_value = 40
        self.escape_chance = 30
        self.xp = 200


class Troll(Monster):

    def __init__(self):
        self.name = "Troll"
        self.image = "Images/Giant.png"
        self.health = 130
        self.attack_value = 20
        self.escape_chance = 15
        self.xp = 50
        