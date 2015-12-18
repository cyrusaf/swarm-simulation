import pygame
from pygame import gfxdraw
import math

from Entity import Entity

class MovableEntity(Entity):

	def __init__(self, pos, theta):
		Entity.__init__(self, pos)
		self.theta = float(theta)
		self.color = (0,112,0)
		self.velocity = 5
		self.angular_velocity = .524/6.0 # used to be 1.0

		self.rotatingCW = False
		self.rotatingCCW = False
		self.moving = True

		self.sensor_dist = 150

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius)

	def drawSensor(self, screen):
		pygame.gfxdraw.aacircle(screen, self.pos[0], self.pos[1], self.radius + self.sensor_dist, self.color)


	def move(self):
		if self.moving: self.__moveForward()
		if self.rotatingCW: self.__rotateCW()
		if self.rotatingCCW: self.__rotateCCW()

	def __moveForward(self):
		vec = self.__getVector()
		self.pos[0] += int(vec[0] * self.velocity)
		self.pos[1] += int(vec[1] * self.velocity)

	def __rotateCW(self):
		self.theta -= self.angular_velocity

	def __rotateCCW(self):
		self.theta += self.angular_velocity

	def __getVector(self):
		return (math.cos(self.theta), math.sin(self.theta))

	def normVectorTo(self, entity):
		vec = [self.pos[0] - entity.pos[0], self.pos[1] - entity.pos[1]]
		magnitude = math.sqrt(vec[0]**2 + vec[1]**2)
		if magnitude == 0:
			vec = [0, 0]
		else:
			vec = [vec[0]/magnitude, vec[1]/magnitude]
		cs = math.cos(self.theta)
		sn = math.sin(self.theta)
		return [vec[0]*cs - vec[1]*sn, vec[0]*sn + vec[1]*cs]