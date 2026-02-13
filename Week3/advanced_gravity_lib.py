import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')  # or 'nbAgg' for Jupyter

# A library created in python and visible as a file outside the week folders ('custom_lib.py')
# It is required for many of the simulations (starting in Week 3) to run.
import custom_lib as cp

# Constants. Used in physics calculations.
# Here, only the astronomical unit given in metres.
AU = 149597900000.0

# The class definition of the mass object in the simulation.
class MassObject:
    def __init__(self, mass, x_0, y_0, v_x_0, v_y_0, radius, colour):
        self.mass = mass
        self.x=[x_0]
        self.y=[y_0]
        self.v_x=[v_x_0]
        self.v_y=[v_y_0]
        self.radius=radius
        self.anim_object = plt.Circle((x_0/AU,y_0/AU),radius, color=colour,zorder=3)
    def get_pos(self):
        return self.x,self.y
    def get_velocity(self):
        return self.v_x,self.v_y
    def get_mass(self):
        return self.mass
    def add_velocity(self, v_x, v_y):
        self.v_x.append(v_x)
        self.v_y.append(v_y)
    def add_pos(self, x, y):
        self.x.append(x)
        self.y.append(y)

# Adding the object registers the list type
objects = [MassObject(0,0,0,0,0, 0.1, "red")]
objects.clear()

# Object creation class. Used by an external file to add mass objects to the simulation
def create_object(mass, x_0, y_0, v_x_0, v_y_0, radius, colour):
    new_object = MassObject(mass, x_0, y_0, v_x_0, v_y_0, radius, colour)
    objects.append(new_object)

# Declare variables. A smaller dt gives a more accurate simulation
# n determines the number of iterations the simulation runs for
# The interval is the interval in iterations where a frame is rendered.
# Axis scales determines the size of the area which is visible in the render.
dt=1000 #86400 # in seconds
n=50000 # was 1000000
interval=100
axis_scales=5  # was 5

# Simulate the motion
# This is done by determining the force and applying acceleration to velocity
# The velocity is then applied to the position of the object.
# Each object is acted upon by every other object by a gravitational force.
def simulate():
    # Create mass object0

    for i in range(n):
        for mass_obj in objects:
            x = mass_obj.x
            y = mass_obj.y
            x_ = x[i]
            y_ = y[i]
            v_x = mass_obj.v_x[i]
            v_y = mass_obj.v_y[i]
            for M_obj in objects:
                if not(mass_obj==M_obj):
                    x0 = M_obj.x[i]
                    y0 = M_obj.y[i]
                    dx,dy=cp.get_vector_resolver(x0,y0,x_,y_)
                    a = cp.get_gravitational_acceleration(M_obj.mass,mass_obj.mass,cp.get_distance_squared(x0,y0,x_,y_))
                    v_x+=dx*a*dt
                    v_y+=dy*a*dt
            x_+=v_x*dt
            y_+=v_y*dt
            mass_obj.add_velocity(v_x,v_y)
            mass_obj.add_pos(x_,y_)
    print("[ASI] Completed simulation calculations")

# When animation starts
def init():
    for mass_obj in objects:
        mass_obj.anim_object.center = (mass_obj.x[0]/AU, mass_obj.y[0]/AU)
    return [m.anim_object for m in objects]

# Get current frame
def get_frame_position(it=0):
    it+=1
    return it

# Run animation
def animate(i):
    for mass_obj in objects:
        mass_obj.anim_object.center = (mass_obj.x[i*interval]/AU, mass_obj.y[i*interval]/AU)
    return [m.anim_object for m in objects]  # SAME artists every time

# Render an animation of the simulation. Required to export it or preview it
def render():
    # Declare axis
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    # Axis sizes and circles for motion
    ax.set_xlabel('x / AU')
    ax.set_ylabel('y / AU')
    ax.set_title('Less Simple Gravity Simulation')
    ax.grid(True)
    ax.set_xlim(-axis_scales,axis_scales)
    ax.set_ylim(-axis_scales,axis_scales)

    # Initialise objects
    for mass_obj_plot in objects:
        ax.plot(np.divide(mass_obj_plot.x,AU), np.divide(mass_obj_plot.y, AU), label='Orbit',zorder=1)
        ax.add_patch(mass_obj_plot.anim_object)

    frame_num= int(np.floor(n / interval))
    global anim
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frame_num, interval=5, blit=True) # interval was 20
    print("[ASI] Simulation rendering complete")

# Preview the simulation in a separate window
# Must first render the animation
def preview():
    print("[ASI] Opening simulation preview")
    plt.ion()
    plt.show(block=True)
    plt.pause(2.0)

# Export the simulation as a GIF
# Requires you to first render the animation
def export(filename):
    print("[ASI] Exporting simulation preview")
    # Export
    writer = animation.PillowWriter (fps=30)
    anim.save(filename + '.gif', writer=writer)
    print("[ASI] Simulation export complete")

