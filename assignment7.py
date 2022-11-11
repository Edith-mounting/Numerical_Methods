
def Q_1_f_x(x, y):
    return 4*x*x*x + 3*x*x + 2*x + 1

def Q_2_a_f_x(x, y):
    g = 9.81
    c = 12.5
    m = 68.1
    return (g - (c*y)/m)

def Q_2_b_f_x(x, y):
    g = 9.81
    c = 12.5
    m = 68.1
    a = 8.3
    b = 2.2
    vmax = 46
    return (g - ((c/m)*(y + a*pow(y/vmax, b))))

def Q3_f_x_1( t, x):
    return -0.5*x

def Q3_f_x_2( t, x, y):
    return 4 - 0.1*x - 0.3*y

def Q3_euler( ti, tf, h, xi, yi):
    while(ti < tf):
        x_i_1 = xi + (Q3_f_x_1( ti, xi)*h)
        y_i_1 = yi + (Q3_f_x_2( ti, xi, yi)*h)
        ti = ti + h
        xi = x_i_1
        yi = y_i_1
    print(xi, " ", yi)

def Q3_heun(ti, tf, h, xi, yi):
    while( ti < tf):
        yi_0 = yi + Q3_f_x_2( ti, xi, yi)*h
        yi_dash = Q3_f_x_2( ti + h, xi, yi_0)
        y_dash = ( Q3_f_x_2( ti, xi, yi) + yi_dash)/2
        yi = yi + y_dash*h
        xi_0 = xi + Q3_f_x_1( ti, xi)*h
        xi_dash = Q3_f_x_1( ti + h, xi_0)
        x_dash = (xi_dash + Q3_f_x_1( ti, xi))/2
        xi = xi + x_dash*h
        ti = ti + h
    print( xi, " ", yi)


# Q3_euler( 0, 2, 0.5, 4, 6)
# Q3_euler( 0, 2, 0.5, 4, 6)
# print(euler( 0, 10, 1, 0, Q_1_f_x))
# print(euler( 0, 10, 10, 0, Q_1_f_x))

# print( euler( 0, 15, 0.1, 0, Q_2_a_f_x))
# print( RK4( 0, 15, 0.1, 0, Q_2_a_f_x))

# print( euler( 0, 15, 0.1, 0, Q_2_b_f_x))
# print( RK4( 0, 15, 0.1, 0, Q_2_b_f_x))