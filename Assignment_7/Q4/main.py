def dx_dt( x, y, t):
    return y

def dy_dt( x, y, t):
    return -x + t

def euler( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while( abs(t_current-tf) >= h):
        slope_x = dx_dt(x_current, y_current, t_current)
        slope_y = dy_dt(x_current, y_current, t_current)
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
    print(x_current, " ", y_current, " ", t_current)

def heun( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while(abs(t_current-tf) >= h):
        x_tmp = x_current + dx_dt( x_current, y_current, t_current)*h
        y_tmp = y_current + dy_dt( x_current, y_current, t_current)*h
        slope_x = (dx_dt( x_tmp, y_tmp, t_current + h) + dx_dt(x_current, y_current, t_current))/2
        slope_y = (dy_dt( x_tmp, y_tmp, t_current + h) + dy_dt(x_current, y_current, t_current))/2
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
    print(x_current, " ", y_current, " ", t_current)

def midpoint( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while( abs(t_current-tf) >= h):
        x_i_by_2 = x_current + (dx_dt( x_current, y_current, t_current)*h)/2
        y_i_by_2 = y_current + (dy_dt( x_current, y_current, t_current)*h)/2
        t_mid = t_current + h/2
        slope_x = dx_dt( x_i_by_2, y_i_by_2, t_mid)
        slope_y = dy_dt( x_i_by_2, y_i_by_2, t_mid)
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
    print(x_current, " ", y_current, " ", t_current)

def ralston( ti, tf, h, xi, yi, dx_dt, dy_dt):
    x_current = xi
    y_current = yi
    t_current = ti
    while( abs(t_current-tf) >= h):
        x_new = x_current + 0.75*h*dx_dt( x_current, y_current, t_current)
        y_new = y_current + 0.75*h*dy_dt( x_current, y_current, t_current)
        t_new = t_current + 0.75*h
        slope_x = (dx_dt(x_current, y_current, t_current) + 2*dx_dt(x_new, y_new, t_new))/3
        slope_y = (dy_dt(x_current, y_current, t_current) + 2*dy_dt(x_new, y_new, t_new))/3
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
        # print(t_current)
    print(x_current, " ", y_current, " ", t_current)

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

def dx_dt1(x, y, t):
    return 0
def dy_dt1(x, y, t):
    return -(y*y/t*t)
# print("Results for Q4 for h = 0.1")
# euler( 0, 10, 0.1, 0, 0, dx_dt, dy_dt)
# heun( 0, 10, 0.1, 0, 0, dx_dt, dy_dt)
# midpoint( 0, 10, 0.1, 0, 0, dx_dt, dy_dt)
# ralston( 0, 10, 0.1, 0, 0, dx_dt, dy_dt)
# RK4( 0, 10, 0.1, 0, 0, dx_dt, dy_dt)
# print("Results for Q4 for h = 1")
# euler( 0, 10, 1, 0, 0, dx_dt, dy_dt)
# heun( 0, 10, 1, 0, 0, dx_dt, dy_dt)
# midpoint( 0, 10, 1, 0, 0, dx_dt, dy_dt)
# ralston( 0, 10, 1, 0, 0, dx_dt, dy_dt)
# RK4( 0, 10, 1, 0, 0, dx_dt, dy_dt)
RK4( 1, 10, 2, 0, 1, dx_dt1, dy_dt1)
RK4( 1, 10, 1, 0, 1, dx_dt1, dy_dt1)
RK4( 1, 10, 0.5, 0, 1, dx_dt1, dy_dt1)
RK4( 1, 10, 0.25, 0, 1, dx_dt1, dy_dt1)