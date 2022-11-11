def dy_dx( x, y):
    return -(y*y/x*x)

def euler( xi, xf, h, yi):
    while(abs( xi - xf) >= h):
        yi = yi + (dy_dx(xi, yi)*h)
        xi = xi + h
    return yi

print("Using euler's method")
print("For h = 2, the value of y = ",euler( 1, 10, 2, 1))
print("For h = 1, the value of y = ", euler( 1, 10, 1, 1))
print("For h = 0.5, the value of y = ", euler( 1, 10, 0.5, 1))
print("For h = 0.25, the value of y = ", euler( 1, 10, 0.25, 1))