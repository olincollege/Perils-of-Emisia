"""
Test the character classes are working correctly.
"""
from collections import Counter
import pytest

from characters import (
    MainCharacter, DemonLord
)


# Define sets of test cases.
get_hero_damaged_results = [
    # Check that when hero health is below 0, returns "Defeated"
    (120, "Defeated"),
    # Check that when hero health is above 0, returns "Non-Defeated"
    (90, "Non-Defeated"),
    # Check that when no damage is dealt, returns "Non-Defeated"
    (0, "Non-Defeated"),
    # Check that when hero health is 0, returns "Defeated"
    (100, "Defeated")
]

get_enemy_damaged_results = [
    # Check that when enemy health is below 0, returns "Battle Over" and xp
    (1020, ["Battle Over", 1000]),
    # Check that when enemy health is above 0, returns "battle not over" and 0
    (90, ["battle not over", 0]),
    # Check that when no damage is dealt, returns "battle not over" and 0
    (0, ["battle not over", 0]),
    # Check that when enemy health is 0, returns "Battle Over" and xp
    (1000, ["Battle Over", 1000])
]


@pytest.mark.parametrize("damage,result", get_hero_damaged_results)
def test_get_damaged_hero(damage, result):
    """
    Test that result of a given amount of damage dealt is correct

    Args:
        damage: An integer representing how much damage is dealt
        result: A string representing whether hero is defeated or not.
    """
    hero = MainCharacter()
    assert hero.damaged(damage) == result

@pytest.mark.parametrize("damage,result", get_enemy_damaged_results)
def test_get_damaged_monster(damage, result):
    """
    Test that result of a given amount of damage dealt is correct

    Args:
        damage: An integer representing how much damage is dealt
        result: A list with a string representing whether enemy is defeated or
            not.
    """
    enemy = DemonLord()
    assert enemy.damaged(damage) == result


def test_level_up_1():
    """
    Test whether level up function is working when it is just enough for one
    level up.
    """
    hero = MainCharacter()
    hero.post_battle(100)
    assert hero.level == 2


def test_level_up_2():
    """
    Test whether level up function is working when you get enough xp for two
    level ups after one battle.
    """
    hero = MainCharacter()
    hero.post_battle(200)
    assert hero.level == 3

def test_level_up_3():
    """
    Test whether level up function is working when a battle ends but there is
    not enough experience point to level up.
    """
    hero = MainCharacter()
    hero.post_battle(10)
    assert hero.level == 1