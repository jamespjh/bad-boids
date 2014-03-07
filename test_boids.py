import boids as bd
from nose.tools import assert_almost_equal, assert_greater
from nose.tools import assert_less, assert_equal, assert_sequence_equal
import os
import yaml

def test_bad_boids_regression():
    boids=bd.Boids(50,0.01/50,10,100,0.125/50)
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boids.initialise_from_data(regression_data["before"])
    boids.update()
    for index,boid in enumerate(boids.boids):
        assert_almost_equal(boid.x,regression_data["after"][0][index],delta=0.01)
        assert_almost_equal(boid.y,regression_data["after"][1][index],delta=0.01)
        assert_almost_equal(boid.xv,regression_data["after"][2][index],delta=0.01)
        assert_almost_equal(boid.yv,regression_data["after"][3][index],delta=0.01)

	
def test_bad_boids_initialisation():
    boids=bd.Boids(15,1.0,10.0,100.0,0.5)
    boids.initialise_random()
    assert_equal(len(boids.boids),15)
    for boid in boids.boids:
        assert_less(boid.x,50.0)
        assert_greater(boid.x,-450)
        assert_less(boid.y,600)
        assert_greater(boid.y,300)
        assert_less(boid.xv,10.0)
        assert_greater(boid.xv,0)
        assert_less(boid.yv,20.0)
        assert_greater(boid.yv,-20.0)

def test_boid_interaction_fly_to_middle():
    boids=bd.Boids(2,3.0,2.0,10,0)
    first=bd.Boid(0,0,1,0,boids)
    second=bd.Boid(0,5,0,0,boids)
    assert_sequence_equal(first.interaction(second),[0.0,15.0])
