import time
import numpy
import random
start_time = time.time()

def print_array():
    print(A)
    print("--- %s seconds ---" % (time.time() - start_time))


def new_array():
    return numpy.random.randint(100, size=10)


''' Сортировка пузырьком '''

def bubble_sort():
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j + 1] < A[j]:
                A[j + 1], A[j] = A[j], A[j + 1]


''' Сортировка вставками '''

def insert_sort():
    for i in range(1, len(A)):
        j = i - 1
        key = A[i]
        while key < A[j] and j >= 0:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


''' Сортировка простым выбором '''

def sort_easy_choice():
    for i in range(len(A)):
        min_numb = A[i]; index_min = i
        for j in range(i, len(A)):
            if A[j] < min_numb:
                min_numb = A[j]
                index_min = j
        A[i], A[index_min] = A[index_min], A[i]


''' Шейкерная сортировка '''

def shaker_sort():
    left = 0; right = len(A)-1
    while left <= right:
        for i in range(left, right):
            if A[i] > A[i+1]:
                A[i+1], A[i] = A[i], A[i+1]
        right -= 1

        for i in range(right, left, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
        left +=1


''' Сортировка Шелла '''

def shell_sort():
    d = len(A) // 2
    while d >= 1:
        for i in range(d):
            for j in range(i + d, len(A)-d+1, d):
                k = j - d
                key = A[j]
                while key < A[k] and k >= 0:
                    A[k + d] = A[k]
                    k -= d
                A[k + d] = key
        d = d // 2


''' Быстрая сортировка '''

def qsort(A):
    less = []
    more = []
    equal = []

    if len(A) > 1:
        pivot = random.choice(A)
        for i in range(len(A)):
            if A[i] > pivot:
                more.append(A[i])
            elif A[i] < pivot:
                less.append(A[i])
            else:
                equal.append(A[i])

        return qsort(less) + equal + qsort(more)
    else:
        return A


''' Сортировка пузырьком с барьерром '''

def bubble_sort_barrier():
    for i in range(len(A)):
        b = True
        for j in range(len(A)-1):
            if A[j+1] < A[j]:
                A[j+1], A[j] = A[j], A[j+1]
                b = False
        if b:
            break


array_main = new_array()

print('Сортировка пузырьком:')
A = array_main.copy()
bubble_sort()
print_array()
start_time = time.time()

print('Сортировка вставками: ')
A = array_main.copy()
insert_sort()
print_array()
start_time = time.time()

print('Сортировка вставками + бинарный поиск:')
A = array_main.copy()
for i in range(1, len(A)):
    key = A[i]; left = -1; right = i
    while left < right -1:
        mid = (left + right) // 2
        if A[mid] >= key:
            right = mid
        else:
            left = mid
    for j in range(i, right , -1):
        A[j] = A[j - 1]
    A[right] = key
print_array()
start_time = time.time()

print('Сортировка простым выбором: ')
A = array_main.copy()
sort_easy_choice()
print_array()
start_time = time.time()

print('Шейкерная сортировка:')
A = array_main.copy()
shaker_sort()
print_array()
start_time = time.time()

print('Сортировка Шелла:')
A = array_main.copy()
shell_sort()
print_array()
start_time = time.time()

print('Быстрая сортировка:')
A = array_main.copy()
A = qsort(A)
print_array()
start_time = time.time()


print('Пузырьковая сортировка с барьером:')
A = array_main.copy()
bubble_sort_barrier()
print_array()