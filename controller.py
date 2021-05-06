"""

"""
import pygame

class MapController():

    def __init__(self, model):
        self._model = model

    def model(self):
        return self._model

    def event_control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return [False, [], 0]
            # Player inputs
            movement = self.move_control(event)
            CHECK_STATS = self.show_stats(event)
            return [True, movement, CHECK_STATS]
    
    
    def move_control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return [-0.1, 0]
            if event.key == pygame.K_RIGHT:
                return [0.1, 0]
            if event.key == pygame.K_UP:
                return [0, -0.1]
            if event.key == pygame.K_DOWN:
                return [0, 0.1]
            if event.key == pygame.K_a:
                return [-0.1, 0]
        elif event.type == pygame.KEYUP:
            return [0, 0]
        return [0,0]
    
    def show_stats(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                return 1
        elif event.type == pygame.KEYUP:
            return 2
        return 0


class BattleController():

    def __init__(self, model):
        self.model = model

    def action_chioce(self, event, stat_visibility):
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
        