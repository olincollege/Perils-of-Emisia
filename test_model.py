"""
Test the character classes are working correctly.
"""
from collections import Counter
import pytest
from model import MainModel


# Define sets of test cases.
get_movements = [
    # Check that movement towards positive side is working
    ([20,20], [760,560]),
    # Check that movement towards negative side is working
    ([-20,-20], [720,520]),
    # Check that when not moving, there is no error.
    ([0,0], [740,540]),
]

get_touch = [
    # Check that when character is at a encounter site, function understands it
    ([420,570], [True, 2]),
    # Check that when character is not at an encounter site, function does not
    # misinterpret it.
    ([0,0], [False, -1]),
    # Check that negative version of the coordinates of an encounter site is
    # not causing confusions.
    ([-420,-570], [False, -1]),
]


@pytest.mark.parametrize("values,result", get_movements)
def test_movement(values, result):
    """
    Test that movement method of model class is working correctly

    Args:
        values: A list of integers representing how much the character move.
        result: A list of integers representing the final coordinates of the
            character
    """
    model = MainModel()
    model.move_result(values[0], values[1])
    assert model.location_character == result

@pytest.mark.parametrize("coordinates,result", get_touch)
def test_encounter_site(coordinates, result):
    """
    Test the collision detection between the hero and encounter sites.

    Args:
        coordinates: a list of integers representing the coordinates of
            the hero on the map
        result: A list with boolean statement representing whether the hero is
            at the site or not and an integer representing which encounter site
            it is.
    """
    model = MainModel()
    model.location_character = coordinates
    assert model.check_touch() == result

def test_defeated_monster():
    """
    Test if a defeated monster's location is taken away from the encounter
    site so hero cant get into the same fight she won.
    """
    model = MainModel()
    model.current_location = 2
    model.monster_defeated()
    assert model.locations[2] == [10000,10000]

def test_check_borders_x_1():
    """
    Test if the right border of the map is really impassable by hero.
    """
    model = MainModel()
    model.location_character = [755,625]
    for _ in range(100):
        model.move_result(0.1,0)
        model.check_borders()
    assert model.location_character[0] <= 760

def test_check_borders_x_2():
    """
    Test if the right border of the map is really impassable by hero.
    """
    model = MainModel()
    model.location_character = [1,625]
    for _ in range(100):
        model.move_result(-0.1,0)
        model.check_borders()
    assert model.location_character[0] >= 0

def test_check_borders_y_1():
    """
    Test if the bottom border of the map is really impassable by hero.
    """
    model = MainModel()
    model.location_character = [755,625]
    for _ in range(100):
        model.move_result(0,0.1)
        model.check_borders()
    assert model.location_character[1] <= 630

def test_check_borders_y_2():
    """
    Test if the up border of the map is really impassable by hero.
    """
    model = MainModel()
    model.location_character = [755,1]
    for _ in range(100):
        model.move_result(0,-0.1)
        model.check_borders()
    assert model.location_character [1] >= 0
