#
# a = - (omega)^2 * x
#
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib ; matplotlib.use('TkAgg')  # or 'nbAgg' for Jupyter

radius = 0.1
x = [-1.0]
v = [0.0]
t = [0.0]
T = 1.0 # period in seconds
omega = 2*math.pi/T

k=1.0 # constant for resistive force.
# SET TO k=0 FOR SIMPLE HARMONIC MOTION
# SET TO k=10 FOR CRITICAL DAMPING

dt = 0.01 # time change in seconds.

maxIterations = 1000

# Generate dataset
for n in range(maxIterations):
    a = -math.pow(omega,2)*x[n] -k*v[n]
    v.append(v[n] + a*dt)
    x.append(x[n] + v[n+1]*dt)
    t.append(t[n]+dt)

fig, ax = plt.subplots(2)
ax[0].set_aspect("equal")
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
    if iteration>=maxIterations:
        return x[int(maxIterations-1)]
    return x[int(iteration)]

ball = plt.Circle((x[0],0),radius)
ax[0].add_patch(ball)
ax[0].set_xlim(-1.2,1.2)
ax[0].set_ylim(-0.5,0.5)

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
ax[1].set_xlim(0.0,maxIterations*dt)
ax[1].set_ylim(-1.0,1.0)
ax[1].plot(t,x)
plt.ion()
plt.show(block=True)
plt.pause(2.0)

