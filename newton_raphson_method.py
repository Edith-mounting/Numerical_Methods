def f_1(x):
    return x**3 - (3*x**2) + 2*x

def f_dash(x):
    return 3*x*x - 6*x + 2

def newton_raphson_method( xi, f_1, f_dash):
    x_next = xi - (f_1(xi)/(f_dash(xi)))
    if(abs(x_next - xi) < pow(10, -5)):
        return xi

print( newton_raphson_method( 0, f_1, f_dash))
