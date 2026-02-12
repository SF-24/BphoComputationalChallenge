import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib ; matplotlib.use('TkAgg')  # or 'nbAgg' for Jupyter
import numpy as np

r_mercury=0.387
p_mercury=0.24 # Orbital period in years
r_venus=0.723
p_venus=0.615 # Orbital period in years
r_earth=1
p_earth=1 # Orbital period in years
r_mars=1.523
p_mars=r_mars**1.5 # Orbital period in years

t = np.linspace(0,5*p_mars,1000)
theta_sun = 2*np.pi*np.random.random() + 2*np.pi*t/p_earth
theta_mercury = 2*np.pi*np.random.random() + 2*np.pi*t/p_earth
theta_venus = 2*np.pi*np.random.random() + 2*np.pi*t/p_earth
theta_earth = 2*np.pi*np.random.random() + 2*np.pi*t/p_earth
theta_mars = 2*np.pi*np.random.random() + 2*np.pi*t/p_mars
x_mercury = r_mercury*np.cos(theta_mercury); y_mercury=r_mercury*np.sin(theta_mercury)
x_venus = r_venus*np.cos(theta_venus); y_venus=r_venus*np.sin(theta_venus)
x_earth = r_earth*np.cos(theta_earth); y_earth=r_earth*np.sin(theta_earth)
x_mars = r_mars*np.cos(theta_mars); y_mars=r_mars*np.sin(theta_mars)

# Declare axis
fig, ax = plt.subplots(1)
ax.set_aspect("equal")

# Declare objects
sun = plt.Circle((0,0),0.2)
mercury = plt.Circle((0,0),0.09)
venus = plt.Circle((0,0),0.11)
earth = plt.Circle((0,0),0.13)
mars = plt.Circle((0,0),0.11)
ax.add_patch(sun)
ax.add_patch(mercury)
ax.add_patch(venus)
ax.add_patch(earth)
ax.add_patch(mars)

# Axis sizes and circles for motion
ax.set_xlabel('x / AU')
ax.set_ylabel('y / AU')
ax.set_title('Simple Inner Solary System Orbits (not to scale!)')
ax.grid(True)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.plot(x_mercury, y_mercury, label='Mercury orbit')
ax.plot(x_venus, y_venus, label='Venus orbit')
ax.plot(x_earth, y_earth, label='Earth orbit')
ax.plot(x_mars, y_mars, label='Mars orbit')

# Initialise objects
def init():
    mercury.center=(x_mercury[0],y_mercury[0])
    venus.center=(x_venus[0],y_venus[0])
    earth.center=(x_earth[0],y_earth[0])
    mars.center=(x_mars[0],y_mars[0])
    return [mercury,venus,earth,mars]

def get_frame_position(it=0):
    it+=1
    return it

# Run anim.
def animate(i):
    mercury.center=(x_mercury[i],y_mercury[i])
    venus.center=(x_venus[i],y_venus[i])
    earth.center = (x_earth[i], y_earth[i])
    mars.center = (x_mars[i], y_mars[i])
    return [mercury,venus,earth,mars]

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=20, blit=True)

# ani = animation.FuncAnimation(
#     fig,
#     animate,
#     frames=t.max(),
#     blit=False,
#     interval=1000,
#     repeat=False,
#     cache_frame_data=True,
#     init_func=init
# )

plt.ion()
plt.show(block=True)
plt.pause(2.0)
