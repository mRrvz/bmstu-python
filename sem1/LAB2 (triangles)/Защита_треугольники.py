from math import sqrt

x1, y1 = map(int, input('Введите координаты X и Y точки A: ').split())
x2, y2 = map(int, input('Введите координаты X и Y точки A: ').split())
x3, y3 = map(int, input('Введите координаты X и Y точки A: ').split())

x_diff21 = x2 - x1
x_diff32 = x3 - x2
x_diff31 = x3 - x1
y_diff21 = y2 - y1
y_diff32 = y3 - y2
y_diff31 = y3 - y1

len1 = sqrt(x_diff21 * x_diff21 + y_diff21 * y_diff21)
len2 = sqrt(x_diff32 * x_diff32 + y_diff32 * y_diff32)
len3 = sqrt(x_diff31 * x_diff31 + y_diff31 * y_diff31)

MinSide = len1
x_diff = x2 - x1
y_diff = y2 - y1
x_mn = x2 * y1
y_mn = y2 * x1
x4 = x3
y4 = y3
len4 = len1
if MinSide > len2:
    MinSide = len2
    x_diff = x3 - x2
    y_diff = y3 - y2
    x_mn = x3 * y2
    y_mn = y3 * x2
    x4 = x1
    y4 = y1
    len4 = len2
if MinSide > len3:
    MinSide = len3
    x_diff = x1 - x3
    y_diff = y1 - y3
    x_mn = x1 * y3
    y_mn = y1 * x3
    x4 = x2
    y4 = y2
    len4 = len3


H1 = abs((y_diff) * x4 - (x_diff) * y4 + x_mn - y_mn) \
                / len4

print()
print('Высота, проведенная из наименьшего угла треугольника: {:4.3f}'.format(H1))

