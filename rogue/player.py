import libtcod


class Player(object):
    
    def __init__(self, backend):
        self.x = 0
        self.y = 0
        self.fov_radius = 5
        self.backend = backend
        
    def move(self, dx, dy):
        if self.backend.can_move(self.x + dx, self.y + dy):
            self.x, self.y = self.x + dx, self.y + dy
        self.backend.recompute_fov()
        
    def move_up(self):
        self.move(0, -1)
        
    def move_down(self):
        self.move(0, 1)
        
    def move_right(self):
        self.move(1, 0)
        
    def move_left(self):
        self.move(-1, 0)