'''

**** Задача №2
Романов Алексей ИУ7 13Б
Вариант 3


'''
Flag = False; counts_now = 0; counts_all = 0
index_elem = -1; index_del = -1
def print_matrix(matrix):
    for i in range(K):
        for j in range(M):
            try:
                print(matrix[i][j].rjust(3), end ='')
            except:
                break
        print()

K = int(input('Введите количество строк исходной матрицы: '))
M = int(input('Введите количество столбцов исходной матрицы: '))

matrix = [M * [0] for i in range(K)]

print('\nВведите исходну матрицу (построчно): ')
for i in range(K):
    matrix[i] = list(map(str, input().split()))

print('\nИсходная матрица:')
print_matrix(matrix)

element = input('\nВведите новую букву: ')

for i in range(K):
    if i % 2 == 0:
        for j in range(M-1):
            if matrix[i][j] > element and Flag == False:
                temp = matrix[i][j]
                matrix[i][j] = element
                Flag = True
                index_elem = i
            if Flag == True:
                if j == 0 and i != index_elem:
                    matrix[i][j], temp = temp, matrix[i][j]
                matrix[i][j+1], temp = temp, matrix[i][j+1]
    else:
        for j in range(M-1, 0, -1):
            if matrix[i][j] > element and Flag == False:
                temp = matrix[i][j]
                matrix[i][j] = element
                Flag = True
            if Flag == True:
                if j == M-1:
                    matrix[i][j], temp = temp, matrix[i][j]
                matrix[i][j-1], temp = temp, matrix[i][j-1]
            
print('\nПреобразованная матрица после вставки буквы "' + element+'":')
print_matrix(matrix)

for i in range(K):
    counts_now = 0
    for j in range(M):
        if matrix[i][j] == 'а' or matrix[i][j] == 'е' or matrix[i][j] == 'и' \
           or matrix[i][j] == 'о' or matrix[i][j] == 'у' \
           or matrix[i][j] == 'ы'or matrix[i][j] == 'э' \
           or matrix[i][j] == 'ю' or matrix[i][j] == 'я':
            counts_now += 1
    if counts_now > counts_all:
        counts_all = counts_now
        index_del = i

if index_del != -1:
    matrix.pop(index_del)

    print('\nПреобразованная матрица после удаление строки, \
    содержащей макс. кол-во гласных букв:')
    print_matrix(matrix)

else:
    print('\nНет строк, содержащие гласные буквы.')

            
        
