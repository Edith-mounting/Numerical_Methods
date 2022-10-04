#give the starting conditions and calculating function as input to the function
def bisection_method(x1, x2, f_1):
    while(True):
        xr = (x1 + x2)/2
        f_xr = f_1(xr)
        if(abs(f_xr) < pow( 10, -5)):
            return xr
        if(f_xr < 0):
            x1 = xr 
        else:
            x2 = xr
