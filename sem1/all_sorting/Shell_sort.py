def print_list():
    for i in range(len(A)):
        print('{:4d} '.format(A[i]), end='')
    print()

def sort_Shell(i, k1):
    for k in range(i, len(A)-n, n):
        for j in range(i, len(A)-n, n):
            if A[j+n] < A[j]:
                A[j+n], A[j] = A[j], A[j+n]
            k1 += 1
            print(k1)

def bubble_sort(A, k):
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j+1] < A[j]:
                A[j+1], A[j] = A[j], A[j+1]
                
print('Заполните список: ')
A = list(map(int, input().split()))
n = 1
k1= 0
while n * 2 + 1 <= len(A):
    n = n * 2 + 1

print('\nПромежуточные результаты сортировки.')
while n >= 1:
    for i in range(n):
        sort_Shell(i, k1)
    print('\nПри', n, 'шагах:')
    print_list()
    n = n // 2

print('\nОтсортированный список: ')
print_list()
