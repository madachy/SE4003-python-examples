# calculate position over time with random velocity values

import random
    
time = 0.
dt = .25 # Timestep
position = 50 # Initial position (miles)
velocity = 60 # Velocity (miles/hour)

# header for time output and starting values
print ("Time  Position  Velocity")
print ("%6.2f %6.2f %6.2f" % (time, position, velocity))
       
# Run for 10 hours
while time < 10:
    time = time + dt
    #random velocity between 30 and 60
    velocity = random.randint(30, 60)
    position = position + velocity*dt
    print ("%6.2f %6.2f %6.2f" % (time, position, velocity))

print ("Final position: %6.2f" % position)
