'''

Задача:
1) По введеному начальному значению t, шагу и конечному значению t
посчитать и вывести в виде таблице значения функций P1 и P2 от начального
значения до конечного, с указанным шагом.

2) Построить график функции P2.

'''

'''

Обозначение переменных:

t1 - начальное значение t
step - шаг t
t2 - конечное значение t
endFor - число повторений цикла for
p1 - функция sin(t) + 0.6 * t * cos(t)
p2 - функция t * t * t - 5.09 * t * t + 4.57 * t + 3.2
k - количество значений P1 попавших в диапазон 0.2 <= P1 <= 1.6
A - список значений функции P2
Number - текущее значение t
NumberPrevious - предыдущее значение t
checkOY - переменная, отсекающая OY
ymin - минимальное знач. функции.
ymax - максимальное знач. функции
Sequence - кол-во засчек
size - размер OY
len - длина от ymin до ymax
spacesToOX - кол-во пробелов до OX
iToOX - кол - во строк до OY
spaces - кол - во пробелов до значения функции по OY.
spacesDiff - разница между spaceTo и spaces
blocks - кол-во знаков '━' до ближайшей засечки.
blocksLast - кол-во знаков до '━' конца строки
spacesToMax - кол-во пробелов до 'max'
check1, Check2, Check3, CheckOY_1, CheckOY, CheckOX - проверки 
блокады не позволяющие запустить блок еще раз, при его выполнении.
spaces_StrI - кол-во пробелов в строке с выводом min, max до знач. функции
LastBlocksFirst - кол-во знаков '-' в последнем блоке, до знач функции
LastBlocksSecond - кол-во знаков '-' в последнем блоке, после знач. функции
spaceAfterOX - кол-во пробелов после OX
spaceToNumber - кол-во пробелов до номера по OX
spacesDiff - | spaceToOx - space | - 1

'''

'''

Тестовый пример: 

При вводе нач. значения t = 1.5, шага 0.2 и конечного знач. t = 4,
программа должна выводить:

┏━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Аргумент  ┃      P1      ┃       P2     ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━┫
┃      1.50 ┃       1.0612 ┃       1.9775 ┃
┃      1.70 ┃       0.8602 ┃       1.1719 ┃
┃      1.90 ┃       0.5777 ┃       0.3671 ┃
┃      2.10 ┃       0.2271 ┃      -0.3889 ┃
┃      2.30 ┃      -0.1738 ┃      -1.0481 ┃
┃      2.50 ┃      -0.6032 ┃      -1.5625 ┃
┃      2.70 ┃      -1.0372 ┃      -1.8841 ┃
┃      2.90 ┃      -1.4502 ┃      -1.9649 ┃
┃      3.10 ┃      -1.8168 ┃      -1.7569 ┃
┃      3.30 ┃      -2.1130 ┃      -1.2121 ┃
┃      3.50 ┃      -2.3173 ┃      -0.2825 ┃
┃      3.70 ┃      -2.4126 ┃       1.0799 ┃
┃      3.90 ┃      -2.3864 ┃       2.9231 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┛

Количество значений P1 попавших в диапазон 0.2 <= P1 <= 1.6: 7

'''

from math import *

step = False

while step <= 0 or t2 < t1 :
    t1, step, t2 = map(float,input('Введите начальное значение t,\
шаг и конечное значение t: ').split())
    if t2 < t1:
        print('\nНачальное значение больше конечного.')
        print()
    elif step < 0:
        print('\nОтрицательный шаг.')
        print()
    if step == 0:
        print('\nШаг равен нулю.')
        print()

k = 0
A = []
Number = t1 - step
checkOY = t1
iToOX = -1
check2 = False
CheckOY_1 = False


check1 = True

# Подсчитываем значения P1 и P2 на заданном интервале и выводим таблицу:

endFor = int((t2 - t1) / step + 1)
print()
print('┏━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓\n'
      '┃ Аргумент  ┃      P1      ┃       P2     ┃\n' 
      '┣━━━━━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━┫')
