import pygame
import time
import random
import sys
import os
from pygame.locals import *
# COLOR SCHEME
GREEN = (20, 255, 140)
DARKGREY = (80, 82, 78)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (38,79,110)
BLACK = (0, 0, 0)
count = 0
flags = SCALED | FULLSCREEN | DOUBLEBUF
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(resolution, flags, 16)


def load_image(name):
	image = pygame.image.load(name)
	return image

class titler(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.images.append(load_image('title1.png').convert_alpha())
		self.images.append(load_image('title2.png').convert_alpha())
		self.images.append(load_image('title3.png').convert_alpha())
		self.images.append(load_image('title4.png').convert_alpha())
		self.images.append(load_image('title5.png').convert_alpha())
		self.images.append(load_image('title6.png').convert_alpha())
		self.images.append(load_image('title7.png').convert_alpha())
		self.images.append(load_image('title8.png').convert_alpha())
		self.images.append(load_image('title9.png').convert_alpha())
		self.images.append(load_image('title10.png').convert_alpha())
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 32, 48)

	def update(self):
		global count
		self.image = self.images[self.index]
		count += 1
		if count >= 30:
			self.index = self.index + 1
			count = 0
		if self.index > 9:
			self.index = 0

def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	my_sprite = titler()
	my_group = pygame.sprite.Group(my_sprite)

	while True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

		# Calling the 'my_group.update' function calls the 'update' function of all
		# its member sprites. Calling the 'my_group.draw' function uses the 'image'
		# and 'rect' attributes of its member sprites to draw the sprite.
		my_group.update()
		my_group.draw(screen)
		pygame.display.flip()

	if __name__ == '__main__':
		main()
