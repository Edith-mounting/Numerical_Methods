
def midpoint( xi, xf, dx, yi, f_x):
    while(xi < xf):
        y_i_by_2 = yi + (f_x( xi, yi)*dx)/2
        yi = yi + f_x( xi + dx/2, y_i_by_2)*dx
        xi = xi + dx
    return yi

# print(midpoint( 0, 10, 1, 0, f_x))