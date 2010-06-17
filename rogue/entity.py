
class Entity(object):
    """
    Base class for world entities. Contains basic shared information
    such as position.
    """
    
    def __init__(self, backend):
        self.backend = backend
        
        self.x = 0
        self.y = 0