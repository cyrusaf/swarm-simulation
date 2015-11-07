import pygame

from Entity import Entity

class Food(Entity):

	def __init__(self, pos):
		Entity.__init__(self, pos)
		self.color = (241, 196, 15)
		self.radius = 5

	def draw(self, screen):
		pygame.gfxdraw.filled_circle(screen, self.pos[0], self.pos[1], self.radius, self.color)
		pygame.gfxdraw.aacircle(screen, self.pos[0], self.pos[1], self.radius, self.color)