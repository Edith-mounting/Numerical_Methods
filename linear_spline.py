def linearSpline(xi, yi, n, x):
    y = 0
    points = []
    for i in range( 0, n):
        points.append(( xi, yi))
    points.sort()
    for i in range( 0, n - 1):
        if(points[i][0]<=x and points[i+1][0]>x):
            if(points[i][0]==x):
                return points[i][1]
            slope = (points[i+1][1] - points[i][1])/(points[i+1][0] - points[i][0])
            y = points[i][1] + slope*points[i][0]
            return y