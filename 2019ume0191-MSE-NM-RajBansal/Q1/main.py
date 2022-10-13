import math
from gauss_elimination_with_partial_pivoting import gauss_elimination_with_partial_pivoting

def f_dash( a):
    x = a[0]
    y = a[1]
    p = a[2]
    return [[3*x*x - 3*y, 3*y*y - 3*x, 0],
            [2*x + y - 1, 2*y + x - 1, 0],
            [(x/math.sqrt(x*x + y*y - 1)), (y/math.sqrt( x*x + y*y - 1)), 1]]

def f_cal( a):
    x = a[0]
    y = a[1]
    p = a[2]
    return [-(x**3 + y**3 - 3*x*y -19),
            -(x*x + y*y + x*y -x -y -9),
            -(p - math.sqrt(x*x + y*y -1) -2)]
def coupled_linear_equ(x_initial, n, f_cal, f_dash):
    itr = 1
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
        print("values on iteration",itr,"=",x_initial)
        if(bl==False):
            return x_initial
        itr+=1

x_initial = [ 10, 20, 15]
n = 3
print("Initial guess =", x_initial)
coupled_linear_equ( x_initial, n, f_cal, f_dash)