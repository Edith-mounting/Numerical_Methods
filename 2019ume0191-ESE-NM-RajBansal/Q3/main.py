import math

def f(x):
    return (3*x*x + 2*x - 5)

def gaussQuad3( a, b):
    e1 = 0
    e2 = math.sqrt(3/5)
    w1 = 8/9
    w2 = 5/9
    return (((b-a)*w2*f((b+a)/2 + (e2*(b-a))/2))/2 + ((b-a)*w2*f((b+a)/2 + (-e2*(b-a))/2))/2 + ((b-a)*w1*f((b+a)/2 + (e1*(b-a))/2))/2)

def f_1( a, b):
    ans = 0
    iter = 10
    h = (b - a)/iter
    i = 0
    while(i < iter):
        ans += (gaussQuad3( a, a + h))
        a = a + h
        i+=1
    return (ans - 4)
    
# print(ans)
def regular_falsi_method( a, x1, x2):
    while True:
        f_x1 = f_1( a, x1)
        f_x2 = f_1( a, x2)
        mid = (f_x1 - f_x2)/(x1 - x2)
        xr = x2 - f_x2/mid
        f_xr = f_1( a, xr)
        if(abs(f_xr) < pow( 10, -5)):
            return xr
        if(f_xr < 0):
            x1 = xr
        else:
            x2 = xr
        print(x1, " ", x2)

print("values of x1 and x2 for each iteration are:")
alpha = regular_falsi_method( 1, 1, 2)
print("value of alpha finally : ", alpha)

# a = 1
# b = 1.91
# ans = 0
# iter = 10
# h = (b - a)/iter
# i = 0
# while(i < iter):
#     ans += (gaussQuad3( a, a + h))
#     a = a + h
#     i+=1
# print(ans)
# print(newton_raphson_method(1.5))