sixth = 1.0 / 6.0;

def runge_kutta(f, y_0, t_0, h, ylist):
  t_n = t_0
  ylist[0] = y_0
  for n in range(1, len(ylist)-1): 
    ylist[n] = next_y(f, h, t_n, ylist[n-1])
    t_n = t_n + h
  return ylist

def next_y(f, h, t_n, y_n):
  k1 = h * f(t_n, y_n)
  k2 = h * f(t_n + 0.5 * h, y_n + 0.5 * k1)
  k3 = h * f(t_n + 0.5 * h, y_n + 0.5 * k2)  
  k4 = h * f(t_n + h, y_n + k3)  
  return y_n + sixth * (k1 + 2.0 * k2 + 2.0 * k3 + k4)