
def euler( xi, xf, dx, yi, f_x):
    while(xi < xf):
        yi = yi + (f_x(xi, yi)*dx)
        xi = xi + dx
    return yi

# print(euler( 0, 10, 1, 0, f_x))
# print(euler( 0, 10, 10, 0, f_x))