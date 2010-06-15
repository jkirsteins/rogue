
class BaseState(object):
	
    def __init__(self, stack):
        """ Initializes the state """
        self.stack = stack
        self.is_loaded = False
		
    def load_content(self):
        """ Performs load tasks associated with this state """
        print "Loading content"
        pass
		
    def unload_content(self):
        """ Performs unloading tasks associated with this state """
        print "Unloading content"
        pass
        
    def loading_func(self):
        """ 
        Callback that is used while loading this state. Do not rely on data that has
        to be loaded with load_content here
        """
        pass
        
    def handle_added(self):
        """ Callback for when the state is added to the stack (after loading) """
        pass
		
    def exit(self):
        """ Initiates state removal from the stack """
        stack.remove(self)
		
    def update(self):
        """ Updates the state """
        pass
		
	