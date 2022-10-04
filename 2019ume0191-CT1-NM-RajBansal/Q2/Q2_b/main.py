def f_1(x):
    return x*x + x -1
def f_dash(x):
    return 2*x + 1
def newton_raphson_method( xi):
    while True:
        print(xi)
        x_next = xi - (f_1(xi)/(f_dash(xi)))
        if(abs(x_next - xi) < epsilon):
            return xi
        xi = x_next

epsilon = pow( 10, -5)
newton_raphson_method( -4)