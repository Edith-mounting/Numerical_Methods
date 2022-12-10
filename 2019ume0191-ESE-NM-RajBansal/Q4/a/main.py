def dz_dt( z_current, y_current, t_current):
    return (y_current - z_current)

def dy_dt( z_current, y_current, t_current):
    return (z_current - y_current)

def RK4( ti, tf, h, zi, yi, dx_dt, dy_dt):
    x_current = zi
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
    print("h = ", h, ", z = ", x_current, ", y = ", y_current)
    return x_current, y_current
print("Trying different values of h as follows: ")
h_initial = 0.05
z, y = RK4( 0, 1, h_initial, 0, 40, dz_dt, dy_dt)
while(True):
    h_new = h_initial/2
    z1, y1 = RK4( 0, 1, h_new, 0, 40, dz_dt, dy_dt)
    if(abs(z - z1)<pow(10, -2) and abs(y - y1)<pow(10, -2)):
        break
    z = z1
    y = y1
    h_initial = h_new
print("So Now we can see there is not much in the values of y and z so let's consider h = 0.0015625 as")
