
def my_sort(A, len_list):
    for i in range(len_list):
        for j in range(len_list-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

A = []

N = int(input('Введите количество размер матрицы: '))

print('Введите матрицу (построчно): ')
for i in range(N):
    A.append([])
    A[i] = list(map(int, input().split()))
    if i == 0:
        list_add = A[i].copy()
    else:
        list_add += A[i]

my_sort(list_add, len(list_add))

def f():
    for q in A:
        print(q)

def break_f():
    if now >= N * N:
        return True
    else:
        return False

#A = [[5,3,6], [1,2,6],[0,9,1]]
k = 0; now = 0
for i in range(N//2+1):
    for j in range(k, N-k):
        A[i][j] = list_add[now]
        now += 1
    if break_f() == True:
        break
    for j in range(k+1, N-k-1):
        A[j][N-k-1] = list_add[now]
        now += 1

    for j in range(N-k-1, k-1, -1):
        A[N-k-1][j] = list_add[now]
        now += 1
    for j in range(N-k-2, k, -1):
        A[j][k] = list_add[now]
        now += 1
    k += 1

print('Преобразованная матрица: ')
for i in range(N):
    for j in range(N):
       print(str(A[i][j]).rjust(3), end = ' ')
    print()




