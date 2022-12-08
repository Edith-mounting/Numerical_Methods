from gauss_elimination_with_partial_pivoting import gauss_elimination_with_partial_pivoting

def BVPQ2(T1, TL, beta, T_infinity, h_infinity, L, k, intervals):
    n = intervals + 1
    h = (L/intervals)
    mat = [[0 for i in range(0, n)] for j in range(0, n)]
    b = [0 for i in range(0, n)]
    mat[0][0] = -1*(2 + (beta*beta*h*h))
    mat[0][1] = 1
    b[0] = (-1*T_infinity*beta*beta*h*h) - T1
    for i in range( 1, n - 1):
        mat[i][i-1] = 1
        mat[i][i] = -1*(2 + (beta*beta*h*h))
        mat[i][i + 1] = 1
        b[i] = (-1*T_infinity*beta*beta*h*h)
    mat[n - 1][n - 1] = -1*(2 + (beta*beta*h*h))
    mat[n - 1][n - 2] = 1
    b[n-1] = (-1*T_infinity*beta*beta*h*h) - TL
    print(mat)
    print(b)
    tempDistribution = gauss_elimination_with_partial_pivoting( mat, n, b)
    print( tempDistribution)

BVPQ2( 120, 30, 256, 20, 64, 0.25, 50, 10)
# BVPQ2( 120, 30, 256, 20, 64, 0.25, 50, 100)
    

