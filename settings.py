import random
import pygame

# game options/settings
TITLE = "The Catastrophe!"

# Window size
WIDTH = 1024
HEIGHT = 608
FPS = 60     # how many times the screen will be updated
FONT_NAME = 'arial'
SPRITESHEET = "fightercat.png"

display = pygame.Surface((300,200))

GRASS_IMG = 'grass.png'

# Enemy settings
ENEMY1_img = 'monster1.png'

# Player properties
PLAYER_SPEED = 300
PLAYER_ACC = 0.5  # acceleration of the sprite
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8  # gravity

# tile window
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (67, 140, 94)
GRASS = (66, 227, 109)
BLUE = (0, 0, 255)
SKY = (66, 173, 227)
YELLOW = (255, 255, 0)
LIGHTGREY = (100, 100, 100)
