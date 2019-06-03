
def matrix(B):
    numb_RMN_str = 0; k = 0
    while numb_RMN_str < M - k:
        if ('a' <= B[numb_RMN_str][0][0] <= 'z'):
            numb_RMN_str += 1
            continue 
        else:
            del B[numb_RMN_str]
            k+= 1

    for i in range(M-k):
        for j in range(M-k-1):
            if B[j][0][0] > B[j+1][0][0]:
                B[j], B[j+1] = B[j+1], B[j]

M, L = map(int, input('Введите кол-во строк и столбцов исходной матрицы: ').\
           split())

D = []

print('\nВведите исходну матрицу (построчно): ')
for i in range(M):
    D.append([])
    D[i] = list(map(str, input().split()))

print('\nИсходная матрица: \n')
for string in D:
    print(string)
    print()
    
matrix(D)

if D != []:
    print('\nИзмененная матрица: \n')
    for string in D:
        print(string)
        print()
else:
    print('В матрице нет строк, начинающихся с маленькой латинской буквы.')
