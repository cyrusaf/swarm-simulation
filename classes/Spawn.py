import pygame

from Entity import Entity

class Spawn(Entity):

	def __init__(self, pos):
		Entity.__init__(self, pos)
		self.color = (255,0,0)
		self.radius = 75

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius, 2)