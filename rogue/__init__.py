from . import game


RENDERER = "pygame" # Load this from a config object


def get_renderer(ttype):
    try:
        ttype = 'renderer.' + ttype + '.renderer'
        renderer = __import__(ttype, globals(), locals(), ['renderer'], -1)
        return renderer.Renderer()
    except:
        print("Could not find renderer {0}. Aborting.".format(ttype))


def main():
    renderer = get_renderer(RENDERER)
    gobject = game.Game(renderer)

