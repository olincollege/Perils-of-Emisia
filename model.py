"""
Model component of Perils of Emisia
"""

import math
import characters


class MainModel():
    """
    The class that will be used to store information and methods that are
    needed.

    Attributes:
        start_location: A list representing the starting location of our hero.
        locations: A list made out of lists that store the coordinate info of
            encounter sites.
        location_character: A list representing where our hero is currently.
        current_location: An integer representing whether we are on map mode
            or in a battle. if it is -1 it is map mode. Any other number is an
            encounter.
        running: The program is running when it is True. When it is False, the
            program shuts down.
        current_action: Its default is None but it changes to an integer or
            string when the player takes an action in the battle mode.
    """

    def __init__(self):
        """
        Initial state of the class.
        """
        self.start_location = [740, 540]
        self.locations = [[740, 430], [590, 350], [420, 570], [610, 145], [590, 0],
                          [220, 0], [395, 110], [345, 150],
                          [285, 270], [210, 630], [110, 550],
                          [33, 330], [25, 100]]
        self.location_character = self.start_location
        self.current_location = -1
        self.stat_visibility = 2
        self.running = True
        self.current_action = None

    def reset_current_action(self):
        """
        Resets the current action after the action is successfully made.
        """
        self.current_action = None

    def move_result(self, x_value, y_value):
        """
        Changes the location of the character depending on what is sent by
        controller compound.

        Args:
            x_value: An integer representing how much the character should move
                on x axis.
            y_value: An integer representing how much the character should move
                on y axis.
        """
        self.location_character[0] += x_value
        self.location_character[1] += y_value

    def check_touch(self):
        """
        Check if the hero icon is touching any of the encounter sites.

        Returns:
            A list with first element being True or False depending on if
            the character is touching any encounter site. The second element
            is the location number of the touched encounter site, if the hero
            is nouching nowhere, return -1
        """
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

    def monster_defeated(self):
        """
        If the enemy is defeated, change its encounter site's coordinates to
        somewhere out of map so none of the encounters are repeated.
        Also change the current_location so the game goes back to map mode.
        """
        self.locations[self.current_location] = [10000, 10000]
        self.current_location = -1

    def check_borders(self):
        """
        Check where the character is and if the character is trying to move
        out of the map, don't allow it.
        """
        if self.location_character[0] <= 0:
            self.move_result(1, 0)
        if self.location_character[1] <= 0:
            self.move_result(0, 1)
        if self.location_character[1] >= 630:
            self.move_result(0, -1)
        if self.location_character[0] >= 760:
            self.move_result(-1, 0)

    def check_final_battle(self):
        """
        Check if the battle won was the final battle.

        Returns:
            If it was final battle, return True.
        """
        if self.current_location == 12:
            return True
        return False

    def change_stat_visibility(self, check):
        """
        Changes the stat_visibility from its current state.
        """
        if check == 1:
            self.stat_visibility = 1
        if check == 2:
            self.stat_visibility = 2

    def choose_monster(self):
        """
        Choose which monster will be faced in the current encounter site.

        Returns:
            The class of the current enemy that will be faced by the hero.
        """
        monster_manual = {0: characters.GoblinChief(),
                          1: characters.Troll(), 2: characters.Spymaster(),
                          3: characters.EvilRuneSmith(), 4: characters.IceQueen(),
                          5: characters.IceDragon(), 6: characters.IceGiant(),
                          7: characters.GiantSpider(), 8: characters.EvilBannerlord(),
                          9: characters.CorruptedElfKing(),
                          10: characters.CorruptedArchDruid(), 11: characters.OrcWarchief(),
                          12: characters.DemonLord()}
        return monster_manual[self.current_location]
