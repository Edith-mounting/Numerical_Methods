import math
def f_x( x, F):
    n = 1
    tmp = ((-1)**(n - 1)/(2*n - 1))*math.cos((math.pi*(2*n - 1)*x)/2)*math.exp( (-1*math.pi*math.pi*(2*n-1)*(2*n-1)*F)/4)
    while True:
        n+=1
        val = ((-1)**(n - 1)/(2*n - 1))*math.cos((math.pi*(2*n - 1)*x)/2)*math.exp( (-1*math.pi*math.pi*(2*n-1)*(2*n-1)*F)/4)
        # print(val)
        if(abs(val) < pow( 10, -7)):
            print(n)
            break
        tmp = tmp + val
    tmp = (tmp*4)/math.pi
    return (1 - tmp)

def calculate(h, F, x):
    current_x = 0
    x_values = []
    y_values = []
    while(current_x - x < pow( 10,-5)):
        y = f_x( current_x, F)
        # print(y)
        x_values.append(current_x)
        y_values.append(y)
        current_x = current_x + h
    # print("x4 = ")
    # print(x_values)
    # print("y4 = ")
    # print(y_values)
print("maximum values of n for each interval for F = 0.1")
calculate( 0.1, 0.1, 1)
print("maximum values of n for each interval for F = 1")
calculate( 0.1, 1, 1)
print("maximum values of n for each interval for F = 10")
calculate( 0.1, 10, 1)
print("maximum values of n for each interval for F = 100")
calculate( 0.1, 100, 1)


