
def g_x(x):
    return 1/(x + 1)
def Fixed_Point_Iteration_method(g_x, xi):
    while(True):
        print(xi)
        x_i_plus_one = g_x(xi)
        if(abs(x_i_plus_one - xi) < epsilon):
            return x_i_plus_one
        xi = x_i_plus_one
xi = -4
epsilon = pow( 10, -5)
Fixed_Point_Iteration_method( g_x, xi)