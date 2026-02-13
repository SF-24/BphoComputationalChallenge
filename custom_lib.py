import numpy as np

G=0.0000000000667

def get_gravitational_force(M,m,r_squared):
    if r_squared==0: return 0;
    return -G*M*m/r_squared

def get_distance_squared(x_0,y_0,x_1,y_1):
    return (x_0-x_1)**2+(y_0-y_1)**2

def get_vector_resolver(x_0,y_0,x_1,y_1):
    dx = x_1 - x_0  # Vector FROM planet TO sun
    dy = y_1 - y_0
    r = np.sqrt(dx*dx+dy*dy)
    if r==0: return 1,1
    dx/=r
    dy/=r
    return dx,dy

def get_gravitational_acceleration(M,m,r_squared):
    return get_gravitational_force(M,m,r_squared)/m
