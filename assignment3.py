import math
from fixed_point_iteration import Fixed_Point_Iteration_method
from bisection import bisection_method
from regular_falsi import Regular_Falsi_method

def f_1(c):
    m = 68.1
    g = 9.8
    v = 40
    t = 10
    return ((m*g*(math.exp((-c*t)/m) - 1)) + v*c)

def g8_x(x):
    return math.cos(x)

def g9_x(x):
    return math.asin(math.exp(-x))

def g10_x(x):
    return math.sqrt((10 - x*x*x)/4)

# print(bisection_method( 1, 100, f_1))
print(Regular_Falsi_method( 1, 100, f_1))
# print(Fixed_Point_Iteration_method(g8_x))
# print(Fixed_Point_Iteration_method(g9_x))
# print(Fixed_Point_Iteration_method(g10_x, -1))