import threading


TILE_GRASS = 0
TILE_STONE = 1
TILE_MAGMA = 2
TILE_WATER = 3


class Tile(object):
    def __init__(self, type):
        self.type = type


class World(object):
    def __init__(self):
        self.world = {}

    def get_region(self, from_xyz, to_xyz):
        tiles = []
        # FIXME: Horrible...
        for x in range(from_xyz[0], to_xyz[0], 1):
            for y in range(from_xyz[1], to_xyz[1], 1):
                for z in range(from_xyz[2], to_xyz[2]):
                    tiles.append(self.world[x, y, z])
        return tiles

    def generate_world(self, width, height, min_z, max_z):
        thread = WorldGenerationThread(self.world, width, height, min_z, max_z)
        thread.start()

    def generation_complete(self):
        self.is_generating = False


class WorldGenerationThread(threading.Thread):
    def __init__(self, parent, world, width, height, min_z, max_z):
        threading.Thread.__init__(self)

        self.parent = parent
        self.world = world
        self.width = width
        self.height = height
        self.min_z = min_z
        self.max_z = max_z

    def run(self):
        # Do work here
        print("generating world...")
        for x in range(self.width):
            for y in range(self.height):
                for z in range(self.min_z, self.max_z, 1):
                    self.world[x, y, z] = None
        print("done generating world.")

