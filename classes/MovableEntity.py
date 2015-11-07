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
		self.angular_velocity = 0.1

		self.rotatingCW = False
		self.rotatingCCW = False
		self.moving = True

		self.sensor_dist = 50

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