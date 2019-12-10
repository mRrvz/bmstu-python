'''
**** Задача 1
Романов Алексей ИУ7 13Б
Вариант 3
'''

string_X = input('Введите строку X: ')
string_Y = input('Введите строку Y: ')
k = 0
print()
print('X - ' + string_X, end =' ') 
for i in range(len(string_Y)):
    if string_Y[i] in string_X:
        delete = string_X.index(string_Y[i])
        string_X = string_X[:delete] + string_X[delete+1:]
        k += 1
    else:
        break

if k == len(string_Y):
    print('    Y - ' + string_Y + ' (можно составить)')
else:
    print('    Y - ' + string_Y + ' (нельзя составить)')
