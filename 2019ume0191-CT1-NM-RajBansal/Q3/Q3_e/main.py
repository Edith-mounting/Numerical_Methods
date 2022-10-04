def g_x(x):
    return 1/(x + 1)
def Fixed_Point_Iteration_method(g_x, xi, w):
    while(True):
        print(xi)
        x_i_plus_one = (g_x(xi) + (1 - w)*g_x(xi))/2
        if(abs(x_i_plus_one - xi) < epsilon):
            return x_i_plus_one
        xi = x_i_plus_one
xi = -1.5
w = 0.02
epsilon = pow( 10, -5)
Fixed_Point_Iteration_method( g_x, xi, w)