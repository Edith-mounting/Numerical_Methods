from gauss_elimination_with_partial_pivoting import gauss_elimination_with_partial_pivoting
def output( x, n, xi):
    ans = 0
    val = 1
    for i in range( 0, n):
        ans += val*x[i]
        val = val*xi
    return ans
def regressionUtil( xi, yi, order_of_polynomial, x, number_of_points):
    order_of_polynomial += 1
    a = [[0 for i in range(order_of_polynomial)] for j in range(order_of_polynomial)]
    b = [0 for i in range(order_of_polynomial)]
    val = 0
    for i in range( 0, order_of_polynomial):
        tmp = val
        for j in range( 0, order_of_polynomial):
            for k in range( 0, number_of_points):
                a[i][j] += pow( xi[k], tmp)
            tmp += 1
        for k in range(0, number_of_points):
            b[i] += (yi[k]*pow( xi[k], val))
        val+=1
    # print(a)
    # print(b)
    result = gauss_elimination_with_partial_pivoting( a, order_of_polynomial, b)
    # print(result)
    return output( result, order_of_polynomial, x)
# n = 14
# temp = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000]
# cp = [1.003, 1.005, 1.008, 1.013, 1.020, 1.029,
# 1.040, 1.051, 1.063, 1.075, 1.087, 1.099, 1.121, 1.142]

# print(regressionUtil( temp, cp, 3, 273, n))
# print(regressionUtil( temp, cp, 3, 525, n))
# print(regressionUtil( temp, cp, 3, 850, n))
# print(regressionUtil( temp, cp, 3, 950, n))
# print(regressionUtil( temp, cp, 1, 525, n))