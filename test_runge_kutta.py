import unittest
from runge_kutta import runge_kutta
import math

class TestRungeKutta(unittest.TestCase):

  def assertEquals(self, x1, x2, delta, t):
    self.assertFalse(math.fabs(x1-x2) > delta, 'Excpected {} but got {} at t={}'.format(x1, x2, t))

  def test_should_approximate_t_squared(self):
    y_0 = 0.0
    t_0 = 0.0
    steps = 100
    h = 1.0 / float(steps)
    function_2_t = lambda t_n, y_n: 2.0 * t_n
    ylist = [0.0 for i in range(steps)]
    runge_kutta(function_2_t, y_0, t_0, h, ylist)

    for i in range(0, steps-1):
      t = float(i) * h
      self.assertEquals(ylist[i], t*t, 0.000000000000001, t)
    
    return