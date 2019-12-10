# Romanov Alexey IU-7 13B. Programm 2. Вариант 7

M = int(input('Введите размер квадратной матрицы: '))
R = [0] * M
for i in range(M):
    print(i)
    R[i] = [0] * M

for j in range(M // 2):
    for k in range(N):
        R[j][k] = (N * N // 2) + 3
        R[k][j] = (N * N // 2) - 1
        

