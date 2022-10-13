def newton_interpolation_util( xi, yi, n, x):
    f = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        f[i][i] = yi[i]
    l = 1
    while(l<n):
        i = 0
        while(i<n):
            if(i+l >= n):
                break
            f[i+l][i] = (f[i+l][i+1] - f[i+l-1][i])/(xi[i+l] - xi[i])
            i+=1
        l+=1
    
    y = f[0][0]
    x_terms = 1
    for i in range(1, n):
        x_terms = x_terms*(x - xi[i-1])
        y += x_terms*f[i][0]
    return y

def newton_interpolation( xi, yi, n, x_given, order_of_polynomial):
    close_values = []
    for i in range( 0, n):
        close_values.append(((abs(xi[i] - x_given)), i))
    close_values.sort()
    x = []
    y = []
    for i in range(0, order_of_polynomial + 1):
        x.append( xi[close_values[i][1]])
        y.append( yi[close_values[i][1]])
    # print(x)
    # print(y)
    return newton_interpolation_util( x, y, order_of_polynomial + 1, x_given)

xi = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
yi = [7.18, 4.26, 2.22, 0.92, 0.21, 0, 0.19, 0.70, 1.49, 2.49, 3.68]
order_of_polynomial = 2
n = 11
x1 = 0.1
x2 = 1.1
x3 = 1.9
print("y1 =", newton_interpolation( xi, yi, n, x1, order_of_polynomial))
print("y2 =", newton_interpolation( xi, yi, n, x2, order_of_polynomial))
print("y3 =", newton_interpolation( xi, yi, n, x3, order_of_polynomial))