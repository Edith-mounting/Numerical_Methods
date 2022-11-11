
def RK4( xi, xf, dx, yi, f_x):
    while( xi < xf):
        k1 = f_x( xi, yi)
        k2 = f_x( xi + dx/2, yi + (k1*dx)/2)
        k3 = f_x( xi + dx/2, yi + (k2*dx)/2)
        k4 = f_x( xi + dx, yi + k3*dx)
        yi = yi + ((k1 + 2*k2 + 2*k3 + k4)*dx)/6
        xi = xi + dx
    return yi

# print(RK4( 0, 10, 1, 0, f_x))
# print(RK4( 0, 10, 10, 0, f_x))
