def f_x(x, y):
    return 4*x*x*x + 3*x*x + 2*x + 1

def midpoint( xi, xf, dx, yi):
    while(xi < xf):
        y_i_by_2 = yi + (f_x( xi, yi)*dx)/2
        yi = yi + f_x( xi + dx/2, y_i_by_2)*dx
        xi = xi + dx
    return yi

print(midpoint( 0, 10, 1, 0))