
def heun( xi, xf, dx, yi, f_x):
    while(xi < xf):
        yi_0 = yi + f_x( xi, yi)*dx
        yi_dash = f_x( xi + dx, yi_0)
        y_dash = (f_x( xi, yi) + yi_dash)/2
        yi = yi + y_dash*dx
        xi = xi + dx
    return yi

# print(heun( 0, 10, 1, 0, f_x))