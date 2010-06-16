
from rogue.backend.backend import Backend
from rogue.factory import FrontendFactory


class Game(object):

    def __init__(self, config):
        
        self.config = config
        
        self.config.set("__metadata__", "name", "amazorogue")
        self.config.set("__metadata__", "version", "0.1")
        
        self.backend = Backend(self)
        self.frontend = FrontendFactory(self, self.config.frontend_name())
        
    def run(self):
        self.frontend.main_loop()