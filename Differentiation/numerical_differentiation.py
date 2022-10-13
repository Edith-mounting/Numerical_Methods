#Assignment 6
def f_x(x):
    return x**4 - x**3 + x**2 - x + 1

def Q3_second( x, h):
    return (f_x( x + h) - f_x(x))/h

def Q3_third( x, h):
    return (-3*f_x(x) + 4*f_x(x + h) - f_x(x + 2*h))/(2*h)

def Q3_fourth( x, h):
    return (3*f_x(x + h) - (11*f_x(x))/6 - (3*f_x( x + 2*h))/2 + (f_x( x + 3*h))/3 )/(h)

print(Q3_second( 5, 0.5))
print(Q3_second( 5, 0.1))
print(Q3_third( 5, 0.5))
print(Q3_third( 5, 0.1))
print(Q3_fourth( 5, 0.5))
print(Q3_fourth( 5, 0.1))