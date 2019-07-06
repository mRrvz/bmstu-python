'''

Задача: по введеному начальному значению t, шагу и конечному значению t
посчитать и вывести в виде таблице значения функций P1 и P2 от начального
значения до конечного, с указанным шагом.

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
NumberNew - temp переменная для обхода проверок, если шаг не попадает на Х = 0.0
NumberOld - предыдущее значение t
checkOY - переменная, отсекающая OY
ymin - минимальное знач. функции.
ymax - максимальное знач. функции
Sequence - кол-во засчек
SequencePlus - кол-во интервало, полученных после разделения засечками
size - размер OY
len - длина от ymin до ymax
spacesTo - кол-во пробелов до OX
iToOX - кол - во строк до OY
y - текущее значение функции 
spaces - кол - во пробелов до значения функции по OY.
spacesDiff - разница между spaceTo и spaces
blocks - кол-во знаков '━' до ближайшей засечки.
blocksLast - кол-во знаков до '━' конца строки
spacesToNumb - кол-во пробелов до номера X
spacesToNumbStr - строка для с кол-вом пробелов для format'a
spacesToMax - кол-во пробелов до 'max'
Check1 - проверка, не позволяющая приравнять Number к NumbeOld, в случае если шаг попадает на Х = 0.0
check - проверка, не позволяющая запустить построение OX больше одного раза, в случае если шаг не попадает на X = 0.0

'''

'''

Тестовый пример: 

При вводе нач. значения t = 1.5, шага 0.1 и конечного знач. t = 4,
программа должна выводить:

┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃   Аргумент   ┃        P1        ┃        P2       ┃
┣━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫
┃           1.5┃            1.0612┃           1.9775┃
┃           1.6┃            0.9715┃           1.5776┃
┃           1.7┃            0.8602┃           1.1719┃
┃           1.8┃            0.7285┃           0.7664┃
┃           1.9┃            0.5777┃           0.3671┃
┃           2.0┃            0.4099┃          -0.0200┃
┃           2.1┃            0.2271┃          -0.3889┃
┃           2.2┃            0.0317┃          -0.7336┃
┃           2.3┃           -0.1738┃          -1.0481┃
┃           2.4┃           -0.3864┃          -1.3264┃
┃           2.5┃           -0.6032┃          -1.5625┃
┃           2.6┃           -0.8212┃          -1.7504┃
┃           2.7┃           -1.0372┃          -1.8841┃
┃           2.8┃           -1.2479┃          -1.9576┃
┃           2.9┃           -1.4502┃          -1.9649┃
┃           3.0┃           -1.6409┃          -1.9000┃
┃           3.1┃           -1.8168┃          -1.7569┃
┃           3.2┃           -1.9751┃          -1.5296┃
┃           3.3┃           -2.1130┃          -1.2121┃
┃           3.4┃           -2.2278┃          -0.7984┃
┃           3.5┃           -2.3173┃          -0.2825┃
┃           3.6┃           -2.3795┃           0.3416┃
┃           3.7┃           -2.4126┃           1.0799┃
┃           3.8┃           -2.4153┃           1.9384┃
┃           3.9┃           -2.3864┃           2.9231┃
┃           4.0┃           -2.3255┃           4.0400┃
┗━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛

Количество значений P1 попавших в диапазон 0.2 <= P1 <= 1.6: 7

'''

from math import *

step = False

while step <= 0 or t2 < t1 :
    t1, step, t2 = map(float,input('Введите начальное значение t, шаг и конечное значение t: ').split())
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
checkOX = t1
checkiToOX = t1
iToOX = -1
check2 = False
# Подсчитываем значения P1 и P2 на заданном интервале и выводим таблицу:

endFor = int((t2 - t1) / step + 1)
print()
print('┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓\n'
      '┃   Аргумент   ┃        P         ┃        P1       ┃\n' 
      '┣━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━┫')
for i in range(endFor):
    #p1 = sin(t1)
    p = t1 * t1 * t1 - 5.09 * t1 * t1 + 4.57 * t1 + 3.2
    p1 = sin(t1) + 0.6 * t1 * cos(t1)

    # Подсчет кол-ва строк до ОХ:
    if round(t1,3) < 0.0:
        iToOX += 1
    if checkiToOX == 0:
        check2 = True

    if abs(p) < 1000 and abs(p1) < 1000:
        print('┃     {:9.1f}┃      {:12.4f}┃     {:12.4f}┃'.format(t1, p, p1))
    else:
        print('┃     {:9.1f}┃      {:12.4e}┃     {:12.4e}┃'.format(t1, p, p1))
    A.append(p)
    t1 += step
    if 0.2 <= p <= 1.6:
        k += 1
