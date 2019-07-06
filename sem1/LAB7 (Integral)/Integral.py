'''

Задача: посчитать интеграл через первообразную, методом Симпсона, методом
левых прямоугольников. Посчитать абсолютную и относительну ошибку при
заданном кол-ве разбиений. Так же посчитать интеграл с точностью эпсилон.

Обозначение переменных:

a, b, Eps - нижняя и верхняя граница и эпсилон
n1, n2 - кол-во участков разбиения
trianglesMethodN1, trianglesMethodN2 - знач. интеграла методом пр.  для n1, n2
simpsonMethodN1, simpsonMethodN2 - знач. интеграл методом Симпсона для n1, n2
integralEpsilon, integralEpsilonStepBack - значение интеграла при n и n * n
n, n_1 - рабочие переменные

Тестовые примеры:

1) От 1 до 3, Epsilon = 0.01, разбиений 10 и 100
Метод левых пр.: при 10 = 1.1682290; при 100 = 1.1053086
Метод Симспона: при 10 = 1.0986606; при 100 = 1.0986123
Интеграл с точностью = 1.10383871; шагов 128.
Абсолютная ошибка для левых пр, при 10 6.961670e-02, при 100 6.696295e-03
Относительная ошибка для левых пр, при 10 6.336786e-02, при 100 6.095230e-03
Абсолютная ошибка для Симпсона, при 10 4.830999e-05, при 100 5.262427e-09
Относительная ошибка для Симспона, при 10 4.397365e-05, при 100 4.790067e-09

'''

from math import *

# Инициализация и ввод переменных:

a = True; b = False; Eps = False; n1 = False; n2 = False
trianglesMethodN1 = 0; trianglesMethodN2 = 0; simpsonMethodN1 = 0
simpsonMethodN2 = 0; integralEpsilonStepBack = 0; integralEpsilon = 0
n = 4; n_1 = 2

while a >= b:
    a, b = map(float, input('Введите нижний и верхний предел подинтегральной \
функции: ').split())
    if a >= b:
        print('\nВерхний предел меньше или равен нижнему пределу \
подинтегральной фукнции\n')

while Eps <= 0:
    Eps = float(input('\nВведите Epsilon: '))
    if Eps <= 0:
        print('\nEpsilon меньше либо равен нуля.')
              
while n1 <= 0 or n2 <= 0 or n2 % 2 != 0:
    n1, n2 = map(int, input('\nВведите кол-во участков разбиения для метода \
левых прямоугольников и для метода Симпсона (четное): ').split())
    if n1 <= 0 or n2 <= 0:
        print('\nКоличество участков не может быть отрицательным.')
    if n2 % 2 != 0:
        print('\nКоличество участков для метода Симпсона должно быть четным.')

def f(x):
    return x * x

h1 = (b - a) / n1
h2 = (b - a) / n2

Integral = (b * b * b / 3) - (a * a * a / 3)

#Integral = log(abs(b)) - log(abs(a))

# Вычисление интеграла методом левых пр. на n1 и n2:

for i in range(n1):
    x_i = a + i * h1
    trianglesMethodN1 += f(x_i)

for i in range(n2):
    x_i = a + i * h2
    trianglesMethodN2 += f(x_i)

trianglesMethodN1 *= h1
trianglesMethodN2 *= h2

# Вычисление интеграла методом Симспона на n1 и n2:

for i in range(1, n1):
    x_i = a + i * h1
    simpsonMethodN1 += n * f(x_i)
    n, n_1 = n_1, n

n = 4; n_1 = 2

for i in range(1, n2):
    x_i = a + i * h2
    simpsonMethodN2 += n * f(x_i)
    n, n_1 = n_1, n

simpsonMethodN1 += f(a) + f(a + n1 * h1)
simpsonMethodN2 += f(a) + f(a + n2 * h2)
simpsonMethodN1 *= h1 / 3
simpsonMethodN2 *= h2 / 3    

