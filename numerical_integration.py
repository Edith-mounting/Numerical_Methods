def trapezoidal_rule( x, y, n):
    h = x[1] - x[0]
    res = y[0] + y[n-1]
    for i in range( 1, n - 1):
        res += 2*y[i]
    res = (res*h)/2
    return res

def simpson_s_one_third_rule( x, y, n):
    h = x[1] - x[0]
    m = n - 1 #no of intervals
    rem = m%2
    res = 0
    for i in range( 0, n - 2, 2):
        res += ( y[i + 2] + 4*y[i + 1] + y[i])/3
    if(rem%2 == 1):
        res += (y[n-2] + y[n-1])/2
    res = res*h
    return res

def simpson_s_three_eight_rule( x, y, n):
    res = 0
    m = n - 1 #no of intervals
    h = x[1] - x[0]
    for i in range( 0, n - 3, 3):
        res += (3*(y[i] + 3*y[i + 1] + 3*y[i + 2] + y[i + 3]))/8
    rem = m%3
    if(rem == 2):
        res += ( y[n - 3] + 4*y[n - 2] + y[n - 1])/3
    elif(rem == 1):
        res += (y[n-2] + y[n-1])/2
    res = res*h
    return res