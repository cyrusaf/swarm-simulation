import pygame
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
		pygame.draw.circle(screen, (0,0,0), tuple(self.pos), self.radius + self.sensor_dist, 1)


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

	def sense(self, food):
		sensor_radius = self.sensor_dist + self.radius

		food_sensed = []

		# Find collisions with sensor hitbox

		for food_item in food:
			#print "%s - %s" % (food_item.pos, self.pos)
			dist = math.hypot(food_item.pos[0] - self.pos[0], food_item.pos[1] - self.pos[1])

			#print "%s = %s" % (dist, sensor_radius + food_item.radius)
			if dist <= sensor_radius + food_item.radius:
				food_sensed.append(food_item.pos)


		return {'Food': food_sensed}