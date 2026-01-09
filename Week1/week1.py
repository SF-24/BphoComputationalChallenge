import math
import matplotlib.pyplot as plt
import numpy as np

g = 9.81
xMax = 30.0

# Create a linear set of values with 1000 iterations
x = np.linspace(0.0,xMax,1000)

# Create an array of times
t = ([])
for i in x:
    t.append(math.sqrt(2 * i / g))

# Plot a graph of plot time against drop distance.

plt.plot(x,t,'r-','linewidth',2)
plt.show()

