from numerical_integration import trapezoidal_rule, simpson_s_one_third_rule, simpson_s_three_eight_rule
n = 11
y = [-1, 2, 23, 86, 215, 434, 767, 1238, 1871, 2690, 3719]
x = []
for i in range( 0, n):
    x.append(i)

print( trapezoidal_rule( x, y, n))
print( simpson_s_one_third_rule( x, y, n))
print( simpson_s_three_eight_rule( x, y, n))