from gauss_elimination import gauss_elimination
from gauss_elimination_with_partial_pivoting import gauss_elimination_with_partial_pivoting
n = 5
a=[[-2,1,0,0,0],[1,-2,1,0,0],[0,1,-2,1,0],[0,0,1,-2,1],[0,0,0,1,-2]]
b=[-1, 0, 0, 0, -1]
# n = 2
# a=[[1,2],[1.05, 2]]
# b=[10,10.4]
x = gauss_elimination_with_partial_pivoting( a, n, b)
for i in range( 0, n):
    print(x[i])