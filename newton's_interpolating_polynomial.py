# points will be an 2-D array of size n, containing (x, f(x)) for n points
# by using these n points you have to find the value of f(x) on given point
# n>=2, n = 2 means linear interpolation
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

def newton_interpolation( temp, cp, n, t, order_of_interpolation):
    close_values = []
    for i in range( 0, n):
        close_values.append(((abs(temp[i] - t)), i))
    close_values.sort()
    x = []
    y = []
    for i in range(0, order_of_interpolation + 1):
        x.append( temp[close_values[i][1]])
        y.append( cp[close_values[i][1]])
    # print(x)
    # print(y)
    print(newton_interpolation_util( x, y, order_of_interpolation + 1, t))
# xi = [ 1, 4, 6, 5]
# yi = []
# for i in range(4):
#     yi.append(math.log(xi[i]))
# n = 4
# x = 2
# print(interpolation(xi, yi, n, x))
