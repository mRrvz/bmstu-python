# Romanov Alexey IU-7 13B. Programm 1a. Вариант 26

L = int(input('Введите размер массива: '))
R = [0] * L
NUM = []
f = 0
print('Заполните массив R: ')
R[0] = int(input())
max_R = R[0]
NUM += [1]
k = 1
for i in range(1, L):
    R[i] = int(input())
    if R[i] > max_R:
        max_R = R[i]
        NUM = []
        k = 1
        NUM += [i + 1]
    elif R[i] == max_R:
        NUM += [i + 1]
        k += 1
print('Исходный массив R: ', end=' ')
for i in range(L):
    print(R[i], end=' ')
print('\nПолученный массив NUM: ', end=' ')
for j in range(k):
    print(NUM[j], end=' ')
if k != L:
    NUM = [0] * (L - k)
    print('\nСжатый массив R: ', end=' ')
    for i in range(L):
        
        if R[i] != max_R:
            NUM[f] = R[i]
            f += 1
    R = []
    R += NUM
    for j in range(L-k):
        print(R[j], end=' ')
else:
    print('\nВсе элементы одинаковые.')
