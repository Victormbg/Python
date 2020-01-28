import sys
from resources import *
from random import randint
from constants import *

"""
Desc file:
            Class menu for displaying menu/pause game playing sound and some anime stuffs.

TODO:		improve.

Date: 		30/05/2017

Author: 	A.Amine (Goutted)
"""


class Menu(object):
    def __init__(self):
        self.done = False
        self.gameInfo = True
        self.fps = 10
        self.screen = pg.display.get_surface()
        self.color = (0, 0, 0)
        # manage menu fps's
        self.clock = pg.time.Clock()
        # load some resources for menu
        self.my_rc = Resources()
        self.fontAtari = self.my_rc.loadFont('fixedsys.ttf', 80)
        self.fontMenu = self.my_rc.loadFont('fixedsys.ttf', 20)
        self.fontAuthor = self.my_rc.loadFont('fixedsys.ttf', 12)
        self.winnerfont = self.my_rc.loadFont('fixedsys.ttf', 60)
        self.menufx = self.my_rc.loadSound('8bitsmisc.wav')
        self.menufx.set_volume(0.5)
        self.menufx.play(-1)


    def quitGame(self):
        pg.quit()
        sys.exit()


    def eventListener(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quitGame()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.done = True
                    self.gameInfo = False
                    self.menufx.stop()
                elif event.key == pg.K_ESCAPE:
                    self.quitGame()


    # the main loop of the menu.
    def menuLoop(self, gameInfo, winnerMsg):
        self.done = gameInfo
        while not self.done:
            self.eventListener()
            self.update()
            self.draw(winnerMsg)
            pg.display.flip()
            self.clock.tick(self.fps)

        self.menufx.stop()


    def update(self):
        self.keys = pg.key.get_pressed()  # creat random color for menu title texte.
        self.color = (randint(10, 255), randint(10, 255), randint(10, 255))


    def draw(self, winnerMsg):
        self.screen.fill(BACkGROUND_COLOR)
        self.my_rc.printcFont(self.fontAtari, 'Atari Pong', INTRO1_TEXT_POS, self.color)
        self.my_rc.printcFont(self.fontAtari, '1972', INTRO2_TEXT_POS, self.color)
        self.my_rc.printFont(self.fontMenu, 'Enter:  Play', MENU_POS1)
        self.my_rc.printFont(self.fontMenu, 'Space:  Pause', MENU_POS2)
        self.my_rc.printFont(self.fontMenu, 'Escape: Exit', MENU_POS3)
        self.my_rc.printFont(self.fontAuthor, 'By: Amine.A (Goutted) ' + VERSION, AUTHOR_POS)
        self.my_rc.printFont(self.winnerfont, winnerMsg, MENU_MPOS)
