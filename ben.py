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

class Ben(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.images.append(load_image('ben_standing1.png').convert_alpha())
		self.images.append(load_image('ben_standing2.png').convert_alpha())
		self.images.append(load_image('ben_standing3.png').convert_alpha())
		self.images.append(load_image('ben_standing4.png').convert_alpha())
		
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 32, 48)
		
	def moveLeft(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ben_runningleft1.png').convert_alpha())
		self.images.append(load_image('ben_runningleft2.png').convert_alpha())
		self.images.append(load_image('ben_runningleft3.png').convert_alpha())
		self.images.append(load_image('ben_runningleft4.png').convert_alpha())


		
	def moveRight(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ben_running1.png').convert_alpha())
		self.images.append(load_image('ben_running2.png').convert_alpha())
		self.images.append(load_image('ben_running3.png').convert_alpha())
		self.images.append(load_image('ben_running4.png').convert_alpha())


	
	def standingRight(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ben_standing1.png').convert_alpha())
		self.images.append(load_image('ben_standing2.png').convert_alpha())
		self.images.append(load_image('ben_standing3.png').convert_alpha())
		self.images.append(load_image('ben_standing4.png').convert_alpha())

		
		
	def standingLeft(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ben_standingleft1.png').convert_alpha())
		self.images.append(load_image('ben_standingleft2.png').convert_alpha())
		self.images.append(load_image('ben_standingleft3.png').convert_alpha())
		self.images.append(load_image('ben_standingleft4.png').convert_alpha())
		
	def update(self):
		global count
		self.image = self.images[self.index]
		count += 1
		if count >= 5:
			self.index = self.index + 1
			count = 0
		if self.index > 3:
			self.index = 0

def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	my_sprite = Ben()
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
