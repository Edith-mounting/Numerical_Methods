
def ralston( xi, xf, dx, yi, f_x):
    while( xi < xf):
        k1 = f_x( xi, yi)
        k2 = f_x( xi + (3*dx)/4, yi + (3*dx*k1)/4)
        yi = yi + (k1/3 + (2*k2)/3)*dx
        xi = xi + dx
    return yi

# print( ralston( 0, 10, 1, 0, f_x))
# print( ralston( 0, 10, 10, 0, f_x))