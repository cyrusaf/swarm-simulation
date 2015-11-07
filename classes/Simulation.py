import pygame
import math
import time
from random import randint

from Forager import Forager
from Spawn import Spawn
from Food import Food

class Simulation:

	def __init__(self):
		self.running = False
		pygame.init()
		self.screenSize = (800,800)
		self.screen = pygame.display.set_mode(self.screenSize)
		self.spawn = Spawn([self.screenSize[0]/2, self.screenSize[1]/2])
		self.foragers = []
		self.food = []
		self.frame_num = 0
		self.font = pygame.font.SysFont("monospace", 15)
		self.draw_sensors = True


	def startLoop(self):
		self.running = True
		while self.running:
			self.nextFrame()

	def nextFrame(self):
		self.__checkEvents()
		self.__draw()
		self.__checkCollisions()
		self.__move()

		self.frame_num += 1
		time.sleep(1.0/33)

	def spawnForager(self):
		pos = self.spawn.pos[:]
		pos[0] += randint(-1*self.spawn.radius, self.spawn.radius)
		pos[1] += randint(-1*self.spawn.radius, self.spawn.radius)
		theta = randint(0,3)*math.pi/2
		self.foragers.append(Forager(pos, theta))
	
	def spawnFood(self):
		pos = self.spawn.pos[:]
		dx = randint(self.spawn.radius, self.screenSize[0]/2)
		dy = randint(self.spawn.radius, self.screenSize[1]/2)
		pos[0] += dx * (-1 if randint(0,1) == 0 else 1)
		pos[1] += dy * (-1 if randint(0,1) == 0 else 1)
		self.food.append(Food(pos))

	def __checkEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def __draw(self):
		self.screen.fill((255,255,255))
		self.spawn.draw(self.screen)

		# Draw foragers
		total_food = 0
		for forager in self.foragers:
			forager.draw(self.screen)
			if self.draw_sensors: forager.drawSensor(self.screen)
			total_food += forager.food_collected

		# Draw score
		label = self.font.render("Food Collected: %s" % total_food, 1, (0,0,0))
		self.screen.blit(label, (20, 20))

		# Draw food
		for food in self.food:
			food.draw(self.screen)
		pygame.display.flip()

	def __move(self):
		for forager in self.foragers:
			forager.move()

	def __checkCollisions(self):
		for forager in self.foragers:
			collissions = forager.checkCollisions(self.food, self.spawn)
			for i in range(0,collissions):
				self.spawnFood()