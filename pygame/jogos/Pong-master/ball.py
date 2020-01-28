from paddle import *
from constants import *
from math import cos, sin
import random
from resources import *

"""
Desc file: 
            Contains Ball class witch inherits for the Paddle: a ball has a shape a color 
            a quantity of movement, it cans move from top down and collide with walls.
            With that the ball collide with the paddles too, and has it's own movement & update function 
            so they are overridden.

Date: 		29/05/2017

Author: 	A.Amine (Goutted)
"""


class Ball(Paddle):
    def __init__(self, shape, xvel, yvel, color):
        Paddle.__init__(self, shape, xvel, yvel, color)
        # virtual boundaries are just used for collisions optimisation see the description in the function.
        self.virtualBoundary = self.creatBoundaries()
        # angle of bounce in radian.
        self.theta = 0.
        # load ball sounds
        self.my_res = Resources()
        self.hit = self.my_res.loadSound('hit.wav')
        self.loose = self.my_res.loadSound('loose.wav')
        # contains who got +1 in the score
        self.winner = 'none'


    def move(self, dt):
        self.shape.x += self.xspeed * cos(self.theta) * dt
        self.shape.y += self.yspeed * sin(self.theta) * dt

    def update(self, dt, paddle=None, paddle2=None):
        self.move(dt)

        # this if is just for optimisation see description of function virtualBoundary.
        if not self.virtualBoundary.contains(self.shape):
            # Ball/ wall collisions
            if not self.boundary.contains(self.shape):
                self.yspeed *= - 1
                self.theta = random.uniform(MIN_ANGLE, MAX_ANGLE)

                if self.shape.x < 0 or self.shape.x + self.shape.w > self.boundary.w:
                    self.xspeed *= -1
                    self.yspeed *= -1
                    self.theta = random.uniform(MIN_ANGLE, MAX_ANGLE)
                    self.loose.play(0)
                    pg.time.delay(600)
                    # new ball.
                    self.resetPos(paddle)
                    if self.xspeed < 0:
                        self.winner = 'player'
                    else:
                        self.winner = 'ai'

            # ball/pad collisions
            if self.shape.colliderect(paddle):
                self.xspeed *= -1
                # to prevent from multiple collisions ball/pad.
                self.shape.x += paddle.w + 1
                self.theta = random.uniform(0.20, MAX_ANGLE)
                self.hit.play(0)

            elif self.shape.colliderect(paddle2):
                self.xspeed *= -1
                self.shape.x -= paddle2.w - 1
                self.theta = random.uniform(0.20, MAX_ANGLE)
                self.hit.play(0)

    def resetPos(self, paddle):
        self.shape.y = paddle.y + paddle.h / 2
        self.shape.x = paddle.x + paddle.w + 1

    """ 
    Description :
    use function contains(Rect) for optimisation. so we just test collisions functions once 
    we're outside the virtual rect boundaries to avoid computing collision for each iteration uselessly.
    """

    def creatBoundaries(self):
        return pg.Rect(PAD_W + COLLIDE_AREA, COLLIDE_AREA,
                       SCREEN_SIZE[0] - PAD_W - (COLLIDE_AREA * 2),
                       SCREEN_SIZE[1] - (COLLIDE_AREA * 2))
