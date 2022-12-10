#give the g(x) function and starting point as input
import math
def g_x(x):
    return math.pow((x**3 + 2*x)/3, 1/2)

def Fixed_Point_Iteration_method(g_x, xi):
    w = 0.00001
    while(True):
        x_i_plus_one = w*xi + (1 - w)*g_x(xi)
        if(abs(x_i_plus_one - xi) < pow( 10, -5)):
            return x_i_plus_one
        print(xi)
        xi = x_i_plus_one


print(Fixed_Point_Iteration_method(g_x, 3))