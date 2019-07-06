a, b = map(int, input('Введите нижнюю и верхнюю границу интеграла: ').split())
eps = float(input('\nВведите точность Epsilon: '))

from math import log

def f(x):
    return 1 / x
n = 3
integral_Step_Back = 0
integral_Now = 0

for j in range(2):
    h = (b - a) / n
    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            if j == 0:
                integral_Step_Back += 2 * f(x_i)
            else:
                integral_Now += 2 * f(x_i)
        else:
            if j == 0:
                integral_Step_Back += 3 * f(x_i)
            else:
                integral_Now += 3 * f(x_i)
    if j == 0:            
        n *= 2 

integral_Step_Back += f(a) + f(b)
integral_Step_Back *= (3 * ((b - a) / 3)) / 8
integral_Now += f(a) + f(b)
integral_Now *= (3 * ((b - a) / 6)) / 8

#integral = log(b) - log(a)
#print(integral_Now, integral_Step_Back)
#print('Точное значение интеграла: {:.7f}'.format(integral))

while abs(integral_Now - integral_Step_Back) > eps:
    integral_Step_Back = integral_Now
    n *= 2
    h = (b - a) / n
    integral_Now = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            integral_Now += 2 * f(x_i)
        else:
            integral_Now += 3 * f(x_i)
    integral_Now *= (3 * h) / 8
    #print(integral_Now, integral_Step_Back)
    
print('\nИнтеграл с точностью', eps, 'равен: {:.7f}'.format(integral_Now))
print('\nДля вычисления понадобилось', n, 'шагов.')
