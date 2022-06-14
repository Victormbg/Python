import pygame as pg
import os

"""
Desc file:n ( v0.2 )

            this class regroups all functions to load & test resources, sound,
            images, fonts..etc and some utilities functions to print texte in 
            the screen & stuffs like that. 

TODO:
            get the screen var directly in the class & remove it from param font_draw
Date: 		30/05/2017

Author: 	A.Amine (Goutted)
"""


class Resources(object):
    def __init__(self):
        self.screen = pg.display.get_surface()

    def loadSound(self, name):
        name = os.path.join('data', name)
        try:
            sound = pg.mixer.Sound(name)
        except ValueError:
            print('Unable to load sound:', name, ValueError)
            raise
        return sound

    def loadImage(self, name, flag=None):
        try:
            if flag is 'alpha':
                image = pg.image.load(os.path.join('data', name)).convert_alpha()

            else:
                image = pg.image.load(os.path.join('data', name)).convert()
                # imrect = image.get_rect()
        except ValueError:
            print('Unable to load image:', name, ValueError)
            raise
        return image

    def loadFont(self, name, size):
        name = os.path.join('data', name)
        try:
            font = pg.font.Font(name, size)
        except ValueError:
            print('Unable to load TT Font:', name, ValueError)
            raise
        return font

    # functions to print texte in the screen with white by default.
    def printFont(self, font, message, vect):
        self.screen.blit(font.render(message, True, (255, 255, 255)), vect)

    def printcFont(self, font, message, vect, color):
        self.screen.blit(font.render(message, True, color), vect)

    def loadAll(self, *argv):
        pass
