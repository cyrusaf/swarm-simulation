import pygame
import math

class Entity(object):
	def __init__(self, pos):
		self.pos = pos
		self.radius = 15
		self.color = (0,0,0)

	def draw(self, screen):
		pygame.draw.aacircle(screen, self.pos[0], self.pos[1], self.radius, self.color)

	def distFrom(self, entity2):
		return math.sqrt((self.pos[0] - entity2.pos[0])**2 + (self.pos[1] - entity2.pos[1])**2)