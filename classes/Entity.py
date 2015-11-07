import pygame

class Entity(object):
	def __init__(self, pos):
		self.pos = pos
		self.radius = 15
		self.color = (0,0,0)

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius)