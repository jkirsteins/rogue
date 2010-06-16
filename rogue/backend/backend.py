import pygame
import pygame.event


import rogue.world


from rogue.state.statestack import StateStack
from rogue.state.mainmenustate import MainMenuState


class Backend(object):

    def __init__(self, game):
    
        self.game = game
        #self.statestack = StateStack()
        #self.statestack.add(MainMenuState(self.statestack))

        

