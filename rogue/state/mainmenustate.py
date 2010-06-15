
from rogue.state.basestate import BaseState
from rogue.state.loadingstate import LoadingState
from rogue.state.gamestate import GameState


class MainMenuState(BaseState):
	
    def __init__(self, stack):
        BaseState.__init__(self, stack)
        
    def handle_added(self):
        self.stack.remove(self)
        self.stack.add(GameState(self.stack), showLoading=True)
        
    def load_content(self):
        print "Loading mainmenu"
        
    def unload_content(self):
        print "Unloading mainmenu"
        
    #def update(self):
    #    print "In main menu"