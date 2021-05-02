import pygame
from model import MapMode, BattleMode
from controller import MapController, BattleController
import characters

class MapView():

    def __init__(self, model):
        self.model = model

    def stats(self, hero):
        text = [f"Current Health: {hero.health}",f"Current Mana: {hero.mana}",\
            f"Sword Damage: {hero.basic_attack_value}",\
            f"Fireball Damage: {hero.magic_attack_value}",\
            f"Health Regeneration: {hero.hp_regen}",\
            f"Mana Regeneration: {hero.mana_regen}",\
            f"Current XP: {hero.xp}",\
            f"Level: {hero.level}",\
            f"Maximum Health: {hero.max_health}",\
            f"Maximum Mana: {hero.max_mana}"]
        
        return text