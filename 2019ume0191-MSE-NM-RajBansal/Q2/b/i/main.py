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

def langrange( xi, yi, n, x_given, order_of_polynomial):
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
    return langrangeUtil( x, y, order_of_polynomial + 1, x_given)

xi = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
yi = [7.18, 4.26, 2.22, 0.92, 0.21, 0, 0.19, 0.70, 1.49, 2.49, 3.68]
order_of_polynomial = 2
n = 11
x1 = 0.1
x2 = 1.1
x3 = 1.9
print("y1 =", langrange( xi, yi, n, x1, order_of_polynomial))
print("y2 =", langrange( xi, yi, n, x2, order_of_polynomial))
print("y3 =", langrange( xi, yi, n, x3, order_of_polynomial))