import numpy as np
import matplotlib.pyplot as plot

# numpy random sampling function at https ://docs.scipy.org/doc/numpy/reference/routines.random.html
number_samples = 1000

uniform = np.random.uniform(2,5,number_samples)
normal = np.random.standard_normal(number_samples)
triangle = np.random.triangular(0, 2, 8, number_samples)
rayleigh = np.random.rayleigh(3, number_samples)

# options to override defaults
color = "blue"
num_bins = 12
rwidth=0.85 # relative width of the bars as a fraction of the bin width

# single plot using functions
plot.hist (normal, num_bins, rwidth=rwidth, color=color)
plot.title('Normal Distribution')
plot.xlabel('X')
plot.ylabel('Frequency')
plot.savefig('normal histogram.png')

# object-oriented single plot 
figure, axis = plot.subplots()
axis.set(title='Triangle', xlabel = 'X', ylabel='Frequency')
axis.hist (triangle, num_bins, rwidth=rwidth, color=color)
plot.savefig('triangle histogram.png')

# object-oriented 4-per plot
figure, ((axis1, axis2), (axis3, axis4)) = plot.subplots(2, 2)
figure.suptitle('# samples = '+str(number_samples))

axis1.set(title='Uniform', xlabel = 'X', ylabel='Frequency')
axis1.hist (uniform, num_bins, rwidth=rwidth, color=color)

axis2.set(title='Normal', xlabel = 'X', ylabel='Frequency')
axis2.hist (normal, num_bins, rwidth=rwidth, color=color)

axis3.set(title='Triangle', xlabel = 'X', ylabel='Frequency')
axis3.hist (triangle, num_bins, rwidth=rwidth, color=color)

axis4.set(title='Rayleigh', xlabel = 'X', ylabel='Frequency')
axis4.hist (rayleigh, num_bins, rwidth=rwidth, color=color)

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
plot.subplots_adjust(hspace=0.5, wspace=0.3)

plot.savefig('histograms.png')
