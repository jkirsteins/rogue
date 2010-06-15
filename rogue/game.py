import pygame
import pygame.event


import world


from rogue.state.statestack import StateStack
from rogue.state.mainmenustate import MainMenuState


class Game(object):

    def __init__(self, renderer):
        self.renderer = renderer
        self.statestack = StateStack()
        self.statestack.add(MainMenuState(self.statestack))

        self.main_loop()
        
        self.statestack.unload()
        
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
		
    def main_loop(self):
        self.is_running = True
        while( self.is_running ):
            for event in pygame.event.get():
                self.handle_event(event)
            self.statestack.update()
            self.renderer.render()
        

