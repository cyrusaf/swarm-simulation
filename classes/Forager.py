import pygame
from pygame import gfxdraw
import math

from MovableEntity import MovableEntity

class Forager(MovableEntity):

	def __init__(self, pos, theta):
		MovableEntity.__init__(self, pos, theta)
		self.color = (0,112,255)
		self.radius = 10
		self.rotatingCCW = True
		self.carrying_food = False
		self.food_collected = 0

	def draw(self, screen):
		pygame.gfxdraw.filled_circle(screen, self.pos[0], self.pos[1], self.radius, self.color)
		pygame.gfxdraw.aacircle(screen, self.pos[0], self.pos[1], self.radius, self.color)
		vec = self.__getVector()
		pygame.draw.line(screen, (0,0,0), self.pos, (self.pos[0]+(self.radius-1)*vec[0], self.pos[1]+(self.radius-1)*vec[1]), 2)

	def __getVector(self):
		return self._MovableEntity__getVector()

	def checkCollisions(self, food, spawn):
		total = 0
		if self.carrying_food == False:
			for food_item in list(food):
				dist = math.hypot(food_item.pos[0] - self.pos[0], food_item.pos[1] - self.pos[1])
				if dist <= self.radius + food_item.radius:
					self.carrying_food = True
					food.remove(food_item)
					self.color = (0,70,140)
					total += 1

		if self.carrying_food == True:
			dist = math.hypot(spawn.pos[0] - self.pos[0], spawn.pos[1] - self.pos[1])
			if dist <= self.radius + spawn.radius:
				self.carrying_food = False
				self.food_collected += 1
				self.color = (0,112,255)

		return total

	def sense(self, food, spawn):
		sensor_radius = self.sensor_dist + self.radius

		food_sensed = []

		# Find collisions with sensor hitbox
		food_items = []
		for food_item in food:
			#print "%s - %s" % (food_item.pos, self.pos)
			dist = math.hypot(food_item.pos[0] - self.pos[0], food_item.pos[1] - self.pos[1])

			#print "%s = %s" % (dist, sensor_radius + food_item.radius)
			if dist <= sensor_radius + food_item.radius:
				food_items.append([self.normVectorTo(food_item), dist])


		food_items.sort(key=lambda x: x[1])


		sensor_angle = math.pi/8
		sensor_num   = 5
		sensors = [0 for i in range(0,sensor_num)]

		for food_item in food_items:
			# Get angle to food
			angle = math.atan2(food_item[0][1], food_item[0][0])

			total_angle = sensor_angle*sensor_num
			for i in range(0,sensor_num):
				sense_angle = (i+0.5)*sensor_angle - total_angle/2
				anglediff = (sense_angle - angle + math.pi/2) % math.pi - math.pi/2
				if anglediff <= sensor_angle/2 and anglediff >= -1*sensor_angle/2:
					if food_item[1] == 0: food_item[1] = 0.1
					sensors[i] = 2.0#self.sensor_dist / food_item[1]


			food_sensed.append(sensors)
			sensors = [0 for i in range(0,sensor_num)]

		# Sense spawn
		vec = self.normVectorTo(spawn)
		angle = math.atan2(vec[1], vec[0])
		total_angle = sensor_angle*sensor_num
		for i in range(0,sensor_num):
			sense_angle = (i+0.5)*sensor_angle - total_angle/2
			anglediff = (sense_angle - angle + math.pi/2) % math.pi - math.pi/2
			if anglediff <= sensor_angle/2 and anglediff >= -1*sensor_angle/2:
				sensors[i] = 2.0

		spawn_sensed = sensors


		return {
			'food': food_sensed,
			'spawn': spawn_sensed,
			'carrying_food': self.carrying_food
		}