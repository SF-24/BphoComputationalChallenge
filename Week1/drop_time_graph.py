import math
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib docs: https://matplotlib.org
# Colour list: https://matplotlib.org/stable/gallery/color/named_colors.html

g = 9.81
xMax = 30.0
fontSize=12

# Create a linear set of values with 1000 iterations
x = np.linspace(0.0,xMax,1000)

# Create an array of times
t = ([])
for i in x:
    t.append(math.sqrt(2 * i / g))

# Plot a graph of plot time against drop distance.

plt.plot(x,t,'r-',linewidth=2)
plt.box(on=True)
plt.setp(plt.xlabel('x'),fontsize=fontSize)
plt.setp(plt.ylabel('y'),fontsize=fontSize)
plt.grid(color='silver', linestyle='-', linewidth=1, axis='both')
plt.xlabel('distance: x/m')
plt.ylabel('time: t/s')
plt.title('Distance dropped vs time taken without air resistance')
plt.show()