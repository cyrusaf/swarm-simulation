from random import randint

from classes import Simulation
	

sim = Simulation()
for i in range(0,10):
	sim.spawnForager()

for i in range(0,50):
	sim.spawnFood()

sim.running = True
while sim.running:
	if sim.frame_num % 25 == 0:
		for forager in sim.foragers:
			print forager.sense(sim.food)
			forager.rotatingCW = (True if randint(0,1) == 0 else False)
			forager.rotatingCCW = (True if randint(0,1) == 0 else False)
			#forager.moving = (True if randint(0,1) == 0 else False)


	sim.nextFrame()