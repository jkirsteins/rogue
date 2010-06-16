import os.path
from optparse import OptionParser


from rogue.game import Game
from rogue.config import Config


def main():

    parser = OptionParser()
    parser.add_option("-f", "--frontend", 
                  type="string",
                  dest="frontend_name",
                  help="use frontend called NAME", 
                  metavar="NAME")
    parser.add_option("-r", "--resolution", 
                  type="string",
                  dest="resolution",
                  help="use specified resolution", metavar="WIDTHxHEIGHT")
    (options, args) = parser.parse_args()
    
    cfg = Config(os.path.join("config", "config.cfg"))
    if options.frontend_name != None:
        cfg.set('Game', 'frontend', options.frontend_name)
    
    cfg.merge_file(os.path.join("config", "%s.cfg" % cfg.frontend_name()))
    if options.resolution != None:
        cfg.set('Video', 'resolution', options.resolution)
    
    game = Game(cfg)
    game.run()
    