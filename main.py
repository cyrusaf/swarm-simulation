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
			sensed = forager.sense(sim.food, sim.spawn)
			if sensed['carrying_food'] == True: print sensed
			forager.rotatingCW = (True if randint(0,1) == 0 else False)
			forager.rotatingCCW = (True if randint(0,1) == 0 else False)
			#forager.moving = (True if randint(0,1) == 0 else False)

	#time.sleep(1.0/33)


	sim.nextFrame()