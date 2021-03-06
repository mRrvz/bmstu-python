'''

Задача: в трех целочилсенных массивах A, B и C заполненных целыми числами,
найти такие элементы которые есть в массиве A, но нет в массивах B и С.

'''

'''

Обозначение переменных:

А, B, C - массивы A, B и С.
stringWithNumbers - строка для вывода чисел, подходящих условию
x - счетчик чисел не подходящих чисел

'''

'''

Тестовые примеры:

1) А = 1 2 3; B = 0 0 0; С = 0 0 1
Вывод: 2 3 

2) А = 0 3 5 6; В = 1 1 2 3; C = 5 0
Вывод: 6

3) А = 0 1 2 5; В = 0 2; С = 1 5
Вывод: нет таких чисел

'''

stringWithNumbers = ''
x = 0

# Заполнение (ввод) массивов A, B и С:

A = list(map(int, input('В одну строку заполните массив А целыми числами: ')\
             .split()))
B = list(map(int, input('\nВ одну строку заполните массив B целыми числами: ')\
             .split()))
C = list(map(int, input('\nВ одну строку заполните массив C целыми числами: ')\
             .split()))

# Цикл проверки чисел подходящих под условие:

for i in range(len(A)):
    if (A[i] in (B)) or (A[i] in (C)):
        x += 1
    else:
        stringWithNumbers += ''.join(str(A[i]) + ' ')

# Вывод результата: 
                        
if stringWithNumbers == '':
    print('\nНет элементов, которые есть в массиве А, но которых нет \
в массивах B и С.')
else:
    print('\nЭлементы, которые cодержит массив А, но не содержат \
массивы B и С: \n')
    print(stringWithNumbers)
