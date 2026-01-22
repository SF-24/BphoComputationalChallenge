import math

n=0
x=[1.0]
v=[1.0]
t=[0.0]
g=9.81
dt=0.01
e=0.8 # Restitution coefficient
max_bounce=20
current_bounce=0

# Simulate bouncing
while current_bounce>max_bounce:
    # Iterate
    x.append(x[n]-v[n]*dt-0.5*g*math.pow(dt,2))
    v.append(v[n]+g*dt)
    t.append(t[n]+dt)
    if x[n + 1] < 0 < v[n + 1]: # If bounced
        current_bounce+=1
        v[n+1]=v[n]*e # Apply restitution
    n+=1

# Time taken to stop bouncing
T = 2*math.sqrt(2*x[0]/g)*(1/(1-e)-0.5)
print(T)



