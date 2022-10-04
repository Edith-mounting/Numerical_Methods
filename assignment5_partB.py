from cmath import log
import math
from lagrange import langrange
from regression import regressionUtil
n = 14
temp = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000]
cp = [1.003, 1.005, 1.008, 1.013, 1.020, 1.029,
1.040, 1.051, 1.063, 1.075, 1.087, 1.099, 1.121, 1.142]
# cp = [math.log(i) for i in cp]
# langrange( temp, cp, n, 273, 1)
# langrange( temp, cp, n, 273, 2)
# langrange( temp, cp, n, 273, 3)
# langrange( temp, cp, n, 525, 1)
# langrange( temp, cp, n, 525, 2)
# langrange( temp, cp, n, 525, 3)
# langrange( temp, cp, n, 850, 1)
# langrange( temp, cp, n, 850, 2)
# langrange( temp, cp, n, 850, 3)
# langrange( temp, cp, n, 950, 1)
# langrange( temp, cp, n, 950, 2)
# langrange( temp, cp, n, 950, 3)

print(regressionUtil( temp, cp, 1, 525, n))
print(regressionUtil( temp, cp, 2, 525, n))
print(regressionUtil( temp, cp, 3, 525, n))