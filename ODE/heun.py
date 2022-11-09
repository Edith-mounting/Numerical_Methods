def f_x(x, y):
    return 4*x*x*x + 3*x*x + 2*x + 1

def heun( xi, xf, dx, yi):
    while(xi < xf):
        yi_0 = yi + f_x( xi, yi)*dx
        yi_dash = f_x( xi + dx, yi_0)
        y_dash = (f_x( xi, yi) + yi_dash)/2
        yi = yi + y_dash*dx
        xi = xi + dx
    return yi

print(heun( 0, 10, 1, 0))