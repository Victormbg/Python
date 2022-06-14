import random, sys
from math import *
from ball import *
from constants import *
from ai import *

"""
Desc file:
			The Main Class Engine, for managing the logic of the game, contains a 
			global update() & draw() functions to update and draw the whole main game. Init all class too.
			main function of the class is the main loop, it calls all the game logic. 
			update function : contains all the update() method of the game, same thing for draw().
			
TODO:		Edit the evenListener()*
				
Date: 		30/05/2017

Author: 	A.Amine (Goutted)
"""


class Engine(object):
    def __init__(self):
        """Initalize the display and all game objects."""
        self.screen = pg.display.get_surface()
        self.Boundary = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = FPS_MAX
        self.dt = 1.0 # delta time isn't activated.
        self.keys = pg.key.get_pressed()
        self.done = False
        self.color = GAME_COLOR
        self.player = Paddle(pg.Rect(PL_PAD_X, PL_PAD_Y, PAD_W, PAD_H), 0, PAD_SPEED, self.color)
        self.computer = Paddle(pg.Rect(AI_PAD_X, AI_PAD_Y, PAD_W, PAD_H), 0, PAD_SPEED + 1, self.color)
        self.ball = Ball(pg.Rect(400, 300, BL_DIM, BL_DIM), BL_XVEL, BL_YVEL, self.color)
        # creat new Ai fro the computer paddle : the interaction of ai is between camputer pad and ball.
        self.ai = Ai(self.ball, self.computer)
        # load relative resources to this class.
        self.my_rc = Resources()
        self.font = self.my_rc.loadFont('fixedsys.ttf', 55)
        self.fpstext = self.my_rc.loadFont('arial.ttf', 15)
        self.dashline = self.my_rc.loadImage('dash.png')
        self.gamefx = self.my_rc.loadSound('gameloop.wav')
        self.gamefx.set_volume(0.5)
        # menu / game event listener
        self.menuInfo = False
        # display message you win/ loose to player.
        self.winnerMsg = ''

    def update(self):
        # Update the player, computer, key pressed, ball, all stuffs & shits are updated here !
        self.keys = pg.key.get_pressed()
        self.ball.update(self.dt, self.player.shape, self.computer.shape)
        self.player.update(self.dt)
        self.ai.update(self.dt)
        self.updateScore()
        # then check for winner
        self.winnerCheck()


    def updateScore(self):
        # for each update we see if there's a winner, and add +1pts for him.
        if self.ball.winner is 'player':
            self.player.score += 1
            self.ball.winner = 'none'
        elif self.ball.winner is 'ai':
            self.computer.score += 1
            self.ball.winner = 'none'

    def quitGame(self):
        pg.quit()
        sys.exit()

    def winnerCheck(self):
        if self.player.score == MAX_SCORE:
            self.winnerMsg = 'You Win !'
            self.player.score = 0
            self.computer.score = 0
            self.done = True
            self.menuInfo = False
        elif self.computer.score == MAX_SCORE:
            self.winnerMsg = 'Game Over'
            self.player.score = 0
            self.computer.score = 0
            self.done = True
            self.menuInfo = False
        else:
            self.winnerMsg ='Paused..'

    def eventListener(self):
        # the event keys to interact with the player.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quitGame()
            elif self.keys[pg.K_ESCAPE]:
               self.quitGame()
            elif self.keys[pg.K_SPACE]:
                self.done = True
                self.menuInfo = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.side = -1
                elif event.key == pg.K_DOWN:
                    self.player.side = 1
                elif event.key == pg.K_p:
                    self.gamefx.stop()
                    self.gamefx.play(-1)
                elif event.key == pg.K_s:
                    self.gamefx.stop()
                elif event.key == pg.K_F10:
                    self.switchFpsMode()
            else:
                self.player.side = 0

    # enable disable fps
    def switchFpsMode(self):
        if not self.fps:
            self.fps = FPS_MAX
            self.dt = 1.0
        else:
            self.fps = 0
            self.dt = FPS_MAX/self.clock.get_fps()


    def draw(self):
        # Draw all necessary objects to the level.
        self.screen.fill(BACkGROUND_COLOR)
        self.screen.blit(self.dashline, (425, 0))
        self.player.draw()
        self.computer.draw()
        self.ball.draw()
        self.my_rc.printFont(self.font, str(self.computer.score), AI_SCORE_POS)
        self.my_rc.printFont(self.font, str(self.player.score), PL_SCORE_POS)
        self.my_rc.printFont(self.fpstext, "fps: " + str(self.clock.get_fps()), (760, 5))

    def mainLoop(self, menuInfo):
        # play some fx sound
        self.done = menuInfo
        self.gamefx.play(-1)

        # the main loop of the level.
        while not self.done:
            self.eventListener()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)

        self.gamefx.stop()
