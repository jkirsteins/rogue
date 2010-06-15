import world


class Game(object):
    def __init__(self, renderer):
        self.renderer = renderer

        self.init()
        self.main_loop()

    def init(self):
        self.load_world()

    def load_world(self):
        # Load world if already generated? etc...
        self.world = world.World()
        self.world.generate_world(128, 128, 2, 4)
    
    def main_loop(self):
        while 1:
            self.renderer.render()

