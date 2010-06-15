import time


from rogue.state.basestate import BaseState


class GameState(BaseState):
        
    def load_content(self):
        print "Loading GameState"
        print "\tFinished"
        
    def handle_added(self):
        print "GameState added to the stack"
        
    def loading_func(self):
        print "Loading GameState ..."