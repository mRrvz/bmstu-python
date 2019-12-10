'''

Задача: матрицу D(5,5) преобразовать в матрицу A(4,5), путем удаления гл. диаг.;
Найти строку, в которой находится минимальное кол-во отриц. элементов.
Вывести ее индекс и кол-во отриц. элем. в ней.

Обозначение переменных:

N - кол-во строк и столбцов исходного списка D.
D, A - исходная и преобр. матрицы.
Elem - мин. кол-во отриц. элементов в строке.\
indexStr - текущий номер строки (исп. в цикле прохода по матрице).
indexStrNull, indexStrK - номер строки (либо строк) с мин. кол-вом отриц. элем.
k, kRepeatedly - кол-во отриц. элем. в текущей строке / предущей строке.
NumberKLines - кол-во строк с мин. возможным и одинаковым кол-вом отриц. элем.
string, strElem, i - рабочие переменные.


Тестовые примеры:

1) Ввод:
0 -1 -1 -2 -3
-1 0 -1 -2 -3
-1 -1 0 -1 -1
-1 -1 -1 0 -1
-1 -1 -1 0 0

Вывод:
-1, -1, -2, -3
-1, -1, -2, -3
-1, -1, -1, -1
-1, -1, -1, -1
-1, -1, 1, 0
Номер строки: 5, отриц. элем-ов: 2

2) Ввод:
1 -2 3
-1 2 3
-1 2 3

Вывод:
-2 3
-1 3
-1 2
Строки с миним. кол-вом элементов: 3 шт; их индесы 1, 2, 3.
В них содержится по 1 отриц. элементу


'''

# Инициализация и ввод

N = False; Elem = 6; indexStr = 0; string = ''; kRepeatedly = False
Flag1 = True; A = []; D = []

while N > 5 or N <= 1:
    N = int(input('Введите число столбцов и строк квадратной матрицы \
(не более 5): '))
    if N > 5:
        print('\nВы ввели число более пяти. \n')
    elif N <= 1:
        print('\nМатрица не может состоять из', N, 'строк и стобцов. \n')

print('\nВведите матрицу ', N, ' * ', N, ' (построчно): ', sep='')
for i in range(N):
    D.append([])
    D[i] = list(map(int, input().split()))

# Вывод исходной матрицы D:
        
print('\nИсходная матрица D: \n')

for string in D:
    for strElem in string:
        print(str(strElem).rjust(3), end ='')
    print()
print()

# Создание матрицы А:

for i in range(N):
    A.append([])
    for j in range(N-1):
        if j < i:
            A[i].append(D[i][j])
        else:
            A[i].append(D[i][j+1])

# Вывод измененной матрицы А, поиск строки с отриц. элем.:          
print('Измененная матрица А: \n')
for string in A:
    indexStr += 1
    k = 0
    for strElem in string:
        if strElem < 0:
            k += 1
        print(str(strElem).rjust(3), end ='')
    print()    
    if k < Elem and k != 0:
        Elem = k
        indexStrNull = indexStr
    elif k == Elem:
        if k != kRepeatedly:
            NumberKLines = 1
            indexStrK = str(indexStrNull)
        kRepeatedly = k
        indexStr1 = indexStr
        NumberKLines += 1
        indexStrK += ', '
        indexStrK += str(indexStr)
    
# Вывод сообщений с информ. о строке с отриц. элем.

if Elem == 1:
    stringForPrint = 'отрицательный элемент.'
else:
    stringForPrint = 'отрицательных элемента.'

if kRepeatedly == Elem:
    Flag1 = False
    print('\nВ матрице', NumberKLines,  'строки, в которых одинаковое \
(и минимальное) кол-во отрицательных элементов.')
    print('Номера этих строк:', indexStrK, '\nВ них содержится', Elem, stringForPrint)

if Flag1 == True:
    if Elem == 6:
        print('\nВ матрице А нет отрицательных элементов.')
    else:
        print('\nНомер строки с минимальным кол-вом отрицательных элементов: ', \
            indexStrNull, '. \nВ ней содерджится ', Elem, ' ', stringForPrint, sep='')
