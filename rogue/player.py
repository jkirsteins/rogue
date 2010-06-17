from libtcod import map_compute_fov


from rogue.being import Being


class Player(Being):
    """ Player controllable character """
    
    def __init__(self, backend, config):
        Being.__init__(self, backend, config)
        
    
    def place(self, x, y):
        res = Being.place(self, x, y)
        if res == True:
            self.compute_fov()
        return res
        
    def compute_fov(self):
        self.fov = map_compute_fov(self.backend.current_area.tcod_map,
                                self.x,
                                self.y,
                                4)    