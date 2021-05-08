"""
Control component of the Perils of Emisia game.
"""
import pygame

# Pylint score of this file is extremely low because pylint thinks pygame
# doesn't have any key methods but it is wrong and I don't know how to solve
# that problem. Please disregard that.

class Controller():
    """
    The class that will be used to interpret user input during the map phase.

    Attributes:
        _model: A class which is a part of the model component.
    """
    def __init__(self, model):
        """
        Initial state of the MapController class.
        """
        self._model = model

    def move_control(self, event):
        """
        The method that takes arrow key inputs and returns which direction
        should the character icon move.

        Args:
            event: it is a pygame event component which contains the info of
                what input is entered by the user.

        Returns:
            A list of x and y coordinates representing how much the character
                icon should move on the map.

        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return [-0.1, 0]
            if event.key == pygame.K_RIGHT:
                return [0.1, 0]
            if event.key == pygame.K_UP:
                return [0, -0.1]
            if event.key == pygame.K_DOWN:
                return [0, 0.1]
        elif event.type == pygame.KEYUP:
            return [0, 0]
        return [0,0]

    def show_stats(self, event):
        """
        Checks whether the user is pressing tab and if the user is pressing
        tab, returns and integer to change the visibility of stats.

        Args:
            event: it is a pygame event component which contains the info of
                what input is entered by the user.

        Returns:
            An integer. if the tab is pressed, returns 1, if tab button is
                released, returns 2 and if user did nothing with tab button,
                returns 0.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                return 1
        elif event.type == pygame.KEYUP:
            return 2
        return 0

    def action_chioce(self, event, stat_visibility):
        """
        Checks what action did the user choose to do.

        Args:
            event: it is a pygame event component which contains the info of
                what input is entered by the user.
            stat_visibility: It is an integer representing whether the stats
                are visible on screen or not.

        Returns:
            An integer or a string depending on what action is taken. Or None
            if the user didn't do anything.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                return "sword"
            elif event.key == pygame.K_s:
                return "fireball"
            elif event.key == pygame.K_e:
                return "escape"
            elif event.key == pygame.K_TAB:
                if stat_visibility == 1:
                    return 2
                elif stat_visibility == 2:
                    return 1
            else:
                return None