for i in range(endFor):

    #p2 = sin(t1)
    #p2 = t1
    p2 = t1 * t1 * t1 - 5.09 * t1 * t1 + 4.57 * t1 + 3.2
    p1 = sin(t1) + 0.6 * t1 * cos(t1)

    # Подсчет кол-ва строк до ОХ:

    if round(t1,3) < 0.0:
        iToOX += 1
    if round(t2,3) < 0:
        iToOX = -1
        CheckOY_1 = True

    if abs(p1) < 1000 and abs(p2) < 1000:
        print('┃{:10.2f} ┃{:13.4f} ┃\
{:13.4f} ┃'.format(t1, p1, p2))
    else:
        print('┃{:10.2f} ┃{:13.4e} ┃\
{:13.4e} ┃'.format(t1, p1, p2))
    A.append(p2)
    t1 += step
    if 0.2 <= p1 <= 1.6:
        k += 1
print('┗━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┛')
print('\nКоличество значений P1 попавших в диапазон 0.2 <= P1 <= 1.6:', k)

print()

Sequence = False
while Sequence < 4 or Sequence > 8:
    Sequence = int(input('Введите количество засечек (от 4 до 8): '))
    if Sequence < 4 or Sequence > 8:
        print('\nКоличество засечек должно быть от 4-х до 8-ми.')
        print()

ymin = min(A)
ymax = max(A)

#NullY = sin(0)
NullY = 0 - 5.09 * 0 + 4.57 * 0 + 3.2

# 4 - 68, 5 - 71, 6 - 69, 7 -  69, , 8 - 69

if Sequence >= 6:
    size = 69 + Sequence
elif Sequence == 4:
    size = 68 + Sequence
else:
    size = 71
blocks = (size - Sequence) // (Sequence - 1) + 1

print()
if abs(ymin) < 1000 and abs(ymax) < 1000:
    print('Минимальное значение (min) функции = {:2.3f}'.format(ymin))
    print('\nМаксимальное значение (max) функции = {:2.3f}\n'.format(ymax))
else:
    print('Минимальное значение (min) функции = {:2.3e}'.format(ymin))
    print('\nМаксимальное значение (max) функции = {:2.3e}\n'.format(ymax))

print('График функции P2 = t^3 - 5.09 * t^2 + 4.57 * t + 3.2:\n')


lenOY = ymax - ymin
spacesToOX = round((0 - ymin) / (lenOY / size))
if spacesToOX <= 0:
    spacesToOX = 0
Check2 = False
Check3 = True
spacesToMax = size - 6

NumbOY = lenOY / (Sequence - 1)
print()
str1 = ''

SizeOY = round((ymax - ymin) / (lenOY / size))

ymin1 = ymin

# Вычисление пробелов для знач. по OY (для первого числа, ymin)

A1 = [0] * (Sequence + 1)
A2 = [0] * (Sequence + 1)
A1[0] = ymin

if ymin < 0:
    CheckMin1 = 1
else:
    CheckMin1 = 0
if abs(A1[0]) > 99:
    A2[0] = '{:0.1e}'
    LenghtLast = 4
    LenghtLast = 7 + CheckMin1
elif abs(A1[0]) > 10:
    A1[0] = int(ymin)
    A2[0] = '{:0d}'
    LenghtLast = 2 + CheckMin1
else:
    A2[0] = '{:0.1f}'
    LenghtLast = 3 + CheckMin1
qw = 0

# Вычисление пробелов для знач. по OY

