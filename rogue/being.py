from libtcod import map_compute_fov


from rogue.entity import Entity


class Being(Entity):
    """
    Base class for living creatures. Contains shared information such
    as FOV, etc.
    """
    
    def __init__(self, backend, config):
        Entity.__init__(self, backend)
        
        self.config = config
        
    def place(self, x, y):
        if self.backend.current_area.is_walkable(x, y):
            self.x = x
            self.y = y
            return True
        return False

        

    
    