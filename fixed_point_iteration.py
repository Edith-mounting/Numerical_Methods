#give the g(x) function and starting point as input
def Fixed_Point_Iteration_method(g_x, xi):
    while(True):
        x_i_plus_one = g_x(xi)
        if(abs(x_i_plus_one - xi) < pow( 10, -5)):
            return x_i_plus_one
        xi = x_i_plus_one