for i in range(1,Sequence):
    if i == (Sequence - 1):
        qw = 1
    CheckMin1 = 0
    A1[i] = A1[i-1] + NumbOY
    if A[i] < 0:
        CheckMin1 = 1
    if abs(A1[i]) > 99:
        spacesToNumbOY = (blocks + 7  + CheckMin1) - LenghtLast - qw
        A2[i] = '{:' + str(spacesToNumbOY) + '.1e}'
        LenghtLast = 7 + CheckMin1
    elif abs(A1[i]) > 10:
        A1[i] = int(A1[i])
        spacesToNumbOY = (blocks  + 1  + 1 + CheckMin1) - LenghtLast - qw
        A2[i] = '{:' + str(spacesToNumbOY) + 'd}'
        LenghtLast = 2  + CheckMin1
    else:
        spacesToNumbOY = (blocks   + 3 + CheckMin1)  - LenghtLast - qw
        A2[i] = '{:' + str(spacesToNumbOY) + '.1f}'
        LenghtLast = 3  + CheckMin1

# Вывод OY со знач.

if Sequence == 4:
    print(A2[0].format(A1[0]), A2[1].format(A1[1]), A2[2].format(A1[2]),\
          A2[3].format(A1[3]))
elif Sequence == 5:
    print(A2[0].format(A1[0]), A2[1].format(A1[1]), A2[2].format(A1[2]), \
          A2[3].format(A1[3]), A2[4].format(A1[4]))
elif Sequence == 6:
    print(A2[0].format(A1[0]), A2[1].format(A1[1]), A2[2].format(A1[2]), \
          A2[3].format(A1[3]), A2[4].format(A1[4]), A2[5].format(A1[5]))
elif Sequence == 7:
    print(A2[0].format(A1[0]), A2[1].format(A1[1]), A2[2].format(A1[2]), \
          A2[3].format(A1[3]), A2[4].format(A1[4]), A2[5].format(A1[5]), \
          A2[6].format(A1[6]))
else:
    print(A2[0].format(A1[0]), A2[1].format(A1[1]), A2[2].format(A1[2]), \
          A2[3].format(A1[3]), A2[4].format(A1[4]), A2[5].format(A1[5]),\
          A2[6].format(A1[6]),A2[7].format(A1[7]))


print('┏', ('━' * blocks + '┳') * (Sequence - 2), \
      '━' * (blocks - 1) + '┳', '━' * 5, sep='')

# Цикл построения графика:

