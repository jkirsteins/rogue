
def FrontendFactory(game, name):
    #try:
    module = 'rogue.frontend.' + name + '.frontend'
    frontend_module = __import__(module, globals(), locals(), ['frontend'], -1)
    return frontend_module.Frontend(game)
    #except:
    #    print("Could not find renderer {0}. Aborting.".format(ttype))