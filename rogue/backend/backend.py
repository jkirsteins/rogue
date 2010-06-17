from datetime import datetime, timedelta


import libtcod


import rogue.world


from rogue.npc import NPC
from rogue.player import Player


from rogue.area import Area


from rogue.state.statestack import StateStack
from rogue.state.mainmenustate import MainMenuState


TEST_MAP = [
                '##############################################',
                '#######################      #################',
                '######    ###########    #     ###############',
                '###### ## ############  ###        ###########',
                '###### ## ########      #####             ####',
                '###### ## ######       ########    ###### ####',
                '######  # #####      #################### ####',
                '#######   ######    ######                  ##',
                '########   #######  ######   #     #     #  ##',
                '########   ######      ###        M         ##',
                '########                                    ##',
                '####       ######      ###   #     #     #  ##',
                '#### ###   ########## ####                  ##',
                '#### ###   ##########   ###########=##########',
                '#### ##################   #####          #####',
                '#### ###             #### #####          #####',
                '####      @    #     ####                #####',
                '########       #     #### #####          #####',
                '########       #####      ####################',
                '##############################################',
                ]


class Backend(object):

    def __init__(self, game):
    
        self.game = game
        
        self.current_area = Area(self, TEST_MAP)
        
        self.monster = NPC(self, None)
        self.monster.place(*self.current_area.monster_pos)
                
        self.player = Player(self, None)
        self.player.place(*self.current_area.player_pos)
        
        self.prev_update = datetime.now()
        self.delta = 0
        
        
    def update(self):
        """ TODO: Move the step calculation to the object being updated.
        so... sooo sleepy """
        now = datetime.now()
        delta_micro = (now - self.prev_update).microseconds
        self.delta += (delta_micro / 100000000.0)
        step = 0.5 # of a sec
        while self.delta > step:
            self.delta -= step
            self.prev_update = now
            self.monster.update(step)
        
   
                
    def current_area(self):
        """ TODO: return an Area object? """
        return self.current_area
        

