import matplotlib;
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')  # or 'nbAgg' for Jupyter
import custom_lib as cp

# Constants
AU = 149597900000.0
slingshot= True

if not slingshot:
    M=1988475000000000000000000000000.0
    m=1000000.0 #1000000.0
    dt=100 #86400 # in seconds

    axis_scales=4 # was 5
    n=1000000
    interval=1000
    mass_v_x_init = 0  #15000.0
    mass_v_y_init = 21000  #15000.0
    mass_x = [1.0*AU]
    mass_y = [0*AU]

else:
    M=1988475000000000000000000000000.0
    m=1000000.0 #1000000.0
    dt=100 #86400 # in seconds

    axis_scales=1.5  # was 5
    n=1000000
    interval=1000
    mass_v_x_init = -1000  #15000.0
    mass_v_y_init = 31000  #15000.0
    mass_x = [0.8*AU]
    mass_y = [2.3*AU]

mass_v_x = [-mass_v_x_init] # in ms-1
mass_v_y = [-mass_v_y_init] #/149597900.0]

for i in range(n):
    mass_x.append(mass_v_x[i]*dt+mass_x[i])
    mass_y.append(mass_v_y[i]*dt+mass_y[i])
    r_sq=cp.get_distance_squared(0,0,mass_x[i],mass_y[i])
    if r_sq==0:
        print("Error. distance is 0.")
        break
    angle_x,angle_y=cp.get_vector_resolver(0,0,mass_x[i],mass_y[i])
    # Velocity and acceleration
    a = cp.get_gravitational_acceleration(M,m,r_sq)
    mass_v_x.append(mass_v_x[i] + a*angle_x * dt)
    mass_v_y.append(mass_v_y[i] + a*angle_y * dt)

# Declare axis
fig, ax = plt.subplots()
ax.set_aspect("equal")
# Axis sizes and circles for motion
ax.set_xlabel('x / AU')
ax.set_ylabel('y / AU')
ax.set_title('Simple Gravity Simulation')
ax.grid(True)
ax.set_xlim(-axis_scales,axis_scales)
ax.set_ylim(-axis_scales,axis_scales)

# Declare objects
star = plt.Circle((0,0),0.2)
mass = plt.Circle((0,0),0.1)
ax.add_patch(star)
ax.add_patch(mass)
ax.plot(np.divide(mass_x,AU), np.divide(mass_y, AU), label='Orbit')

# Initialise objects
def init():
    mass.center=(mass_x[0]/AU,mass_y[0]/AU)
    return [mass]

def get_frame_position(it=0):
    it+=1
    return it

# Run anim.
def animate(i):
    if i>=n:
        anim.new_frame_seq()
        return [mass]
    # and (np.abs(mass_x[i])/AU>axis_scales or np.abs(mass_y[i])/AU>axis_scales):
    mass.center = (mass_x[i*interval]/AU, mass_y[i*interval]/AU)
    return [mass]

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=2, blit=True) # interval was 20

plt.ion()
plt.show(block=True)
plt.pause(2.0)
