from newton_raphson_coupled_equation import coupled_linear_equ

def f_Q1_dash( a):
    x = a[0]
    y = a[1]
    z = a[2]
    return [[ 1, 1, 1],
    [ y + z, x + z, x + y], 
    [y*y + 2*x*z - y*z, z*z + 2*x*y - x*z, x*x + 2*y*z - x*y]]

def f_Q1_cal( a):
    x = a[0]
    y = a[1]
    z = a[2]
    return [ -1*(x+y+z-3), -1*( x*y + y*z + z*x - 3),
    -1*( x*y*y + y*z*z + z*x*x - x*y*z -2)]

def f_Q2_dash( a):
    x = a[0]
    y = a[1]
    z = a[2]
    return [[3*x*x - 3*y*z, 3*y*y - 3*x*z, 3*z*z - 3*x*y],
    [2*x*(y - z) - y*y + z*z, 2*y*(z - x) - z*z + x*x, 2*z*(x - y) - x*x + y*y],
    [3*y*z - z*z - 2*x*y, 3*x*z - 2*y*z - x*x, 3*x*y - y*y - 2*x*z]]

def f_Q2_cal( a):
    x = a[0]
    y = a[1]
    z = a[2]
    return [-1*(x*x*x + y*y*y + z*z*z - 3*(x*y*z + 6)),
        -1*(x*x*(y-z) + y*y*(z-x) + z*z*(x-y) + 2),
    -1*((x-y)*y*z + (y-z)*z*x + (z-x)*x*y + 5)]

#Don't forget to include -1 while calculating function using values
# file = open("input.txt",'r')
# x_initial = file.read()

# x_initial = [ 0, 2, 3]
# n = 3
# x_final = coupled_linear_equ( x_initial, n, f_Q1_cal, f_Q1_dash)
# y_final = f_Q1_cal(x_final)
# for i in range( 0, n):
#     print( y_final[i])

# x_initial = [ 0, 1, 2]
# n = 3
# x_final = coupled_linear_equ( x_initial, n, f_Q2_cal, f_Q2_dash)
# y_final = f_Q2_cal(x_final)
# for i in range( 0, n):
#     print( y_final[i])

def f_Q_cal( a):
    x = a[0]
    y = a[1]
    z = a[2]
    p = a[3]
    return [(-1)*(x*y*(y-z) + y*z*(z - x) + z*x*(x - y) - 10),
        (-1)*(x*y*z*(x + y + z - 4) - 120),
        (-1)*((x-y)**2*z + (y-z)**2*x + (z - x)**2*y - 2*(x + y + z)),
        (-1)*(x*y*z - x - y - z - p)]

# def f_Q_dash( a):
#     x = a[0]
#     y = a[1]
#     z = a[2]
#     p = a[3]
#     return [[y*(y - z) ]]
# x_initial = [ 5, 6, 7, 10]
# n = 4
# x_final = coupled_linear_equ( x_initial, n)