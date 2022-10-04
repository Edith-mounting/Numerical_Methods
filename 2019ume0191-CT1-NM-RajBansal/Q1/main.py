
def f_1(x):
    return x*x + x -1
def bisection_method(x1, x2, f_1):
    while(True):
        xr = (x1 + x2)/2
        f_xr = f_1(xr)
        if(abs(f_xr) < epsilon):
            return xr
        print(xr)
        if(f_xr < 0):
            x1 = xr 
        else:
            x2 = xr
    
x1 = 0
x2 = 1
epsilon = pow( 10, -5)
bisection_method( 0, 1, f_1)