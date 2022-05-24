import random
import statistics
import matplotlib.pyplot as plot

num_iterations = 100
requirements = [] # initialize list of results
effort_output = [] # initialize list of results

for iteration in range(1, num_iterations):
  number_requirements = random.uniform(100, 200)
  print(number_requirements)
  requirements.append(number_requirements)
  effort = 1006 * number_requirements**0.65
  effort_output.append(effort)
  print(effort)

mean_requirements = statistics.mean(requirements)
print ("Requirements Mean  = %3.2f" % (mean_requirements))

# use plot functions
plot.title('Requirements Histogram')
plot.xlabel('Requirements')
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
plot.hist (requirements, rwidth=0.85,)
            
# plot options
color = "blue"
num_bins = 12

# object oriented plotting

# one plot
figure, axis1 = plot.subplots()
axis1.set(title='requirements', xlabel="Requirements", ylabel='Count')
axis1.hist (requirements, num_bins, rwidth=0.85, color=color)

# two plots
figure, (axis1,axis2) = plot.subplots(2, 1, figsize=(6,6))
plot.subplots_adjust(hspace=.5, wspace=0.3)
axis1.set(title='Requirements histogram', xlabel="Requirements", ylabel='Count')
axis1.hist (requirements, num_bins, rwidth=0.85, color=color)
axis2.set(title='Effort histogram', xlabel="Effort (Person-Months)", ylabel='Count')
axis2.hist (effort_output, num_bins, rwidth=0.85, color=color)
