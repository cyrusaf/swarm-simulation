import pygame
import math
import time
from random import randint

class Entity(object):
	def __init__(self, pos):
		self.pos = pos
		self.radius = 15
		self.color = (0,0,0)

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius)

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

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius)

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
		
class Forager(MovableEntity):

	def __init__(self, pos, theta):
		MovableEntity.__init__(self, pos, theta)
		self.color = (0,112,255)
		self.rotatingCCW = True

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius)
		vec = self.__getVector()
		pygame.draw.line(screen, (0,0,0), self.pos, (self.pos[0]+(self.radius-1)*vec[0], self.pos[1]+(self.radius-1)*vec[1]), 2)

	def __getVector(self):
		return self._MovableEntity__getVector()

class Spawn(Entity):

	def __init__(self, pos):
		Entity.__init__(self, pos)
		self.color = (255,0,0)
		self.radius = 75

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, tuple(self.pos), self.radius, 2)


class Simulation:

	def __init__(self):
		self.running = False
		pygame.init()
		self.screenSize = (800,800)
		self.screen = pygame.display.set_mode(self.screenSize)
		self.spawn = Spawn([self.screenSize[0]/2, self.screenSize[1]/2])
		self.foragers = []
		self.frame_num = 0

	def startLoop(self):
		self.running = True
		while self.running:
			self.gameLoop()

	def gameLoop(self):
		self.__checkEvents()
		self.__draw()
		self.__move()

		self.frame_num += 1
		time.sleep(1.0/33)

	def spawnForager(self):
		pos = self.spawn.pos[:]
		pos[0] += randint(-1*self.spawn.radius, self.spawn.radius)
		pos[1] += randint(-1*self.spawn.radius, self.spawn.radius)
		theta = randint(0,3)*math.pi/2
		self.foragers.append(Forager(pos, theta))
		print self.foragers
		

	def __checkEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def __draw(self):
		self.screen.fill((255,255,255))
		self.spawn.draw(self.screen)
		for forager in self.foragers:
			forager.draw(self.screen)
		pygame.display.flip()

	def __move(self):
		if self.frame_num % 10 == 0:
			for forager in self.foragers:
				forager.rotatingCW = (True if randint(0,1) == 0 else False)
				forager.rotatingCCW = (True if randint(0,1) == 0 else False)
				forager.moving = (True if randint(0,1) == 0 else False)

		for forager in self.foragers:
			forager.move()

	def __checkCollisions(self):
		pass

	

sim = Simulation()
for i in range(0,10):
	sim.spawnForager()
sim.startLoop()