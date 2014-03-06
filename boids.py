"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random

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
        self.xs=[random.uniform(-450,50.0) for x in range(self.count)]
        self.ys=[random.uniform(300.0,600.0) for x in range(self.count)]
        self.xvs=[random.uniform(0,10.0) for x in range(self.count)]
        self.yvs=[random.uniform(-20.0,20.0) for x in range(self.count)]

    def initialise_from_data(self,data):
        self.xs,self.ys,self.xvs,self.yvs=data

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
        for i in range(self.count):
            delta_v_x=0
            delta_v_y=0
            for j in range(self.count):
                interaction=self.boid_interaction(self.xs[i],self.ys[i],self.xvs[i],
                        self.yvs[i],self.xs[j],self.ys[j],self.xvs[j],self.yvs[j])
                delta_v_x+=interaction[0]
                delta_v_y+=interaction[1]
            # Accelerate as stated
            self.xvs[i]+=delta_v_x
            self.yvs[i]+=delta_v_y
            # Move according to velocities
            self.xs[i]+=self.xvs[i]
            self.ys[i]+=self.yvs[i]



