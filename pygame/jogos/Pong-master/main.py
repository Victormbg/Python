#!/usr/bin/python

from engine import *
from menu import *

"""
Desc file:
                A simple 2D pong game with realistic physics against AI made with Pygame on Python 3.6. 
                The game parameters can be changed from the constants.py file, for ex to make 
                the AI ​​more aggressive, go ahead and reduce the values AI_MAX_REACT and MAX_ERR_INT.

Date: 			30/05/2017
Author: 		A.Amine (Goutted)

                Released under the GNU General Public License.
"""


def main():
    pg.init()
    pg.key.set_repeat(25, 5)
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE, pg.FULLSCREEN)
    pg.mouse.set_visible(False)

    game = Engine()
    menu = Menu()
    while True:
        menu.menuLoop(game.menuInfo, game.winnerMsg)
        game.mainLoop(menu.gameInfo)


if __name__ == "__main__":
    main()
