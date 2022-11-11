def dx_dt( x, y, t):
    return -0.5*x

def dy_dt( x, y, t):
    return 4 - (0.1*x) - (0.3*y)

def euler( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while( t_current < tf):
        slope_x = dx_dt(x_current, y_current, t_current)
        slope_y = dy_dt(x_current, y_current, t_current)
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
    print( x_current, " ", y_current)

def heun( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while(t_current < tf):
        x_tmp = x_current + dx_dt( x_current, y_current, t_current)*h
        y_tmp = y_current + dy_dt( x_current, y_current, t_current)*h
        slope_x = (dx_dt( x_tmp, y_tmp, ti + h) + dx_dt(x_current, y_current, t_current))/2
        slope_y = (dy_dt( x_tmp, y_tmp, ti + h) + dy_dt(x_current, y_current, t_current))/2
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
    print( x_current, " ", y_current)

def midpoint( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while( t_current < tf):
        x_i_by_2 = x_current + (dx_dt( x_current, y_current, t_current)*h)/2
        y_i_by_2 = y_current + (dy_dt( x_current, y_current, t_current)*h)/2
        t_mid = t_current + h/2
        slope_x = dx_dt( x_i_by_2, y_i_by_2, t_mid)
        slope_y = dy_dt( x_i_by_2, y_i_by_2, t_mid)
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
    print( x_current, " ", y_current)

def ralston( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while( t_current < tf):
        x_new = x_current + 0.75*h*dx_dt( x_current, y_current, t_current)
        y_new = y_current + 0.75*h*dy_dt( x_current, y_current, t_current)
        t_new = t_current + 0.75*h
        slope_x = (dx_dt(x_current, y_current, t_current) + 2*dx_dt(x_new, y_new, t_new))/3
        slope_y = (dy_dt(x_current, y_current, t_current) + 2*dy_dt(x_new, y_new, t_new))/3
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h

    print(x_current, " ", y_current)

def RK4( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while( t_current < tf):
        x_k1 = dx_dt( x_current, y_current, t_current)
        y_k1 = dy_dt( x_current, y_current, t_current)
        x_k2 = dx_dt( x_current + (x_k1*h)/2, y_current + (y_k1*h)/2, t_current + h/2)
        y_k2 = dy_dt( x_current + (x_k1*h)/2, y_current + (y_k1*h)/2, t_current + h/2)
        x_k3 = dx_dt( x_current + (x_k2*h)/2, y_current + (y_k2*h)/2, t_current + h/2)
        y_k3 = dy_dt( x_current + (x_k2*h)/2, y_current + (y_k2*h)/2, t_current + h/2)
        x_k4 = dx_dt( x_current + (x_k3*h)/2, y_current + (y_k3*h)/2, t_current + h/2)
        y_k4 = dy_dt( x_current + (x_k3*h)/2, y_current + (y_k3*h)/2, t_current + h/2)
        slope_x = (x_k1 + 2*x_k2 + 2*x_k3 + x_k4)/6
        slope_y = (y_k1 + 2*y_k2 + 2*y_k3 + y_k4)/6
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
    print(x_current, " ", y_current)

print("Results for Q3")
euler( 0, 2, 0.5, 4, 6, dx_dt, dy_dt)
heun( 0, 2, 0.5, 4, 6, dx_dt, dy_dt)
midpoint( 0, 2, 0.5, 4, 6, dx_dt, dy_dt)
ralston( 0, 2, 0.5, 4, 6, dx_dt, dy_dt)
RK4( 0, 2, 0.5, 4, 6, dx_dt, dy_dt)