for i in range(endFor):
    spaces = round((A[i] - ymin) / (lenOY / size))
    spacesCounter = 0
    if Number < 0.000:
        spacesCounter = 1
    # Прибавление шага.
    # Check2 - проверка, не позволяющая выводить OY (P1) беск. раз.

    if Check2 == False:
        NumberPrevious = Number
        Number = round(Number + step, 3)
    '''
    # Вывод строки с max и min.
    # Четный блок (справа выводятся тек. знач. X (T)):

    if iToOX == i and i % 2 == 0:
        spacesToNumb = 3

        # Знач. функции левее OX (T):

        if spacesToOX > spaces:
            spacesToOX_I = spacesToOX - spaces - 2 + 1
            spaces -= 4
            spacesToMax = size - spacesToOX  + (Sequence - 4) + 2
            print('min', ' ' * spaces, '*', ' ' * spacesToOX_I, '┃', \
                  ' ' * spacesToMax, 'max', ' ' * spacesToNumb, Number,\
                  sep='')

        # Знач. функции правее OX (T):

        elif spacesToOX < spaces:
            spacesToOX_I = spacesToOX - 4
            spacesToMax = size - spaces + (Sequence - 3) + 1
            spaces = spaces - spacesToOX_I - 4
            print('min', ' ' * spacesToOX_I, '┃', ' ' * (spaces - 1),'*', \
                   ' ' * spacesToMax, 'max', ' ' * spacesToNumb, Number, \
                  sep='')

        # Знач. функции совпадает с OX (T):

        else:
            spaces_StrI = spaces - 4
            spacesToMax = size - spaces_StrI - 2 + (Sequence - 4)
            print('min', ' ' * spaces_StrI, '*', ' ' * spacesToMax,\
                  'max',' ' * spacesToNumb, Number, sep='')
        continue
    # Нечетный блок (не выводятся тек. знач. X (T))

    elif iToOX == i and i % 2 != 0:

        # Знач. функции левее OX (T):

        if spacesToOX > spaces:
            spacesToOX_I = spacesToOX - spaces - 2 + 1
            spaces -= 4
            spacesToMax = size - spacesToOX  + (Sequence - 4)
            print('min', ' ' * spaces, '*', ' ' * spacesToOX_I, '┃', \
                  ' ' * spacesToMax, 'max', sep='')

        # Знач. функции правее OX (T):

        elif spacesToOX < spaces:
            spacesToOX_I = spacesToOX - 4
            spacesToMax = size - spaces - 2 + (Sequence - 3) + 1
            spaces = spaces - spacesToOX_I - 4
            print('min', ' ' * spacesToOX_I, '┃', ' ' * (spaces - 1), '*', \
                  ' ' * spacesToMax, 'max', sep='')

        # Знач. функции совпадает с OX (T):

        else:
            spaces_StrI = spaces - 4
            spacesToMax = size - spaces_StrI - 2 + (Sequence - 4)
            print('min', ' ' * spaces_StrI, '*', ' ' * spacesToMax, \
                  'max', sep='')
        continue

    # Вывод OY (P2):

    if NumberPrevious < 0 and Number >= 0 and checkOY < 0 and Check3 == True:
        spaces = round((NullY - ymin) / (lenOY / size))
        spacesToEnd = size - spaces + 4 + (Sequence - 4)
        if i % 2  == 0:
            print('━' * (spaces -1), '*', '━' * spacesToEnd, '▶ P2', ' 0.0', \
              sep='')
        else:
            print('━' * (spaces -1), '*', '━' * spacesToEnd, '▶ P2',  \
              sep='')
        if Number != 0.000:
            Check2 = True
        Check3 = False
        continue
    '''
    Check2 = False
 
    # Если график не пересекает OX (T):

    if spacesToOX == 0:
        spacesAfterOX = size - spaces + 5 - spacesCounter + 5 - (4 - Sequence)
        if i % 2 == 0:
            print(' ' * spaces, '*', ' ' * spacesAfterOX, round(Number, 3), \
                  sep='')
        else:
            print(' ' * spaces, '*')
        continue

    # Знач. функции левее ОХ (T):

    if spacesToOX > spaces:
        if spaces == 0:
            spaces = 1
        if i % 2 == 0:
            spacesDiff = spacesToOX - spaces - 1
            spacesAfterOX = size - spacesToOX + 3 - spacesCounter + 6 \
                            - (4 - Sequence)
            print(' ' * (spaces - 1), '*', ' ' * spacesDiff, '┃', \
                  ' ' * spacesAfterOX, round(Number,3), sep='' )
        else:
            spacesDiff = spacesToOX - spaces - 1
            print(' ' * (spaces - 1), '*', ' ' * spacesDiff, '┃', sep ='')

    # Знач. функции cовпадает с ОХ (T):

    if spacesToOX == spaces:
        if i % 2 == 0:
            spacesDiff = size - spaces + 3 - spacesCounter + 6 - (4 - Sequence)
            print(' ' * (spacesToOX - 1)  , '*', ' ' * spacesDiff, \
                  round(Number,3), sep='')
        else:
            print(' ' * (spacesToOX - 1), '*', sep ='')

    # Знач. функции правее ОХ (T):

    if spacesToOX < spaces:
        if i % 2 == 0:
            spacesDiff = spaces - spacesToOX - 1
            spacesAfterOX = size - spaces - spacesCounter + 5  + Sequence
            print(' ' * (spacesToOX - 1) ,'┃', ' ' * spacesDiff, \
                  '*', ' ' * spacesAfterOX, round(Number,3), sep='')
        else:
            spacesDiff = spaces - spacesToOX - 1
            print(' ' * (spacesToOX-1) , '┃', ' ' * spacesDiff, '*', sep='')

if spacesToOX > 0:
    print(' ' * (spacesToOX - 1) , '▼', sep='')
    print(' ' * (spacesToOX - 1), 'T', sep='')

#print(spacesToOX)
