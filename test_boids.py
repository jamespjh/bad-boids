import boids as bd
from nose.tools import assert_almost_equal, assert_greater, assert_less, assert_equal
import os
import yaml

def test_bad_boids_regression():
    boids=bd.Boids(50,0.01/50,10,100,0.125/50)
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boids.initialise_from_data(regression_data["before"])
    boids.update()
    current_data=(boids.xs,boids.ys,boids.xvs,boids.yvs)
    for after,before in zip(regression_data["after"],current_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
def test_bad_boids_initialisation():
    boids=bd.Boids(15,1.0,10.0,100.0,0.5)
    boids.initialise_random()
    assert_equal(len(boids.xs),15)
    for x in boids.xs:
        assert_less(x,50.0)
        assert_greater(x,-450)
    for y in boids.ys:
        assert_less(y,600)
        assert_greater(y,300)
    for xv in boids.xvs:
        assert_less(xv,10.0)
        assert_greater(xv,0)
    for yv in boids.yvs:
        assert_less(yv,20.0)
        assert_greater(yv,-20.0)
