#Give matrix a, size n and matrix b as input to the function
def gauss_elimination(a, n, b):
    for k in range(0, n):
        for i in range(k + 1, n):
            factor = a[i][k]/a[k][k]
            for j in range(k, n):
                a[i][j] = a[i][j] - factor*a[k][j]
            b[i] = b[i] - factor*b[k]
    
    x = [ 0, 0, 0, 0, 0]
    x[n-1] = b[n-1]/a[n-1][n-1]
    for i in range( n - 2, -1, -1):
        sum = b[i]
        for j in range(i + 1, n):
            sum = sum - a[i][j]*x[j]
        x[i] = sum/a[i][i]
    for i in range( 0, n):
        print(x[i])