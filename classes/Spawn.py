import pygame
from pygame import gfxdraw

from Entity import Entity

class Spawn(Entity):

	def __init__(self, pos):
		Entity.__init__(self, pos)
		self.color = (255,0,0)
		self.radius = 75

	def draw(self, screen):
		pygame.gfxdraw.aacircle(screen, self.pos[0], self.pos[1], self.radius, self.color)