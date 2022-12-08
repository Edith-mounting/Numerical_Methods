import math

def f(x):
    return math.log(1 + x)/(1 + x*x) 

def gaussQuad1( a, b):
    e = 0
    w = 2
    return (b-a)*w*f(((b+a)/2) + ((e*(b-a))/2))/2

def gaussQuad2( a, b):
    e = math.sqrt(1/3)
    w = 1
    return ((b-a)*w*f((b+a)/2 + (e*(b-a))/2))/2 + ((b-a)*w*f((b+a)/2 + (-e*(b-a))/2))/2

def gaussQuad3( a, b):
    e1 = 0
    e2 = math.sqrt(3/5)
    w1 = 8/9
    w2 = 5/9
    return ((b-a)*w2*f((b+a)/2 + (e2*(b-a))/2))/2 + ((b-a)*w2*f((b+a)/2 + (-e2*(b-a))/2))/2 + ((b-a)*w1*f((b+a)/2 + (e1*(b-a))/2))/2

def gaussQuad4( a, b):
    e1 = math.sqrt(3/7 - (2*math.sqrt(6/5))/7)
    e2 = math.sqrt(3/7 + (2*math.sqrt(6/5))/7)
    w1 = (18 + math.sqrt(30))/36
    w2 = (18 - math.sqrt(30))/36
    return ((b-a)*w2*f((b+a)/2 + (e2*(b-a))/2))/2 + ((b-a)*w2*f((b+a)/2 + (-e2*(b-a))/2))/2 + ((b-a)*w1*f((b+a)/2 + (e1*(b-a))/2))/2 + ((b-a)*w1*f((b+a)/2 + (-e1*(b-a))/2))/2

a = 0
b = 1
ans = 0
iter = 5
i = 0
while(i < iter):
    ans += (gaussQuad3( a, a + 0.2))
    a = a + 0.2
    i+=1
print(ans)
