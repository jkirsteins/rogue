from libtcod import path_new_using_map, path_compute, path_get


from rogue.being import Being


class NPC(Being):
    """ Base class for all NPCs """
    
    def __init__(self, backend, config):
        Being.__init__(self, backend, config)
        self.path = path_new_using_map(backend.current_area.tcod_map)
        self.target_pos = None
        
    def place(self, x, y):
        res = Being.place(self, x, y)
        if not res: return
        
        if self.target_pos == None:
            self.target_pos = (self.x, self.y)
        if self.target_pos == (self.x, self.y):
            self.get_new_target()
            print "From %s to %s" % (str((self.x, self.y)), str(self.target_pos))
            path_compute(self.path, self.x, self.y, *self.target_pos)
            self.path_index = 0
        return res
    
    def update(self, delta):
        x, y = path_get(self.path, self.path_index)
        self.path_index += 1
        self.place(x,y)
    
    def get_new_target(self):
        from random import randint
        x, y = self.x, self.y
        print "Getting new target"
        while (self.x == x and self.y == y) or (not self.backend.current_area.is_walkable(x, y)):
            x = randint(0, self.backend.current_area.width - 1)
            y = randint(0, self.backend.current_area.height - 1)
            print "Trying %d %d" % (x, y)
        print "Meh"
        self.target_pos = (x, y)
        