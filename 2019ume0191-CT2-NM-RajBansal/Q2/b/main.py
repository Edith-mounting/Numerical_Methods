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

x = [1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,
 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]

y = [ 1.87, 2.87, 4.47, 6.62, 9.3, 12.5, 16.22, 20.44, 25.17, 30.41,
 36.15, 42.38, 49.13, 56.37, 64.11, 72.36, 81.10, 90.35, 100.09]

n = 19
print("Using simpson's 1/3 rule")
print( simpson_s_one_third_rule( x, y, n))