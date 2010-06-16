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
            self.render()
            libtcod.console_flush()
            
            key = libtcod.console_wait_for_keypress(True)
            self.update(key)
            
            if key.vk == libtcod.KEY_ESCAPE:
                break
    
    def update(self, key):
        if key.vk == libtcod.KEY_LEFT:
            self.game.backend.player.move_left()
        elif key.vk == libtcod.KEY_RIGHT:
            self.game.backend.player.move_right()
        elif key.vk == libtcod.KEY_UP:
            self.game.backend.player.move_up()
        elif key.vk == libtcod.KEY_DOWN:
            self.game.backend.player.move_down()
        
    
    def render(self):
        libtcod.console_clear(0)
        
        self.render_information()
        self.render_map()
        self.render_player()
        
    def render_map(self):
        map = self.game.backend.current_area()
        
        outside_fov_colors = {
            '#': libtcod.Color(0, 0, 100),
            ' ': libtcod.Color(50, 50, 150),
            '=': libtcod.Color(100, 100, 100),
        }       
        
        inside_fov_colors = {
            '#': libtcod.Color(130, 110, 50),
            ' ': libtcod.Color(200, 180, 50),
            '=': libtcod.Color(255, 255, 255),
        } 

        
        y = 0
        for row in map:
            x = 0
            for v in row:
                if libtcod.map_is_in_fov(self.game.backend.current_fov(), x, y): 
                    colors = inside_fov_colors
                else:
                    colors = outside_fov_colors
                
                libtcod.console_set_foreground_color(0, colors[v])
                if v == ' ':
                    libtcod.console_put_char(0, x, y, '.', libtcod.BKGND_SET)
                else:
                    #libtcod.console_set_foreground_color(0, colors[v])
                    #libtcod.console_set_foreground_color(0, colors[v])
                    libtcod.console_put_char(0, x, y, v, libtcod.BKGND_SET)
                x += 1
            y += 1
        
    def render_information(self):
        libtcod.console_set_foreground_color(0, libtcod.white)
        libtcod.console_print_left(0, 1, 1, libtcod.BKGND_NONE,
                    "move around with the arrow keys")
        
    def render_player(self):
        player = self.game.backend.player
        
        libtcod.console_set_foreground_color(0, libtcod.yellow)
        libtcod.console_put_char(0, 
                                 player.x, 
                                 player.y, 
                                 '@',
                                 libtcod.BKGND_NONE)
        pass

		

    
