def dy_dx( x, y):
    return ((-1*y*y)/(x*x))

def RK4( xi, xf, h, yi):
    while( abs( xi - xf) >= h):
        k1 = dy_dx( xi, yi)
        k2 = dy_dx( xi + h/2, yi + (k1*h)/2)
        k3 = dy_dx( xi + h/2, yi + (k2*h)/2)
        k4 = dy_dx( xi + h, yi + k3*h)
        yi = yi + ((k1 + 2*k2 + 2*k3 + k4)*h)/6
        xi = xi + h
    return yi
print("Using RK4 method")
print( "For h = 2, the value of y = ",RK4( 1, 10, 2, 1))
print("For h = 1, the value of y = ", RK4( 1, 10, 1, 1))
print("For h = 0.5, the value of y = ", RK4( 1, 10, 0.5, 1))
print( "For h = 0.25, the value of y = ",RK4( 1, 10, 0.25, 1))