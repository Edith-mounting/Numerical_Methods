from gauss_elimination_with_partial_pivoting import gauss_elimination_with_partial_pivoting

def previousYearQuestion(intervals, h_infinity, t_infinity, b, k, q):
    h = b/intervals
    n = intervals + 1
    mat = [[0 for i in range(0, n)] for j in range(0, n)]
    b = [0 for i in range(0, n)]
    mat[0][0] = -1
    mat[0][1] = 1
    b[0] = 0
    mat[n-1][n - 2] = 1
    mat[n-1][n-1] = -1*(1 + (h*h_infinity))
    print(h)
    b[n-1] = -1*(h*h_infinity*t_infinity)/k
    for i in range( 1, n - 1):
        mat[i][i] = -2
        mat[i][i-1] = 1
        mat[i][i+1] = 1
        b[i] = -1*(q*h*h)/k
        # print(b[i])
    print(mat)
    print(b)
    temp = gauss_elimination_with_partial_pivoting( mat, n, b)
    print(temp)

previousYearQuestion(5, 100.0, 10.0, 0.01, 1.0, 400000.0)
# previousYearQuestion(10, 100, 10, 0.1, 1, 400000)
# previousYearQuestion(20, 100, 10, 0.1, 1, 400000)
# previousYearQuestion(30, 100, 10, 0.1, 1, 400000)