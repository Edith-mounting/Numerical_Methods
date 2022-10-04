import math
def Q1_a(y):
    x = y
    y = (3-x)/2
    print(x , y)
    if(abs(x - y) < 10**-5):
        return 
    Q1_a(y)

def Q1_b(y):
    x = 3 - 2*y
    y = x
    print(x, y)
    Q1_b(y)

def Q2_a(x):
    x = 4/x
    Q2_a(x)

def Q3_a(x):
    x = 1/math.sin(x)
    print(x)
    Q3_a(x)

def Q3_b(x):
    x = 1/math.tan(x)
    print(x)
    Q3_b(x)

def checkFloatingForMachine(x):
    while 1 + x > 1:
        x = x/2
        print(x)

def Q5_a(x):
    fact = 1
    res = 1
    i = 1
    y = x
    while(abs(y/fact) > pow( 10, -5)):
        print(res)
        res += (y/fact)
        i+=1
        y = y*x
        fact = fact*i

def divisibleByP(x, p):
    sum = 0
    while(x>0):
        sum += x%10
        x=x//10

    if(sum%p==0):
        return True
    return False
def Q7_a( m, p):
    i = pow( 10, m)
    count = 0
    a = []
    while(i < pow(10, m + 1)):
        if(divisibleByP( i, p)):
            a.append(i)
            count+=1
        i+=1
    print(count)
    n = len(a)
    y1 = 0
    y2 = 0
    y3 = 0
    for i in range(0, n):
        for j in range(0, n):
            y1 += a[i]*a[j]
            if(i!=j):
                y2 += a[i]*a[j]
            if(i < j):
                y3 += a[i]*a[j]
    print(y1, y2, y3)
# y = 0
# checkFloatingForMachine(1)
# Q1_a(y)
# Q1_b(y)
# Q2_a(1)
# Q5_a(1)
# print(math.exp(1))
# Q5_a(-1)
# Q5_a(10)
# Q3_a(0.5)
# Q3_b(0.5)
Q7_a( 3, 13)


