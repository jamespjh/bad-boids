import boids
from nose.tools import assert_almost_equal, assert_greater, assert_less, assert_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    boids.update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
def test_bad_boids_initialisation():
    xs,ys,xvs,yvs=boids.initialise_boids()
    assert_equal(len(xs),boids.boid_count)
    for x in xs:
        assert_less(x,50.0)
        assert_greater(x,-450)
    for y in ys:
        assert_less(y,600)
        assert_greater(y,300)
    for xv in xvs:
        assert_less(xv,10.0)
        assert_greater(xv,0)
    for yv in yvs:
        assert_less(yv,20.0)
        assert_greater(yv,-20.0)
