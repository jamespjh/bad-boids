"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boid_count=50
flock_attraction=0.01/boid_count
avoidance_radius=10
formation_flying_radius=100
speed_matching_strength=0.125/boid_count

def initialise_boids(count):
    boids_x=[random.uniform(-450,50.0) for x in range(count)]
    boids_y=[random.uniform(300.0,600.0) for x in range(count)]
    boid_x_velocities=[random.uniform(0,10.0) for x in range(count)]
    boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(count)]
    boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
    return boids

def boid_interaction(my_x,my_y,my_xv,my_yv,his_x,his_y,his_xv,his_yv):
    delta_v_x=0
    delta_v_y=0

    x_separation=his_x-my_x
    y_separation=his_y-my_y
    
    # Fly towards the middle
    delta_v_x+=x_separation*flock_attraction
    delta_v_y+=y_separation*flock_attraction
    
    # Fly away from nearby boids
    if x_separation**2 + y_separation**2 < avoidance_radius**2:
        delta_v_x-=x_separation
        delta_v_y-=y_separation
    
    # Try to match speed with nearby boids
    if x_separation**2 + y_separation**2 < formation_flying_radius**2:
        delta_v_x+=(his_xv-my_xv)*speed_matching_strength
        delta_v_y+=(his_yv-my_yv)*speed_matching_strength
    return delta_v_x,delta_v_y


def update_boids(boids):
    xs,ys,xvs,yvs=boids
    for i in range(len(xs)):
        delta_v_x=0
        delta_v_y=0
        for j in range(len(xs)):
            interaction=boid_interaction(xs[i],ys[i],xvs[i],yvs[i],xs[j],ys[j],xvs[j],yvs[j])
            delta_v_x+=interaction[0]
            delta_v_y+=interaction[1]
        # Accelerate as stated
        xvs[i]+=delta_v_x
        yvs[i]+=delta_v_y
        # Move according to velocities
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]


boids=initialise_boids(boid_count)
figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
        frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
