from libtcod import map_new, map_set_properties, map_is_in_fov


class Area(object):
    """ Class representing a bounded region (like a dungeon level) """
    
    def __init__(self, backend, map_data):
        """ Initialize an area with given data """
        self.backend = backend
        
        self.width = len(map_data[0])
        self.height = len(map_data)
        
        self.raw_map = map_data
        self.strip_raw_metadata()
        
        self.build_tcod_map()
        
    def get_visible_npcs(self, being):
        """ Returns NPCs visible from a given being's viewpoint """
        monster = self.backend.monster
        if map_is_in_fov(self.tcod_map, monster.x, monster.y):
            return [monster]
        else:
            return []
        
    def get_visible_parts(self, being):
        """ Returns information about the visible parts of the area around
        the being """
        res = []
        for y in xrange(self.height):
            row = ""
            for x in xrange(self.width):
                if map_is_in_fov(self.tcod_map, x, y):
                    row += self.raw_map[y][x]
                else:
                    row += '?'
            res.append(row)
        return res
        
    def strip_raw_metadata(self):
        """
        Removes metadata symbols from the raw map data and sets
        the relevant properties based on them.
        """
        for y in xrange(self.height):
            for x in xrange(self.width):
                val = self.raw_map[y][x]
                if val == '@':
                    self.raw_map[y] = self.raw_map[y].replace('@', ' ')
                    self.player_pos = (x, y)
                if val == 'M':
                    self.raw_map[y] = self.raw_map[y].replace('M', ' ')
                    self.monster_pos = (x, y)
        
    def is_walkable(self, x, y):
        """ Tests if a given coordinate is walkable """
        return True if self.raw_map[y][x] == ' ' else False
        
    def build_tcod_map(self):
        """
        Function builds a TCOD map from self.raw_map, treating
        ' ' as transparent and walkable, and all other chars
        as non-transparent and non-walkable (temp convention)
        """
        self.tcod_map = map_new(self.width, self.height)
        for y in xrange(self.height):
            for x in xrange(self.width):
                walkable = self.is_walkable(x, y)
                transparent = walkable
                map_set_properties(self.tcod_map, x, y, transparent, walkable)
        