# Вычисление интеграла с точностью Epsilon:

integralEpsilonStepBack = (b - a) * a
n = 1

while True:
    integralEpsilon = 0
    n *= 2
    for i in range(n):
        x_i = a + i * ((b - a) / n)
        integralEpsilon += f(x_i)
    integralEpsilon *= (b - a) / n  
    if abs(integralEpsilon - integralEpsilonStepBack) < Eps:
        break
    else:
        integralEpsilonStepBack = integralEpsilon

# Подсчет абсолютной и относительной погрешности для каждого метода:      

absoluteMistakeTrianglesN1 = abs(Integral - trianglesMethodN1)
relativeMistakeTrianglesN1 = abs((Integral - trianglesMethodN1) / Integral)

absoluteMistakeTrianglesN2 = abs(Integral - trianglesMethodN2)
relativeMistakeTrianglesN2 = abs((Integral - trianglesMethodN2) / Integral)

'''
absoluteMistakeSimpsonN1 = abs(Integral - simpsonMethodN1)
relativeMistakeSimpsonN1 = abs((Integral - simpsonMethodN1) / Integral)

absoluteMistakeSimpsonN2 = abs(Integral - simpsonMethodN2)
relativeMistakeSimpsonN2 = abs((Integral - simpsonMethodN2) / Integral)
'''

# Вывод значений интеграла:

print('\n┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓')
print('┃      Метод      ┃', 'n1 ='.rjust(8), n1, '┃'.rjust(7-len(str(n1))), \
'n2 ='.rjust(8), n2, '┃'.rjust(7-len(str(n2))))
print('┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫')
print('┃ Метод левых пр. ┃{:16.7f}'.format(trianglesMethodN1), \
      '┃{:16.7f}'.format(trianglesMethodN2), '┃')
print('┣━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫')
print('┃ Метод Симспона  ┃{:16.7f}'.format(simpsonMethodN1), \
      '┃{:16.7f}'.format(simpsonMethodN2), '┃')
print('┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛\n')

print('Точное значение интеграла равно: {:.8f}'.format(Integral))
print('\nЗначение интеграла с точностью Epsilon посчитанное с помощью метода левых пр. равно: {:.8f}'.format(integralEpsilon))
print('Понадобилось разбиений:', n)

# Вывод погрешнсоетй и вычисление с точностью Epsilon: 

print('\nПогрешность для метода левых прямоугольников: \n')
print('┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓')
print('┃      n      ┃ Абсолют. ошибка ┃ Относит. ошибка ┃')
print('┣━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫')
print('┃   n =', n1,'┃'.rjust(6-len(str(n1))),\
      '{:15.6e}'.format(absoluteMistakeTrianglesN1), \
      '┃{:16.6e}'.format(relativeMistakeTrianglesN1), '┃')
print('┣━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫')
print('┃   n =', n2,'┃'.rjust(6-len(str(n2))),\
      '{:15.6e}'.format(absoluteMistakeTrianglesN2), \
      '┃{:16.6e}'.format(relativeMistakeTrianglesN2), '┃')
print('┗━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛\n')

''' 
print('Погрешность для метода Симпсона: \n')
print('┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓')
print('┃      n      ┃ Абсолют. ошибка ┃ Относит. ошибка ┃')
print('┣━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫')
print('┃   n =', n1,'┃'.rjust(6-len(str(n1))),\
      '{:15.6e}'.format(absoluteMistakeSimpsonN1), \
      '┃{:16.6e}'.format(relativeMistakeSimpsonN1), '┃')
print('┣━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫')
print('┃   n =', n2,'┃'.rjust(6-len(str(n2))),\
      '{:15.6e}'.format(absoluteMistakeSimpsonN2), \
      '┃{:16.6e}'.format(relativeMistakeSimpsonN2), '┃')
print('┗━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛\n')
'''
