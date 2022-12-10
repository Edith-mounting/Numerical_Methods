import math

def g_x(x):
    return math.pow(3*x*x - 2*x, (1/3))
   
def aitken_steffenson_acceleration_method(xi):
    while True:
        xi_plus_one = g_x(xi)
        xi_plus_two = g_x(xi_plus_one)
        x_next = xi - (pow(xi_plus_one - xi, 2)/(xi_plus_two - 2*xi_plus_one + xi))
        print(xi)
        if(abs(x_next - xi) < pow( 10, -5)):
            return xi
        xi = x_next

print( aitken_steffenson_acceleration_method(3))
