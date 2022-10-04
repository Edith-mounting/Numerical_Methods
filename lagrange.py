def langrangeUtil(xi, yi, n, x):
    y = 0
    for i in range( 0, n):
        temp = yi[i]
        for j in range( 0, n):
            if(i == j):
                continue
            temp = temp*(x - xi[j])/(xi[i] - xi[j])
        y += temp
    return y

def langrange( temp, cp, n, t, order_of_interpolation):
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
    print(langrangeUtil( x, y, order_of_interpolation + 1, t))
# xi = [ 1, 4, 6, 5]
# yi = []
# for i in range(4):
#     yi.append(math.log(xi[i]))
# n = 4
# x = 2
# print(langrangeUtil(xi, yi, n, x))