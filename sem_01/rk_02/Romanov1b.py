# Romanov Alexey IU-7 13B. Programm 1b. Вариант 26

R = list(map(int, input('Введите массив R (в одну строку): ').split()))
NUM = []
for i in range(len(R)):
    if R[i] == max(R):
        NUM.append(i+1)
print('\nИсходный массив R: ', end =' ')
for j in range(len(R)):
    print(R[j], end=' ')
print('\nПолученный масив NUM: ', end =' ')
for i in range(len(NUM)):
    print(NUM[i], end=' ')

if len(NUM) == len(R):
    print('\nВсе элементы одинаковые.')
else:
    print('\nСжатый массив R: ', end=' ')
    for j in range(len(NUM)):
        R.remove(max(R))
    for i in range(len(R)):
        print(R[i], end=' ')
