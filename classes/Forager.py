import pygame
import math

from MovableEntity import MovableEntity

class Forager(MovableEntity):

	def __init__(self, pos, theta):
		MovableEntity.__init__(self, pos, theta)
		self.color = (0,112,255)
		self.radius = 10
		self.rotatingCCW = True
		self.carryingFood = False
		self.food_collected = 0

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius)
		vec = self.__getVector()
		pygame.draw.line(screen, (0,0,0), self.pos, (self.pos[0]+(self.radius-1)*vec[0], self.pos[1]+(self.radius-1)*vec[1]), 2)

	def __getVector(self):
		return self._MovableEntity__getVector()

	def checkCollisions(self, food, spawn):
		total = 0
		if self.carryingFood == False:
			for food_item in list(food):
				dist = math.hypot(food_item.pos[0] - self.pos[0], food_item.pos[1] - self.pos[1])
				if dist <= self.radius + food_item.radius:
					self.carryingFood = True
					food.remove(food_item)
					self.color = (0,70,140)
					total += 1

		if self.carryingFood == True:
			dist = math.hypot(spawn.pos[0] - self.pos[0], spawn.pos[1] - self.pos[1])
			if dist <= self.radius + spawn.radius:
				self.carryingFood = False
				self.food_collected += 1
				self.color = (0,112,255)

		return total