print('┗━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛')
print('\nКоличество значений P попавших в диапазон 0.2 <= P <= 1.6:', k)

print()

if check2 == True:
    iToOX -= 1

Sequence = False
while Sequence < 4 or Sequence > 8:
    Sequence = int(input('Введите количество засечек (от 4 до 8): '))
    if Sequence < 4 or Sequence > 8:
        print('\nКоличество засечек должно быть от 4-х до 8-ми.')
        print()

ymin = min(A)
ymax = max(A)

print()
if abs(ymin) < 1000 and abs(ymax) < 1000:
    print('Минимальное значение (min) функции = {:2.3f}'.format(ymin))
    print('\nМаксимальное значение (max) функции = {:2.3f}\n'.format(ymax))
else:
    print('Минимальное значение (min) функции = {:2.3e}'.format(ymin))
    print('\nМаксимальное значение (max) функции = {:2.3e}\n'.format(ymax))

SequencePlus = Sequence + 1
if Sequence == 4 or Sequence == 6:
    size = 70
else:
    size = 72
#size = round(65 / (SequencePlus) * (SequencePlus))
len = ymax - ymin

check = True
spacesTo = round( (0 - ymin) / (len / size) )

A.append(ymax)

m = 0
blocks = size // SequencePlus
blocksLast = blocks

           
print('График функции P = t^3 - 5.09 * t^2 + 4.57 * t + 3.2')
print()

# Цикл построения графика:

