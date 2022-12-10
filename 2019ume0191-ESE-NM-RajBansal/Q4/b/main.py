# import xlwt
# from xlwt import Workbook
# wb = Workbook()
# sheet = wb.add_sheet('Sheet 1')
def dz_dt( z_current, y_current, t_current):
    return (y_current - z_current)

def dy_dt( z_current, y_current, t_current):
    return (z_current - y_current)

def RK4( ti, tf, h, zi, yi, dx_dt, dy_dt):
    x_current = zi
    y_current = yi
    t_current = ti
    y_values = [yi]
    z_values = [zi]
    t_values = [ti]
    row = 0
    column = 0
    while( t_current < tf):
        # sheet.write(row, column, t_current)
        # sheet.write(row, column + 1, x_current)
        # sheet.write(row, column + 2, y_current)
        row+=1
        x_k1 = dx_dt( x_current, y_current, t_current)
        y_k1 = dy_dt( x_current, y_current, t_current)
        x_k2 = dx_dt( x_current + (x_k1*h)/2, y_current + (y_k1*h)/2, t_current + h/2)
        y_k2 = dy_dt( x_current + (x_k1*h)/2, y_current + (y_k1*h)/2, t_current + h/2)
        x_k3 = dx_dt( x_current + (x_k2*h)/2, y_current + (y_k2*h)/2, t_current + h/2)
        y_k3 = dy_dt( x_current + (x_k2*h)/2, y_current + (y_k2*h)/2, t_current + h/2)
        x_k4 = dx_dt( x_current + (x_k3*h)/2, y_current + (y_k3*h)/2, t_current + h/2)
        y_k4 = dy_dt( x_current + (x_k3*h)/2, y_current + (y_k3*h)/2, t_current + h/2)
        slope_x = (x_k1 + 2*x_k2 + 2*x_k3 + x_k4)/6
        slope_y = (y_k1 + 2*y_k2 + 2*y_k3 + y_k4)/6
        x_current = x_current + slope_x*h
        y_current = y_current + slope_y*h
        t_current = t_current + h
        z_values.append(x_current)
        y_values.append(y_current)
        t_values.append(t_current)
    # print("h = ", h, ", z = ", x_current, ", y = ", y_current)
    # print("t = ", t_values)
    # print("z = ", z_values)
    # print("y = ", y_values)
    # return x_current, y_current
# print("Trying different values of h as follows: ")
h_optimum = 0.0015625
RK4( 0, 1, h_optimum, 0, 40, dz_dt, dy_dt)
# wb.save('result1.xlsx')
