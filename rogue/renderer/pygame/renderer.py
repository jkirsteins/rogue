import sys
import pygame


# init pygame
pygame.init()


class Renderer(object):
    def __init__(self):
        # Get these settings somewhere
        self.width, self.height = 640, 480
        self.screen = pygame.display.set_mode((self.width, self.height))

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # FIXME: DO NOT EXIT LIKE THIS

        self.screen.fill((0, 0, 0))
        pygame.display.flip()

