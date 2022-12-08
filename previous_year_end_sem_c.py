# x -> z
# t -> x
def dx_dt( x, y, t):
    return ( 4*t - 3*x -2*y)

def dy_dt( x, y, t):
    return (x)

def RK4( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while( abs(t_current-tf) >= h):
        x_k1 = dx_dt( x_current, y_current, t_current)
        y_k1 = dy_dt( x_current, y_current, t_current)

        x_k2 = dx_dt( x_current + (x_k1*h)/2, y_current + (y_k1*h)/2, t_current + h/2)
        y_k2 = dy_dt( x_current + (x_k1*h)/2, y_current + (y_k1*h)/2, t_current + h/2)
        
        x_k3 = dx_dt( x_current + (x_k2*h)/2, y_current + (y_k2*h)/2, t_current + h/2)
        y_k3 = dy_dt( x_current + (x_k2*h)/2, y_current + (y_k2*h)/2, t_current + h/2)
        
        x_k4 = dx_dt( x_current + (x_k3*h), y_current + (y_k3*h), t_current + h)
        y_k4 = dy_dt( x_current + (x_k3*h), y_current + (y_k3*h), t_current + h)
        
        slope_x = (x_k1 + 2*x_k2 + 2*x_k3 + x_k4)/6
        slope_y = (y_k1 + 2*y_k2 + 2*y_k3 + y_k4)/6
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
        print(x_current, " ", y_current, " ", t_current)

RK4( 0, 10, 0.3, -2, 0, dx_dt, dy_dt)