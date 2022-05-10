# demonstrate monte carlo simulation with time loop to calculate position over time and calculate simple statistics

import random
import statistics # used for statistics
    
dt = .25 # Timestep
num_iterations = 50
verbose = False # False will turn off single run intermediate output

car1_distance, car2_distance = [], [] # initialize output measure lists

for iteration in range(num_iterations):
  time = 0.
  position1 = 50 # Initial position (miles)
  position2 = 50 # Initial position (miles)
  # print header for time output and initial states
  if verbose: print ("Time  Position 1  Position 2")
  if verbose: print ("%6.2f %6.2f %6.2f" % (time, position1, position2))
  while time < 10: # Run a 10 hour race
      time = time + dt
      #random velocities
      velocity1 = random.randint(35, 65)
      velocity2 = random.randint(30, 60)
      position1 = position1 + velocity1*dt
      position2 = position2 + velocity2*dt
      if verbose: print ("%6.2f %6.2f %6.2f" % (time, position1, position2))
        
  car1_distance.append(position1)
  car2_distance.append(position2)
    
  if verbose: print ("Final position: %6.2f" % position1)
  if verbose: print ("Final position2: %6.2f" % position2)

print (f"Car 1 Distance Mean  = {statistics.mean(car1_distance) :3.0f} Miles")
print (f"Car 2 Distance Mean  = {statistics.mean(car2_distance) :3.0f} Miles")

print(car1_distance)
print(car2_distance)
