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
    print(i)
    y = (k[i]/6)*(((x-xi[i+1])**3/(xi[i]-xi[i+1])) - (x-xi[i+1])*(xi[i]-xi[i+1]))
    y = y - (k[i + 1]/6)*((x - xi[i])**3/(xi[i]-xi[i+1])-(x-xi[i])*(xi[i]-xi[i+1]))
    y += (yi[i]*(x-xi[i+1]) - yi[i+1]*(x - xi[i]))/(xi[i]-xi[i+1])
    return y

xi = [ 4, 5, 10, 16, 17, 28, 48, 63, 64, 65]
yi = [84, 35, 64, 60, 83, 62, 83, 93, 70, 93]  
n = 10
x = 60 
print(cubicSpline( xi, yi, n, x)) 
    