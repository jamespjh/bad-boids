import boids as bd
from nose.tools import assert_almost_equal, assert_greater
from nose.tools import assert_less, assert_equal, assert_sequence_equal
from numpy.testing import assert_array_equal
import os
import yaml

def test_bad_boids_regression():
    boids=bd.Boids(50,0.01/50,10,100,0.125/50)
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boids.initialise_from_data(regression_data["before"])
    boids.update()
    for index,boid in enumerate(boids.boids):
        assert_almost_equal(boid.position[0],regression_data["after"][0][index],delta=0.01)
        assert_almost_equal(boid.position[1],regression_data["after"][1][index],delta=0.01)
        assert_almost_equal(boid.velocity[0],regression_data["after"][2][index],delta=0.01)
        assert_almost_equal(boid.velocity[1],regression_data["after"][3][index],delta=0.01)

	
def test_bad_boids_initialisation():
    boids=bd.Boids(15,1.0,10.0,100.0,0.5)
    boids.initialise_random()
    assert_equal(len(boids.boids),15)
    for boid in boids.boids:
        assert_less(boid.position[0],50.0)
        assert_greater(boid.position[0],-450)
        assert_less(boid.position[1],600)
        assert_greater(boid.position[1],300)
        assert_less(boid.velocity[0],10.0)
        assert_greater(boid.velocity[0],0)
        assert_less(boid.velocity[1],20.0)
        assert_greater(boid.velocity[1],-20.0)

def test_boid_interaction_fly_to_middle():
    boids=bd.Boids(2,3.0,2.0,10,0)
    first=bd.Boid(0,0,1,0,boids)
    second=bd.Boid(0,5,0,0,boids)
    assert_array_equal(first.interaction(second),[0.0,15.0])

def test_boid_interaction_avoidance():
    boids=bd.Boids(2,3.0,10.0,10,0)
    first=bd.Boid(0,0,1,0,boids)
    second=bd.Boid(0,5,0,0,boids)
    assert_array_equal(first.interaction(second),[0.0,10.0])

def test_boid_interaction_formation():
    boids=bd.Boids(2,3.0,2.0,10.0,7.0)
    first=bd.Boid(0,0,0.0,0,boids)
    second=bd.Boid(0,5,11.0,0,boids)
    assert_array_equal(first.interaction(second),[11.0*7.0,15.0])
