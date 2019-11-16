from runge_kutta import runge_kutta
import math

def linear_in_t(t_n, y_n):
  return 2.0 * t_n

def assertEquals(x1, x2, delta, t):
  if math.fabs(x1-x2) > delta:
    raise Exception('Excpected {} but got {} at t={}'.format(x1, x2, t))

def should_approximate_t_squared():
  y_0 = 0.0
  t_0 = 0.0
  steps = 100
  h = 1.0 / float(steps)
  ylist = [0.0 for i in range(steps)]
  runge_kutta(linear_in_t, y_0, t_0, h, ylist)

  for i in range(0, steps-1):
    t = float(i) * h
    assertEquals(ylist[i], t*t, 0.000000000000001, t)
  
  print("should_approximate_t_squared OK")
  return