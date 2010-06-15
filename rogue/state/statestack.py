import threading


from rogue.state.basestate import BaseState


class StateLoaderThread(threading.Thread):
    """ Class handles state loading in a separate thread """
    
    def __init__(self, state, callback, **kwargs):
        threading.Thread.__init__(self)
       
        self.should_load = kwargs.get('load', not kwargs.get('unload', False))
        self.state = state
        self.callback = callback

    def run(self):
        if self.should_load:
            self.state.load_content()
        else:
            self.state.unload_content()
        self.callback(self.state)

        
class StateStack(object):
    """ Handles game states and their transitions """
	
    def __init__(self):
		""" Initializes an empty stack """
		self.stack = []
		
    def add(self, state, **kwargs):
        """ Loads the state in a separate thread and adds to stack once it has loaded """
        thread = StateLoaderThread(state, self.add_loaded_state, load=True)
        thread.start()
        
        show_loading = kwargs.get('showLoading', False)
        if show_loading:
            self.loading_func = state.loading_func
        else:
            self.loading_func = None
        
    def add_loaded_state(self, state):
        """ Adds a state that has finished loading to the stack """
        self.loading_func = None
        self.stack.append(state)
        state.handle_added()
        
    def unload(self):
        """ Function calls the unload methods on all states, then clears the stack """
        for state in self.stack:
            state.unload_content()
        self.stack = []
		
    def remove(self, state):
        """ Removes a state from the stack """
        thread = StateLoaderThread(state, self.remove_unloaded_state, unload=True)
        thread.start()
    
    def remove_unloaded_state(self, state):
        """ Removes a state from the stack, when it has finished unloading """
        self.stack.remove(state)
	    
    def update(self):
        """ Executes the update function of each state in the stack """
        if self.loading_func != None:
            self.loading_func()
        for state in self.stack:
            state.update()	# TODO: pass input state and delta
            
