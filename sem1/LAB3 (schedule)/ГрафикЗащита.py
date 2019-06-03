
from math import *

step = False

while step <= 0 or t2 < t1 :
    t1, step, t2 = map(float,input('Введите C, шаг и D: ').split())

k = 0
A = []
Number = t1 - step
checkOY = t1
iToOX = -1
check2 = False
CheckOY_1 = False


check1 = True

endFor = int((t2 - t1) / step + 1)
print()

for i in range(endFor):

    p2 = t1 * t1 - 49

    # Подсчет кол-ва строк до ОХ:

    if round(t1,3) < 0.0:
        iToOX += 1
    if round(t2,3) < 0:
        iToOX = -1
        CheckOY_1 = True

    A.append(p2)
    t1 += step

ymin = min(A)
ymax = max(A)

NullY = -49


size = 71
blocks = (size - 5) // (5 - 1) + 1


print('График функции b = x * x - 49')


lenOY = ymax - ymin
spacesToOX = round((-49 - ymin) / (lenOY / size))
if spacesToOX <= 0:
    spacesToOX = 0
Check2 = False
Check3 = True
spacesToMax = size - 6

NumbOY = lenOY / (5 - 1)
print()
str1 = ''

SizeOY = round((ymax - ymin) / (lenOY / size))

ymin1 = ymin


A1 = [0] * (5 + 1)
A2 = [0] * (5 + 1)
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


for i in range(1,5):
    if i == (5 - 1):
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



print(A2[0].format(A1[0]), A2[1].format(A1[1]), A2[2].format(A1[2]), A2[3].format(A1[3]), A2[4].format(A1[4]))



print('┏', ('━' * blocks + '┳') * (5 - 2), \
      '━' * (blocks - 1) + '┳', '━' * 5, sep='')


for i in range(endFor):
    spaces = round((A[i] - ymin) / (lenOY / size))
    spacesCounter = 0
    if Number < 0.000:
        spacesCounter = 1


    if Check2 == False:
        NumberPrevious = Number
        Number = round(Number + step, 3)
    spacesToMax = size - spaces - 2 + (5 - 3) + 1
    if NumberPrevious < 0 and Number >= 0 and checkOY < 0 and Check3 == True:
        spaces = round((NullY - ymin) / (lenOY / size))
        spacesToEnd = size - spaces + 4 + (5 - 4)
        if i % 2  == 0:
            print('━' * (spaces -1), '*', '━' * spacesToEnd, '▶ B', ' 0.0', \
              sep='')
        else:
            print('━' * (spaces -1), '*', '━' * spacesToEnd, '▶ B',  \
              sep='')
        if Number != 0.000:
            Check2 = True
        Check3 = False
        continue

    Check2 = False
 
    if spacesToOX == 0:
        spacesAfterOX = size - spaces + 5 - spacesCounter + 5 - (4 - 5)
        if i % 2 == 0:
            print(' ' * spaces, '*', ' ' * spacesAfterOX, round(Number, 3), \
                  sep='')
        else:
            print(' ' * spaces, '*')
        continue



    if spacesToOX > spaces:
        if spaces == 0:
            spaces = 1
        spacesDiff = spacesToOX - spaces - 1
        spacesAfterOX = size - spacesToOX + 3 - spacesCounter + 6 \
                        - (4 - 5)
        print(' ' * (spaces - 1), '*', ' ' * spacesDiff, '┃', \
                ' ' * spacesAfterOX, round(Number,3), sep='' )

    if spacesToOX == spaces:
        spacesDiff = size - spaces + 3 - spacesCounter + 6 - (4 - 5)
        print(' ' * (spacesToOX - 1)  , '*', ' ' * spacesDiff, \
                round(Number,3), sep='')


    if spacesToOX < spaces:
        spacesDiff = spaces - spacesToOX - 1
        spacesAfterOX = size - spaces - spacesCounter + 5  + 5
        print(' ' * (spacesToOX - 1) ,'┃', ' ' * spacesDiff, \
                  '*', ' ' * spacesAfterOX, round(Number,3), sep='')

if spacesToOX > 0:
    print(' ' * (spacesToOX - 1) , '▼', sep='')
    print(' ' * (spacesToOX - 1), 'X', sep='')

