import pygame as pg

"""
Desc file: 
            Contains generic paddle class : a paddle has a shape a color 
            a quantity of movement, it cans move from top down and collide with walls.
            
TODO:   	* remove param boundary from update function and get local var screen.get_rect().
            * remove param screen from func drawn too.
            * replace optional val = 0 by value = None.
                
Date: 		30/05/2017

Author: 	A.Amine (Goutted)
"""

class Paddle(object):
    def __init__(self, shape, xvel, yvel, color):
        self.shape = shape
        self.color = color
        self.xspeed = xvel
        self.yspeed = yvel
        self.side = 0
        self.score = 0
        self.screen = pg.display.get_surface()
        self.boundary = self.screen.get_rect()

    def move(self, dt):
        self.shape.y += self.yspeed * self.side * dt

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.shape, 0)

    def update(self, dt, paddle=None, paddle2=None):
        self.move(dt)
        # check for collision paddle/walls
        if self.shape.y < 0:
            self.side = 0
            self.shape.y = 0
        elif self.shape.y + self.shape.h > self.boundary.h:
            self.side = 0
            self.shape.y = self.boundary.h - self.shape.h