for i in range(endFor):
    y = A[i]
    spaces = round((y - ymin) / (len / size))
    NumberOld = Number
    Check1 = False
    Number = round(Number + step, 3)
    blocksLastFirst =  spaces - (blocks + 1) * Sequence 
    blocksLastSecond = blocksLast - blocksLastFirst -1

    # Проверка построения OX, для функции с шагом, не попадающим на х = 0.0:

    if  NumberOld < 0 and Number >= 0 and check == True and Number != 0:
        NumberNew = NumberOld
        Check1 = True
        Number = 0.000

    if checkOY >= 0:
        print('min ', ' ' * (size ), ' max', sep='')
        print(('━' * blocks + '┳') * Sequence, '━' * (blocksLast + 4), sep='')
        checkOY = -1

    # Проверка, пересекает ли функция на заданном отрезке OX.
    # Если пересекает, то выполняется этот блок:

    if ymin < 0:

        # Проверка на расположение значения функции (*) относительно OX.
        # В данном блоке * левее OX:

        if spacesTo >= spaces:
            spacesDiff = spacesTo - spaces
            spacesToNumb = size - spacesTo + 12  #!
            spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'

            if Number == 0.000 and check == True:
                if spaces >= blocks * Sequence:
                    spacesToNumb = 74   - ((blocks + 1) * Sequence + blocksLastSecond + blocksLastFirst ) #!
                    spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'
                    print(('━' * blocks + '┳') * Sequence, '━' * blocksLastFirst, \
                          '*', '━' * blocksLastSecond,\
                        '━▶ P', spacesToNumbStr.format(round(Number,3)), sep='')
                else:
                    SequenceOne = spaces // blocks
                    SequenceTwo = Sequence - SequenceOne - 1
                    blocksOne = spaces % blocks  - SequenceOne
                    blocksTwo = blocks - blocksOne - Sequence
                    spacesToNumb = (73 + (Sequence - 3))  - ((blocks + 1) * Sequence + blocksLast) #!
                    spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'
                    print(('━' * blocks + '┳') * SequenceOne, '━' * blocksOne, '*', \
                          '━' * blocksTwo, '┳', ('━' * blocks + '┳') * SequenceTwo,\
                          '━' * blocksLast,'━' * 4 , '━▶ P', spacesToNumbStr.format(round(Number, 3)), sep='')
                if Check1 == True:
                    Number = NumberNew
                check = False
                continue

            if i  == iToOX and i % 2 == 0:
                #spacesToNumb = 75   - ((blocks + 1) * Sequence + blocksLastSecond + blocksLastFirst + 1 - (Sequence + 4)) #!
                spacesToNumb = 67 - ((blocks + 1) * Sequence + blocksLastSecond + blocksLastFirst + 1 - (Sequence + 4))
                spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'
                spacesToMax = ((blocks + 1) * Sequence + blocksLastFirst  + blocksLastSecond) - spaces - (Sequence - 4)
                print('min ', ' ' * (spaces - 4), '*', \
                      ' ' * spacesDiff, '┃', ' ' * spacesToMax, \
                      'max', spacesToNumbStr.format(round(Number,3)), sep='')
            elif i == iToOX and i % 2 != 0:
                spacesToMax = size - spacesTo + 1
                print('min ', ' ' * (spaces - 4), '*', \
                      ' ' * spacesDiff, '┃', ' ' * spacesToMax , \
                      'max', sep='')
            elif i % 2 == 0:
                print(' ' * spaces,'*', ' ' * spacesDiff, '┃', \
                      spacesToNumbStr.format(Number), sep='')
            else:
                print(' ' * spaces, '*', ' ' * spacesDiff, '┃', sep='')

        # Проверка на расположение значения функции (*) относительно OX.
        # В данном блоке * правее OX:

        else:
            spacesDiff = spaces - spacesTo
            spacesToNumb = size - spaces + 11 #!
            spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'
            spacesToMax = (size - spacesTo - spacesDiff)
            if Number == 0.000 and check == True:
                if spaces >= blocks * Sequence:
                    spacesToNumb = 74 - ((blocks + 1) * Sequence + blocksLastSecond + blocksLastFirst ) #!
                    spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'
                    print(('━' * blocks + '┳') * Sequence, '━' * blocksLastFirst, \
                          '*', '━' * blocksLastSecond,\
                        '━▶ P', spacesToNumbStr.format(round(Number,3)), sep='')
                else:

                    SequenceOne = spaces // blocks
                    SequenceTwo = Sequence - SequenceOne - 1
                    blocksOne = spaces % blocks - SequenceOne
                    blocksTwo = blocks - blocksOne - 1
                    spacesToNumb = (77 + (Sequence - 3)) - ((blocks + 1) * Sequence + blocksLast) #!
                    spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'
                    print(('━' * blocks + '┳') * SequenceOne, '━' * blocksOne, '*', \
                          '━' * blocksTwo, '┳', ('━' * blocks + '┳') * SequenceTwo, \
                          '━' * blocksLast, '━' * 4, '━▶ P', spacesToNumbStr.format(round(Number, 3)), sep='')
                if Check1 == True:
                    Number = NumberNew
                check = False
                continue

            if i  == iToOX and i % 2 == 0:
                spacesToMax = ((blocks + 1) * Sequence + blocksLastFirst  + blocksLastSecond) - spaces - (Sequence - 4)
                spacesToNumb = 67 - ((blocks + 1) * Sequence + blocksLastSecond + blocksLastFirst + 1 - (Sequence + 4))
                spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'
                print('min', ' ' * (spacesTo - 2), '┃', \
                               ' ' * spacesDiff, '*', ' ' * spacesToMax, \
                      'max', spacesToNumbStr.format(round(Number,3)), sep='')
            elif i == iToOX and i % 2 != 0:
                print('min', ' ' * (spacesTo - 2), '┃', \
                      ' ' * spacesDiff, '*', ' ' * spacesToMax, 'max', sep='')
            elif i % 2 == 0:
                print(' ' * (spacesTo + 1), '┃', ' ' * spacesDiff, \
                      '*', spacesToNumbStr.format(round(Number,3)), sep='')
            else:
                print(' ' * (spacesTo + 1), '┃', ' ' * spacesDiff, '*', sep='')

    # Если функция на заданном отрезке не пересекает OX, выполняется этот блок.

    else:
        spacesToNumb = size - spaces + 11 #!
        spacesToNumbStr = '{:' + str(spacesToNumb) + '.2f}'
        if i % 2 == 0:
            print(' ' * spaces, '*', spacesToNumbStr.format(Number), sep='')
        else:
            print(' ' * spaces, '*', sep='')

if t2 < 0:
    print(('━' * blocks + '┳') * Sequence, '━' * (blocksLast + 4), '━▶ Y', sep='')
if ymin < 0:
    print(' ' * spacesTo, '▼')
if ymin < 0:
    print(' ' * spacesTo, 'T')
