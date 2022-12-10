# #Give matrix a, size n and matrix b as input to the function
# def gauss_elimination_with_partial_pivoting(a, n, b):
#     for k in range(0, n):
#         max_row = k
#         for i in range(k + 1, n):
#             if(abs(a[i][k]) > abs(a[max_row][k])):
#                 max_row = i
#         a[k],a[max_row] = a[max_row],a[k]
#         b[k],b[max_row] = b[max_row],b[k]
#         for i in range(k + 1, n):
#             factor = a[i][k]/a[k][k]
#             for j in range(k, n):
#                 a[i][j] = a[i][j] - factor*a[k][j]
#             b[i] = b[i] - factor*b[k]
    
#     x = [0 for i in range(0, n)]
#     x[n-1] = b[n-1]/a[n-1][n-1]
#     for i in range( n - 2, -1, -1):
#         sum = b[i]
#         for j in range(i + 1, n):
#             sum = sum - a[i][j]*x[j]
#         x[i] = sum/a[i][i]
#     return x
#     # for i in range( 0, n):
#     #     print(x[i])

# def BVP(intervals):
#     n = intervals
#     mat = [[0 for i in range(0, n - 1)] for j in range(0, n - 1)]
#     b = [0 for i in range(0, n - 1)]
#     x = (2/n)
#     for i in range(0,n-1):
#         mat[i][i] = -1*((2*n) - 48*)