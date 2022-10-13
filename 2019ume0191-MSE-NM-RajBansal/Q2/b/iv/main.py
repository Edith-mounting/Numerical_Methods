from gauss_elimination_with_partial_pivoting import gauss_elimination_with_partial_pivoting
def output_function( a, b, x):
    return (a/x) + b*x*x
def regressionUtil( xi, yi, x, number_of_points):
    matrix_size = 2
    a = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    b = [0 for i in range(matrix_size)]
    val = 0
    #Filling matrix a
    for i in range( 0, n):
        if (xi[i]==0):
            continue
        a[0][0] += 1/(xi[i]**2)
        a[0][1] += xi[i]
        a[1][0] += xi[i]
        a[1][1] += (xi[i]**4)
        b[0] += yi[i]/xi[i]
        b[1] += yi[i]*xi[i]*xi[i]
    # print(a)
    # print(b)
    result = gauss_elimination_with_partial_pivoting( a, matrix_size, b)
    # print(result)
    return output_function( result[0], result[1], x)

xi = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
yi = [7.18, 4.26, 2.22, 0.92, 0.21, 0, 0.19, 0.70, 1.49, 2.49, 3.68]
n = 11
x1 = 0.1
x2 = 1.1
x3 = 1.9
print("y1 =", regressionUtil( xi, yi, x1, n))
print("y2 =", regressionUtil( xi, yi, x2, n))
print("y3 =", regressionUtil( xi, yi, x3, n))