import pygame
from pygame.constants import *
from playerpng import playerPNG
from Title import titler
import level
from cursor import Cursor
from helpliest import helper
from Daltonyx import daltonyx
from ben import Ben
pygame.init()

# COLOR SCHEME
GREEN = (20, 255, 140)
DARKGREY = (80, 82, 78)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (24, 0, 255)
BLACK = (0, 0, 0)


# VARIABLES
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
CELL = 50
mapx = 0
gravity =4
v = 4
m = 2
playerspeed = 4
count = 0
ticker = 0
levelswon = 0
choice = 0
helpcount = 0
helptick = 0
volume = 0.1
right = False
left = False
levelEditor = False
onground = False
running = True
jump = False
title = True
game = False
juststarted = True
over = False
win = False
helping = False
flags = SCALED | DOUBLEBUF | HWSURFACE
playerscreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
pygame.display.set_caption("MOE-Rio")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)


# SPRITES
player = playerPNG(3)
player.rect.x = SCREEN_WIDTH/2
player.rect.y = SCREEN_HEIGHT/2
playergroup = pygame.sprite.Group()
playergroup.add(player)
playerbuffer = [player.rect.x, player.rect.y, mapx]

helper1 = helper()
helper1.rect.x = 0
helper1.rect.y = 550
helpgroup = pygame.sprite.Group()
helpgroup.add(helper1)


titles = titler()
titles.rect.x = 700
titles.rect.y = 300
titlegroup = pygame.sprite.Group()
titlegroup.add(titles)

cursor = Cursor()
cursor.rect.x = 0
cursor.rect.y = 0
cursorgroup = pygame.sprite.Group()
cursorgroup.add(cursor)

dalton = daltonyx()
dalton.rect.x = 0
dalton.rect.y = 0
dgroup = pygame.sprite.Group()
dgroup.add(dalton)

ben = Ben()
ben.rect.x = 0
ben.rect.y = 0
bengroup = pygame.sprite.Group()
bengroup.add(ben)


def cellNumber(row, column):
	if row >= 0 and row < int(level.mapheight/CELL) and column >= 0 and column < int(level.mapwidth/CELL):
		return level.level[row][column]
	else:
		return 1

def load_image(name):
	image = pygame.image.load(name)
	return image

# ASSET LINKS
grasstop = load_image("grasstop.png")
grass = load_image("grass.png")
air = load_image("air.png")
gameover = load_image("rip.png")
background = load_image("background.png")
background2 = load_image("background2.png")
winimage = load_image("winimage.png")
levelimg = load_image("levelimg.png")
editor = load_image("editor.png")
help0 = load_image("help1.png")
help1 = load_image("help2.png")
help2 = load_image("help3.png")
selector = load_image("selector.png")
select = pygame.mixer.Sound("select.wav")
jumpSound = pygame.mixer.Sound("jump.wav")