def drawing_head():
    print('┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n'
          '┃       Тип стола      ┃    Длина (в см.)     ┃   Ширина (в см.) ┃\n'
          '┣━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫')

def drawing_footer():
    print('┗━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛')

def drawing_body(list_line, line):
    print('┃ {:20s} ┃         {:12s} ┃       {:10s} ┃'. \
              format(list_line[0], list_line[1], list_line[2]))
    
file = open('table.txt')
print('Список столов: ')
drawing_head()

for line in file:
    list_line = line.split()
    drawing_body(list_line, line)

drawing_footer()

file.close()

file = open('table.txt')

material, min_square = input('Введите материал стола и мин. площадь стола: ').split()

print('\nПодходящие для Вас столы:')
drawing_head()

for line in file:
    list_line = line.split()
    if list_line[0] == material and \
       (int(list_line[1]) * int(list_line[2]) >= int(min_square)) :
        drawing_body(list_line, line)
    
drawing_footer()
