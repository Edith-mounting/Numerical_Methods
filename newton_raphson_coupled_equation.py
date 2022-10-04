from gauss_elimination_with_partial_pivoting import gauss_elimination_with_partial_pivoting

def coupled_linear_equ(x_initial, n, f_cal, f_dash):
    while True:
        a = f_dash( x_initial)
        b = f_cal(x_initial)
        delta_x = gauss_elimination_with_partial_pivoting( a, n, b)
        bl = False
        for i in range( 0, n):
            x_initial[i] += 1*delta_x[i]
        f_values = f_cal( x_initial)
        for i in range( 0, n):
            if(abs(f_values[i]) > pow(10, -5)):
                bl = True
        if(bl==False):
            return x_initial

