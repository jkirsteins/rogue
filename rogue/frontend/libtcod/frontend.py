import sys


import libtcod


from rogue.frontend.basefrontend import BaseFrontend


class Frontend(BaseFrontend):

    def __init__(self, game):        
        self.game = game
        
        res = self.game.config.resolution()
        libtcod.console_init_root(res[0], res[1], self.game.config.title(), False)

    def main_loop(self):
        while not libtcod.console_is_window_closed():
            libtcod.console_flush()
            key = libtcod.console_wait_for_keypress(True)
            print "Key pressed: %s" % key
            if key.vk == libtcod.KEY_ESCAPE:
                break
        print libtcod.console_is_window_closed()
        

    
