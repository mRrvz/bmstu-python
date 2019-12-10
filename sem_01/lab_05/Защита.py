A = list(map(int, input('Введите элементы массива A: ').split()))
B = list(map(int, input('Введите элементы массива B: ').split()))
C = list(map(int, input('Введите элементы массива C: ').split()))

strWithNumbers = ''; k = 0

for i in range(len(A)):
    if (A[i] in B) or (A[i] in C):
        k += 1
    else:
         strWithNumbers += ''.join(str(A[i]) + ' ')

if k == len(A):
    print('\nНет элементов, которые содержатся в массиве А, \
но которые не содержатся в массивах B и С.')
else:
    print('\nЭлементы, которые есть в массиве А, но которых нет \
в массивах B и С:  \n', strWithNumbers, sep='')    
