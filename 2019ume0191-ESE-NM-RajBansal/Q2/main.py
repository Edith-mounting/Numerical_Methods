def f_1(x):
    return (((1 + (0.2*x*x))**3)*0.5787)/x - 2

def f_dash(x):
    return (3*0.5787*((1 + (0.2*x*x))**2)*0.4*x) - 2

def newton_raphson_method( xi, f_1, f_dash):
    while True:
        x_next = xi - (f_1(xi)/(f_dash(xi)))
        if(abs(x_next - xi) < pow(10, -5)):
            return xi
        print(xi)
        xi = x_next

print( newton_raphson_method( 0.25, f_1, f_dash))
