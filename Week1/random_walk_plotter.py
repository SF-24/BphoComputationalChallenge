# TODO: Do later
# Take a fixed step of l metres
# Between each step change the direction by a random value
# Plot first "n" steps.
import math
import matplotlib.pyplot as plt
import numpy as np

# Optimises line rendering at some cost of quality
plt.rcParams['path.simplify'] = True

# Func. generates random motion from origin
def random_walk_demo(step_length, steps):
    x=[0.0]
    y=[0.0]
    for i in range(int(n)):
        theta=2*math.pi*np.random.random()
        dx = l*math.cos(theta)
        dy = l*math.sin(theta)
        x.append(x[i]+dx)
        y.append(y[i]+dy)
    return [x,y]

n = 1e6 # Step count (-1)
l = 1   # Step size
fig, ax = plt.subplots()
# Pregenerate colours
RGB=np.random.random((20,3))

# Iterate
for k in range(20):
    [x_,y_]=random_walk_demo(l,n)
    # plot the random walk
    ax.plot(x_,y_, color=RGB[k])

# Show result
print("Showing axis")
plt.show()
print("Code execution finished")