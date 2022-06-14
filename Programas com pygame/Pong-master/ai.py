import random
from constants import *

"""
Desc file:
            Contains the the artificial intelligence AI of the game: 
            -- Ai just try to follow and place the ball in the center of the paddle,
            with a more random or less different response time (see: self.reactionAiDist) 
            + the positioning error (see: self.errorInterval) and it does that for each iteration.

Date: 		27/05/2017

Author: 	A.Amine (Goutted)
"""


class Ai(object):
    def __init__(self, ball, computer):
        self.ball = ball
        self.computer = computer
        # Ai
        self.reactionAiDist = 0
        self.errorInterval = 0
        # the center of ai pad.
        self.predictionPoint = 0

    # We predict only if the ball goes in the direction of the AI paddle.
    def canPredict(self):
        return self.ball.xspeed > 0

    # Ai reacts after un certain distance, when ball is attacking the ai paddle.
    def canResponse(self, value):
        return self.ball.shape.x > value

    # creat new reaction time(or distance) for ai and new error detection of the ball.
    def getNewReaction(self):
        if self.ball.shape.colliderect(self.computer.shape):
            # the distance reached by the ball to let ai react.
            self.reactionAiDist = random.randint(AI_MIN_REACT, AI_MAX_REACT)
            self.errorInterval = random.randint(MIN_ERR_INT, MAX_ERR_INT)

    # let's resume that in this function:
    def update(self, dt):
        # get the center of ai pad
        self.predictionPoint = self.computer.shape.y + self.computer.shape.h / 2

        # if the ball is attacking the ai, ai can predict.
        if self.canPredict():

            self.getNewReaction()

            if self.predictionPoint > self.ball.shape.y + self.errorInterval:
                self.computer.side = -1
            elif self.predictionPoint < self.ball.shape.y + self.errorInterval:
                self.computer.side = 1
            # see if AI can response now or wait more
            if self.canResponse(self.reactionAiDist):
                self.computer.update(dt)
