
"""
Desc file:
                Contains all constants stuffs of the game, grouped by category.
                All parameters of the pong can be edited here, like pad size or screen
                velocity of pad, ball...the AI params to make it more or less difficult
                ..etc.

Date: 			30/05/2017
Author: 		A.Amine (Goutted)
"""


# =================  screen stuffs
CAPTION = "Basic Atari Pong 1972"
VERSION = "v1.0"
SCREEN_SIZE = (900, 600)
BACkGROUND_COLOR = (0, 0, 0)
GAME_COLOR = (255, 255, 255)
FPS_MAX = 62.5
PL_SCORE_POS = (365, 2)
AI_SCORE_POS = (495, 2)
MAX_SCORE = 10
# =========== Pad player/computer dim,speed, position & stuffs.
PAD_SPEED = 8
PAD_W = 16
PAD_H = 85
PL_PAD_X = 10
PL_PAD_Y = 250
AI_PAD_X = SCREEN_SIZE[0] - PAD_W - 10
AI_PAD_Y = 200
# ================== Size and x y speed of the ball & stuffs
BL_DIM = 13
BL_XVEL = 14
BL_YVEL = 14
COLLIDE_AREA = 25 # The virtual invisible boundaries, where we can compute collisions (for optimisation).
MIN_ANGLE = 0.65  # min & max random angle of the ball after collisions.
MAX_ANGLE = 0.90
# =================== AI stuffs, time of reaction plus error of movement
AI_MIN_REACT = 150
AI_MAX_REACT = 330
MIN_ERR_INT = -25
MAX_ERR_INT = 25
# ================ Menu stuffs
INTRO1_TEXT_POS = (240, 20)
INTRO2_TEXT_POS = (345, 100)
MENU_POS1 = (365, 340)
MENU_POS2 = (365, 375)
MENU_POS3 = (365, 410)
MENU_MPOS = (300, 220)
AUTHOR_POS = (SCREEN_SIZE[0] - 200, SCREEN_SIZE[1] - 50)