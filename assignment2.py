import math
from re import X

def Q2(a, precision):
    res = 0.00
    for i in range( 0, pow( 10, 5)):
        res += a
    return round( res, precision)

def Q3( a, b, precison):
    res = a + b
    return round( res, precison)

def Q7(x):
    x-=1
    res = 0.00
    i = 0
    curr_x = x
    while(True):
        tmp = 0.00
        if(i%2==0):
            tmp += curr_x/(i + 1)
        else:
            tmp -= curr_x/(i+1)
        if( tmp < pow(10, -5)):
            break
        i+=1
        curr_x = curr_x*x
    return res

def Q8():
    ans = pow( math.pi, 4)/90
    res1 = 0.00
    for i in range(1, 10001):
        res1 += (1/pow(i, 4))
    print(res1)
    error = (abs(res1 - ans)/ans)*100
    print("percentage error in case 1:", error)
    res2 = 0.00
    for i in range(10000, 0, -1):
        res2 += (1/pow(i, 4))
    print(res2)
    error = (abs(res2 - ans)/ans)*100
    print("percentage error in case 2:", error)

def f_dash_x_Q9(x):
    return (4*x*x*x + 12*x*x + 4*x + 2)
def Q9( h):
    x = 0
    res = 1
    while((1 - x) > pow(10, -5)):
        res = res + (h*f_dash_x_Q9(x))
        x += h
    return res

def f_dash_x_Q10(x):
    return (math.pi*math.cos((math.pi*x)/2))/2

def Q10( h):
    x = 0
    res = 0
    while((1 - x) > pow(10, -5)):
        res = res + (h*f_dash_x_Q10(x))
        x += h
    return res
    
# x = math.sqrt(1)
# print(round(x, 1))
# x = math.sqrt(2)
# print( round( x, 2))
# x = math.sqrt(4)
# print( round( x, 1))
# print( round( x, 2))
# x = math.pi
# print( round( x, 1))
# print( round( x, 2))
# x = math.exp(1)
# print( round( x, 1))
# print( round( x, 2))
x = pow( 10, -5)
# print( Q2(x, 1))
# print( Q2(x, 2))
a = pow( 10, 5)
b = pow( 10, -5)
# print( Q3( a, b, 1))
# print( Q3( a, b, 2))
# print( Q3( b, a, 1))
# print( Q3( b, a, 2))
print(Q7(x))
print(math.log(2))
# Q8()
# print(Q9(1))
# print(Q9(0.1))
# print(Q9(0.01))
# print(Q10(1))
# print(Q10(0.1))
# print(Q10(0.01))
