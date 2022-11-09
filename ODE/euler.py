def f_x(x, y):
    return 4*x*x*x + 3*x*x + 2*x + 1

def euler( xi, xf, dx, yi):
    while(xi < xf):
        yi = yi + (f_x(xi, yi)*dx)
        xi = xi + dx
    return yi

print(euler( 0, 10, 1, 0))
print(euler( 0, 10, 10, 0))