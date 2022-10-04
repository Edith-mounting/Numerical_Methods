def g_x(x):
    return 1/(x + 1)

def aitken_steffenson_acceleration_method(xi):
    while True:
        xi_plus_one = g_x(xi)
        xi_plus_two = g_x(xi_plus_one)
        x_next = xi - (pow(xi_plus_one - xi, 2)/(xi_plus_two - 2*xi_plus_one + xi))
        print(xi)
        if(abs(x_next - xi) < epsilon):
            return xi
        xi = x_next

xi = -4
epsilon = pow( 10, -5)
aitken_steffenson_acceleration_method(xi)