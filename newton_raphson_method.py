
def newton_raphson_method( xi, f_1, f_dash):
    x_next = xi - (f_1(xi)/(f_dash(xi)))
    if(abs(x_next - xi) < pow(10, -5)):
        return xi