import sys


import libtcod


from rogue.frontend.basefrontend import BaseFrontend


class Frontend(BaseFrontend):

    def __init__(self, game):        
	self.game = game
	
	self.cached_map = {}
	
	res = self.game.config.resolution()
	libtcod.console_init_root(res[0], res[1], self.game.config.title(), False)

    def main_loop(self):
        while not libtcod.console_is_window_closed():
            self.render()
            libtcod.console_flush()
            
            key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
            if key != libtcod.KEY_NONE:
		self.update(key)
	    self.game.backend.update()
            
            if key.vk == libtcod.KEY_ESCAPE:
                break
    
    def update(self, key):
        x = self.game.backend.player.x
        y = self.game.backend.player.y
	if key.vk == libtcod.KEY_LEFT:
            self.game.backend.player.place(x-1, y)
        elif key.vk == libtcod.KEY_RIGHT:
            self.game.backend.player.place(x+1, y)
        elif key.vk == libtcod.KEY_UP:
            self.game.backend.player.place(x, y-1)
        elif key.vk == libtcod.KEY_DOWN:
            self.game.backend.player.place(x, y+1)
        
    
    def render(self):
        libtcod.console_clear(0)
        
        self.render_information()
        self.render_map()
        self.render_player()
	self.render_npcs()
	
    def render_npcs(self):
	npcs = self.game.backend.current_area.get_visible_npcs(self.game.backend.player)
	for npc in npcs:
	    libtcod.console_set_foreground_color(0, libtcod.red)
	    libtcod.console_put_char(0, npc.x, npc.y, 'M', libtcod.BKGND_SET)
        
    def render_map(self):
        map = self.game.backend.current_area.get_visible_parts(self.game.backend.player)
        
        outside_fov_colors = {
            '#': libtcod.Color(0, 0, 100),
            ' ': libtcod.Color(50, 50, 150),
            '=': libtcod.Color(100, 100, 100)
        }       
        
        inside_fov_colors = {
            '#': libtcod.Color(130, 110, 50),
            ' ': libtcod.Color(200, 180, 50),
            '=': libtcod.Color(255, 255, 255)
        } 

        
        y = 0
        for row in map:
            x = 0
            for v in row:
                colors = inside_fov_colors
		
		if v == '?':
		    try:
			v = self.cached_map[x, y]
			colors = outside_fov_colors
		    except KeyError:
			x += 1
			continue
		
		self.cached_map[x, y] = v
                #if libtcod.map_is_in_fov(self.game.backend.current_fov(), x, y): 
                #else:
                #    colors = outside_fov_colors
                
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

		

    
