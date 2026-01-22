#
# a = - (omega)^2 * x
#
import math
from configparser import MAX_INTERPOLATION_DEPTH

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib ; matplotlib.use('TkAgg')  # or 'nbAgg' for Jupyter

radius = 0.1
x = [-1.0]
v = [0.0]
T = 1.0 # period in seconds
omega = 2*math.pi/T

dt = 0.01 # time change in seconds.

maxIterations = 10000

# Generate dataset
for n in range(maxIterations):
    a = -math.pow(omega,2)*x[n]
    v.append(v[n] + a*dt)
    x.append(x[n] + v[n+1]*dt)
    print("Iteration: " + str(n) + " Position: " + str(x[n]))

fig, ax = plt.subplots()
ax.set_aspect("equal")
# Define the ball object

def init():
    ball.center=(x[0],0)
    return [ball]

def get_frame_position(it=0):
    it+=1
    return it

def animate(i):
    x_position = get_x_pos_from_iteration(i)
    ball.center = (x_position, 0.0)
    return [ball]

def get_x_pos_from_iteration(iteration):
    print("iteration: " + str(iteration))
    if iteration>=maxIterations:
        print("Max iterations exceeded")
        return x[int(maxIterations-1)]
    return x[int(iteration)]

ball = plt.Circle((x[0],0),radius)
ax.add_patch(ball)
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-0.5,0.5)

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=maxIterations,
    blit=False,
    interval=dt*1000,
    repeat=False,
    cache_frame_data=True,
    init_func=init
)
plt.ion()
plt.show(block=True)

