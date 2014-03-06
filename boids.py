"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random

class Boid(object):
    def __init__(self,x,y,xv,yv):
        self.x=x
        self.y=y
        self.xv=xv
        self.yv=yv

# Deliberately terrible code for teaching purposes
class Boids(object):
    def __init__(self,
            boid_count,flock_attraction,avoidance_radius,
            formation_flying_radius,speed_matching_strength):
        self.count=boid_count
        self.flock_attraction=flock_attraction
        self.avoidance_radius=avoidance_radius
        self.formation_flying_radius=formation_flying_radius
        self.speed_matching_strength=speed_matching_strength


    def initialise_random(self):
        self.boids=[Boid(random.uniform(-450,50.0),
                random.uniform(300.0,600.0),
                random.uniform(0,10.0),
                random.uniform(-20.0,20.0)) for i in range(self.count)]

    def initialise_from_data(self,data):
        self.boids=[Boid(x,y,xv,yv) for x,y,xv,yv in zip(*data)]

    def boid_interaction(self,my_x,my_y,my_xv,my_yv,his_x,his_y,his_xv,his_yv):
        delta_v_x=0
        delta_v_y=0

        x_separation=his_x-my_x
        y_separation=his_y-my_y

        # Fly towards the middle
        delta_v_x+=x_separation*self.flock_attraction
        delta_v_y+=y_separation*self.flock_attraction

        # Fly away from nearby boids
        if x_separation**2 + y_separation**2 < self.avoidance_radius**2:
            delta_v_x-=x_separation
            delta_v_y-=y_separation

        # Try to match speed with nearby boids
        if x_separation**2 + y_separation**2 < self.formation_flying_radius**2:
            delta_v_x+=(his_xv-my_xv)*self.speed_matching_strength
            delta_v_y+=(his_yv-my_yv)*self.speed_matching_strength

        return delta_v_x,delta_v_y

    def update(self):
        for me in self.boids:
            delta_v_x=0
            delta_v_y=0
            for him in self.boids:
                interaction=self.boid_interaction(me.x,me.y,me.xv,me.yv,
                       him.x,him.y,him.xv,him.yv)
                delta_v_x+=interaction[0]
                delta_v_y+=interaction[1]
            # Accelerate as stated
            me.xv+=delta_v_x
            me.yv+=delta_v_y
            # Move according to velocities
            me.x+=me.xv
            me.y+=me.yv



