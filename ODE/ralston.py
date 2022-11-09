def f_x(x, y):
    return 4*x*x*x + 3*x*x + 2*x + 1

def ralston( xi, xf, dx, yi):
    while( xi < xf):
        k1 = f_x( xi, yi)
        k2 = f_x( xi + (3*dx)/4, yi + (3*dx*k1)/4)
        yi = yi + (k1/3 + (2*k2)/3)*dx
        xi = xi + dx
    return yi

print( ralston( 0, 10, 1, 0))
print( ralston( 0, 10, 10, 0))