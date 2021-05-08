"""
The file that contains all character info and actions
including enemies and the main hero.
"""
from abc import ABC, abstractmethod
import random


class Characters(ABC):
    """
    Abstract version of all character classes.
    """

    def __init__(self, model):
        """
        Abstract version of init method
        """

    def attack(self):
        """
        Abstract version of attack method
        """

    def damaged(self):
        """
        Abstract version of damaged method
        """

    def post_battle(self):
        """
        Abstract version of post_battle method
        """


class MainCharacter(Characters):
    """
    A class that holds stats and action of the hero

    Attributes:
        health: an integer representing the current health of the hero.
        mana: an integer representing the current mana of the hero.
        basic_attack_value: an integer representing the current average
            sword damage of the hero.
        magic_attack_value: an integer representing the current average
            fireball damage of the hero.
        hp_regen: an integer representing the current post battle health
            regeneration of the hero.
        mana_regen: an integer representing the current post battle mana
            regeneration of the hero.
        xp: an integer representing the current experience points of the hero.
        level: an integer representing the current level of the hero.
        max_health: an integer representing the current maximum health of
            the hero.
        max_mana: an integer representing the current maximum mana of the hero.
        escape_chance: an integer representing the basic escape chance
            of the hero.
    """

    def __init__(self):
        """
        Initial state of the hero class.
        """
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
        """
        The method that is called when player declares to attack in battle mode

        Args:
            attack_type: A string representing whether attack is a fireball
                or a slash.

        Returns:
            An integer representing how much damage hero inflicted on enemy.
        """
        # Random is used to make luck a serious factor.
        if attack_type == "sword":
            return random.randint((self.basic_attack_value -
                (self.basic_attack_value // 5)),
                (self.basic_attack_value + (self.basic_attack_value // 5)))
        elif attack_type == "fireball" and self.mana >= 40:
            self.mana -= 40
            return random.randint((self.magic_attack_value -
                (self.magic_attack_value // 5)),
                (self.magic_attack_value + (self.magic_attack_value // 5)))
        # This line makes hero to use sword when it doesn't have enough mana.
        elif attack_type == "fireball" and self.mana < 40:
            return random.randint((self.basic_attack_value -
                (self.basic_attack_value // 5)),
                (self.basic_attack_value + (self.basic_attack_value // 5)))

    def damaged(self, value):
        """
        The method that is called when the hero is attacked in battle mode

        Args:
            value: An integer representing how much damage the monster
                inflicted on the hero

        Returns:
            An string representing whether the health of hero is equal or less
                than zero. If it is less than zero it returns "Defeated".
        """
        self.health -= value
        if self.health <= 0:
            return "Defeated"
        return "Non-Defeated"

    def post_battle(self, xp):
        """
        The method that is called when a battle is won by the player. It
            levels up the hero by making it stronger.

        Args:
            xp: An integer representing how much xp the hero won from the
                battle.

        Returns:
            Nothing. Just does calculations.
        """
        self.health += self.hp_regen
        self.mana += self.mana_regen
        if self.health > self.max_health:
            self.health = self.max_health
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        self.xp += xp
        self.level_up()

    def level_up(self):
        """
        The method that is called when player declares to attack in battle mode

        Args:
            attack_type: A string representing whether attack is a fireball
                or a slash.

        Returns:
            An integer representing how much damage hero inflicted on enemy.
        """
        if self.xp >= (self.level * 100):
            self.level += 1
            self.max_health += 30
            self.max_mana += 30
            self.hp_regen += 10
            self.mana_regen += 10
            self.basic_attack_value += 10
            self.magic_attack_value += 20
            self.health += 20
            self.mana += 20
            if self.health > self.max_health:
                self.health = self.max_health
            if self.mana > self.max_mana:
                self.mana = self.max_mana
            if self.xp >= (self.level * 100):
                self.level_up()

    def escape(self, chance):
        """
        The method that is called when player tries to escape in battle mode.

        Args:
            chance: An integer representing the bonus escape chance the monster
                encountered gives to hero (it can be negative).

        Returns:
            Only True if the hero managed to escape.
        """
        percentage = self.escape_chance + chance
        if percentage >= random.randint(0, 100):
            return True


class Monster(Characters):
    """
    The general class all monster will be a part of.
    Has all the methods each monster will use.
    """
    @abstractmethod
    def __init__(self):
        """
        Just an abstract representation of what each monster will have.
        """
        self.health = 100
        self.attack_value = 20
        self.escape_chance = 0
        self.xp = 100

    def attack(self):
        """
        Returns how much damage the monster inflicted on the hero.
        """
        return random.randint((self.attack_value - (self.attack_value // 5)),\
            (self.attack_value + (self.attack_value // 5)))

    def damaged(self, value):
        """
        Calculates how much health is remaining after an attack.

        Returns:
            if the health is below 0, returns "Battle Over" and the xp gained
                by hero. Otherwise returns "battle not over".
        """
        if value is None:
            pass
        self.health -= value
        if self.health <= 0:
            return ["Battle Over", self.xp]
        return ["battle not over", 0]


class DemonLord(Monster):
    """
    The class that is holding stats for Demon Lord

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """

    def __init__(self):
        """
        Initial state of the Demon Lord.
        """
        self.name = "Demon Lord"
        self.image = "Images/Demon.png"
        self.health = 1000
        self.attack_value = 80
        self.escape_chance = -40
        self.xp = 1000


class CorruptedArchDruid(Monster):
    """
    The class that is holding stats for Corrupted Arch Druid

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Corrupted Arch Druid.
        """
        self.name = "ArchDruid"
        self.image = "Images/Druid.png"
        self.health = 120
        self.attack_value = 60
        self.escape_chance = -20
        self.xp = 100


class CorruptedElfKing(Monster):
    """
    The class that is holding stats for COrrupted Elf King

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Corrupted Elf King.
        """
        self.name = "Elf Queen"
        self.image = "Images/Elf-King.png"
        self.health = 150
        self.attack_value = 30
        self.escape_chance = 0
        self.xp = 100


class EvilRuneSmith(Monster):
    """
    The class that is holding stats for Evil Runesmith

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Evil Runesmith.
        """
        self.name = "Runesmith"
        self.image = "Images/Dwarf.png"
        self.health = 250
        self.attack_value = 20
        self.escape_chance = 20
        self.xp = 75


class GoblinChief(Monster):
    """
    The class that is holding stats for Goblin Chief

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Goblin Chief.
        """
        self.name = "Goblin Chief"
        self.image = "Images/goblin.png"
        self.health = 50
        self.attack_value = 10
        self.escape_chance = -40
        self.xp = 40


class GiantSpider(Monster):
    """
    The class that is holding stats for Giant Spider

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Giant Spider.
        """
        self.name = "Giant Spider"
        self.image = "Images/Spider.png"
        self.health = 100
        self.attack_value = 25
        self.escape_chance = -50
        self.xp = 50


class EvilBannerlord(Monster):
    """
    The class that is holding stats for Evil Bannerlord

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Evil Bannerlord.
        """
        self.name = "Bannerlord"
        self.image = "Images/Bannerlord.png"
        self.health = 150
        self.attack_value = 25
        self.escape_chance = 20
        self.xp = 60


class Spymaster(Monster):
    """
    The class that is holding stats for Spymaster

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Spymaster.
        """
        self.name = "Spymaster"
        self.image = "Images/Spymaster.png"
        self.health = 100
        self.attack_value = 20
        self.escape_chance = -40
        self.xp = 60


class IceQueen(Monster):
    """
    The class that is holding stats for Ice Queen

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Ice Queen.
        """
        self.name = "Ice Queen"
        self.image = "Images/Ice-Queen.png"
        self.health = 300
        self.attack_value = 40
        self.escape_chance = -20
        self.xp = 90


class IceGiant(Monster):
    """
    The class that is holding stats for Ice Giant

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Ice Giant.
        """
        self.name = "Ice Giant"
        self.image = "Images/Ice-Giant.png"
        self.health = 400
        self.attack_value = 40
        self.escape_chance = 50
        self.xp = 150


class OrcWarchief(Monster):
    """
    The class that is holding stats for Orc Warchief

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Orc Warchief.
        """
        self.name = 'Orc Warchief'
        self.image = "Images/Orc.png"
        self.health = 300
        self.attack_value = 60
        self.escape_chance = 20
        self.xp = 100


class IceDragon(Monster):
    """
    The class that is holding stats for Ice Dragon

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Ice Dragon.
        """
        self.name = "Ice Dragon"
        self.image = "Images/Dragon.png"
        self.health = 500
        self.attack_value = 70
        self.escape_chance = 30
        self.xp = 200


class Troll(Monster):
    """
    The class that is holding stats for Troll

    Attributes:
        name: A string representing the name of the monster which will be
            displayed during battle.
        image: A string representing the location of the image that is
            representing the monster
        health: An integer representing the current health of the monster.
        attack_value: An integer representing the average attack value of
            the monster.
        escape_chance: An integer representing the bonus escape chance the
            monster gives to the hero (can be negative).
        xp: An integer representing how much xp will the hero gain if the
            monster is killed.
    """
    def __init__(self):
        """
        Initial state of the Troll.
        """
        self.name = "Troll"
        self.image = "Images/Giant.png"
        self.health = 130
        self.attack_value = 25
        self.escape_chance = 15
        self.xp = 50
