import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')  # or 'nbAgg' for Jupyter
import custom_lib as cp

# Constants
AU = 149597900000.0
slingshot= True

class MassObject:
    # x = []
    # y = []
    # v_x = []
    # v_y = []
    # radius = 0.1
    # anim_object: Circle = plt.Circle((0,0),0.1, color='red')
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

objects = [MassObject(0,0,0,0,0, 0.1, "red")]
objects.clear()

def create_object(mass, x_0, y_0, v_x_0, v_y_0, radius, colour):
    new_object = MassObject(mass, x_0, y_0, v_x_0, v_y_0, radius, colour)
    objects.append(new_object)

dt=1000 # was 1000 #86400 # in seconds
n=50000 # was 1000000
interval=100
axis_scales=5  # was 5

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

def init():
    for mass_obj in objects:
        mass_obj.anim_object.center = (mass_obj.x[0]/AU, mass_obj.y[0]/AU)
        # ax.add_patch(mass_obj.anim_object)
    return [m.anim_object for m in objects]
    # anim_objects = []
    # for mass_obj_0 in objects:
    #     mass_obj_0.anim_object.center = (mass_obj_0.x[0]/AU, mass_obj_0.y[0]/AU)
    #     ax.add_patch(mass_obj_0.anim_object)
    #     anim_objects.append(mass_obj_0.anim_object)
    # return anim_objects

def get_frame_position(it=0):
    it+=1
    return it

# Run anim.
def animate(i):
    for mass_obj in objects:
        mass_obj.anim_object.center = (mass_obj.x[i*interval]/AU, mass_obj.y[i*interval]/AU)
    return [m.anim_object for m in objects]  # SAME artists every time
    # anim_objects = []
    # if i>=n:
    #     return anim_objects
    # for mass_obj_1 in objects:
    #     mass_obj_1.anim_object.center=(mass_obj_1.x[i] / AU, mass_obj_1.y[i] / AU)
    #     anim_objects.append(mass_obj_1.anim_object)
    # return anim_objects

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

    print(len(objects))                 # should be 2
    print(objects[0].x[0], objects[0].y[0])  # 0.0 0.0
    print(objects[1].x[0], objects[1].y[0])  # 1.0 1.0
    print(objects[1].x[10], objects[1].y[10])  # should differ from (0,0)

    # Initialise objects
    for mass_obj_plot in objects:
        ax.plot(np.divide(mass_obj_plot.x,AU), np.divide(mass_obj_plot.y, AU), label='Orbit',zorder=1)
        ax.add_patch(mass_obj_plot.anim_object)

    frame_num= int(np.floor(n / interval))
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frame_num, interval=5, blit=True) # interval was 20

    # Export
    writer = animation.PillowWriter (fps=30)
    anim.save('gravity.gif', writer=writer)

    plt.ion()
    # plt.show(block=True)
    plt.pause(2.0)

    print("Simulation complete.")

