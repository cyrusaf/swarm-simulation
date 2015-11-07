import pygame

from Entity import Entity

class Food(Entity):

	def __init__(self, pos):
		Entity.__init__(self, pos)
		self.color = (241, 196, 15)
		self.radius = 5

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius)