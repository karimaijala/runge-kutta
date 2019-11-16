# runge-kutta
A simple and naïve Runge-Kutta method implementation.

The function runge_kutta in [runge_kutta.py](runge_kutta.py) implements a simple [Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) method.
[runge_kutta_test.py](runge_kutta_test.py) tests the runge_kutta method. 
The test integrates a linear function f(t)=2t and asserts that the result is t^2 within error bounds. 
