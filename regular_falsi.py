#give the starting conditions and calculating function as input to the function
def Regular_Falsi_method( x1, x2, f_1):
    while(True):
        f_x1 = f_1( x1)
        f_x2 = f_1( x2)
        mid = (f_x1 - f_x2)/(x1 - x2)
        xr = x2 - f_x2/mid
        f_xr = f_1( xr)
        if(abs(f_xr) < pow( 10, -5)):
            return xr
        if(f_xr < 0):
            x1 = xr
        else:
            x2 = xr
