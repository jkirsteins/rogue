import libtcod


import rogue.world


from rogue.player import Player


from rogue.state.statestack import StateStack
from rogue.state.mainmenustate import MainMenuState


class Backend(object):

    def __init__(self, game):
    
        self.game = game
        self.player = Player(self)
        
        self.current_map = [
                '##############################################',
                '#######################      #################',
                '######    ###########    #     ###############',
                '###### ## ############  ###        ###########',
                '###### ## ########      #####             ####',
                '###### ## ######       ########    ###### ####',
                '######  # #####      #################### ####',
                '#######   ######    ######                  ##',
                '########   #######  ######   #     #     #  ##',
                '########   ######      ###                  ##',
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
        
        
        map = self.current_area()
        found = False
        for y in xrange(len(map)):
            row = map[y]
            for x in xrange(len(row)):
                if map[y][x] == '@':
                    self.player.x, self.player.y = x, y
                    map[y] = map[y].replace("@", ' ')
                    found = True
                    break
            if found: break
        self.current_map = map
        #self.statestack = StateStack()
        #self.statestack.add(MainMenuState(self.statestack))

    def can_move(self, x, y):
        """ TODO: move this into an Area class """
        return self.current_area()[y][x] == ' '
        
    def current_fov(self):
        """ TODO: to be less ridiculous """
        try:
            res = self.fov
        except:
            map = self.current_area()
            w = len(map[0])
            h = len(map)
            self.fov = libtcod.map_new(w, h)
            for y in range(h):
                for x in range(w):
                    if map[y][x] == ' ':
                        libtcod.map_set_properties(self.fov, x, y, True, True)
                    elif map[y][x] == '=':
                        libtcod.map_set_properties(self.fov, x, y, True, False)
            res = self.fov
            self.recompute_fov()
        return self.fov
        
    def recompute_fov(self):
        libtcod.map_compute_fov(self.current_fov(), self.player.x, self.player.y, 
                                self.player.fov_radius, True)
        
        
    def current_area(self):
        """ TODO: return an Area object? """
        return self.current_map
        

