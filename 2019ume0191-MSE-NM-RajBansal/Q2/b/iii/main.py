from gauss_elimination_with_partial_pivoting import gauss_elimination_with_partial_pivoting
def cubicSpline( xi, yi, number_of_points, x):
    n = number_of_points #number of intervals
    sz = n
    a = [[0 for x1 in range(sz)] for y1 in range(sz)]
    b = [0 for x1 in range(sz)]
    for i in range( 1, n - 1):
        a[i][i - 1] = (xi[i - 1] - xi[i])
        a[i][i] = 2*(xi[i - 1] - xi[i + 1])
        a[i][i + 1] = (xi[i] - xi[i + 1])
        b[i] = 6*(((yi[i-1] - yi[i])/(xi[i-1] - xi[i])) - ((yi[i] - yi[i+1])/(xi[i] - xi[i+1])))
    
    sz1 = n - 2
    a1 = [[0 for x1 in range(sz1)] for y1 in range(sz1)]
    b1 = [0 for x1 in range(sz1)]
    for i in range(0, n - 2):
        for j in range( 0, n - 2):
            a1[i][j] = a[i + 1][j + 1]
        b1[i] = b[i+1]
    # print(a1)
    # print(b1)
    k = gauss_elimination_with_partial_pivoting( a1, sz1, b1)
    k.insert( 0, 0)
    k.append(0)
    itr = n - 1
    for i in range( 1, n):
        if(x>=xi[i-1] and x<xi[i]):
            itr = i - 1
            break    
    # print(itr)
    y = 0
    i = itr
    y = (k[i]/6)*(((x-xi[i+1])**3/(xi[i]-xi[i+1])) - (x-xi[i+1])*(xi[i]-xi[i+1]))
    y = y - (k[i + 1]/6)*((x - xi[i])**3/(xi[i]-xi[i+1])-(x-xi[i])*(xi[i]-xi[i+1]))
    y += (yi[i]*(x-xi[i+1]) - yi[i+1]*(x - xi[i]))/(xi[i]-xi[i+1])
    return y

xi = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
yi = [7.18, 4.26, 2.22, 0.92, 0.21, 0, 0.19, 0.70, 1.49, 2.49, 3.68]
n = 11
x1 = 0.1
x2 = 1.1
x3 = 1.9
print("y1 =", cubicSpline( xi, yi, n, x1))
print("y2 =", cubicSpline( xi, yi, n, x2))
print("y3 =", cubicSpline( xi, yi, n, x3))
    