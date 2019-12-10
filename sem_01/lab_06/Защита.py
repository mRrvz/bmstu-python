C = []; N = 5; A = [0] * 5; maxim = 0
print('Введите матрицу C(5,5): ')
for i in range(N):
    C.append([])
    C[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        A[i] += C[j][i]
        print(str(C[i][j]).rjust(3), end='')
    print()

for i in range(N):
    print('\nСреднее арифметическое', i+1, 'столбца:', (A[i] / N))
    if (A[i] / N) > maxim:
        maxim = A[i] / N
        j = i + 1

print('\nНаибольшая среднее арифметическое у', j, 'столбца.')
print('Среднее арифметическое равно', maxim)
        
        
