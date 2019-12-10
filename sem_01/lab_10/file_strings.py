''''

Задача:

Обозначение переменных:

Тестовые примеры:

'''


'''
******** Функции отвечающие за команды, выбираемые в меню ********
'''

'''*** Подфункции команды 4 ***'''

# Вывод "шапки", "ног" и "тела" таблицы.

def drawing_head():
    print('┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓\n'
          '┃ Язык программирования ┃         Категория          ┃ Популярность (1-5) ┃\n'
          '┣━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━┫')

def drawing_footer():
    print('┗━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━┛')

def drawing_table(file):
    drawing_head()
    for line in file:
        list_line = line.split()
        print('┃ {:21s} ┃ {:26s} ┃         {:10s} ┃'. \
              format(list_line[0], list_line[1], list_line[2]))
    drawing_footer()

''' *** Подфункции команд 5-6 *** '''

# Подфункция функю view_all_strings, ищущая строки, подходящие условию.

def strings_finder(line, find_fields):
    finded_strings = []; k = 0
    for j in range(len(line)):
        if line[j] == find_fields[k]:
            k += 1
        else:
            k = 0

        if k == len(find_fields) and \
                (j + 2 == len(line) or line[j + 1] == ' '):
            finded_strings.append(line)
            k = 0
            break
        elif k == len(find_fields):
            k = 0

    return finded_strings

# Просмотр всех строк и вызов функции strings_finder.

def view_all_strings(find_fields, file):
    finded_strings = []
    for line in file:
        finded_strings += strings_finder(line, find_fields[0])
    if len(find_fields) != 1:
        finded_strings_fin = []
        for i in range(len(finded_strings)):
            finded_strings_fin += \
                strings_finder(finded_strings[i], find_fields[1])
    else:
        finded_strings_fin = finded_strings

    if len(finded_strings_fin) == 0:
        print('Нет записей, содержащие заданные поля.')
    else:
        print('Записи с заданными полями:')

    return finded_strings_fin

# Ввод и обработка искомых полей.

def choice_search_field(string_input, max_len):
    while True:
        find_fields = list(map(str, input('\nВведите ' + string_input\
                                          + ' Вы хотите искать: ').split()))
        if len(find_fields) > max_len or len(find_fields) < max_len:
            print('Вы ввели недопустимое количество полей.')
        else:
            break

    return find_fields

''' *** Подфункции комманд 2-3 *** '''

# Ввод и оработка кол-ва записей очищаемых и/или добавления записей.

def count_strings(string_input):
    while True:
        try:
            count = int(input('\nВведите количество \
записей, которые вы хотите ' + string_input + ': '))
        except ValueError:
            print('Некорректный ввод.')
            continue
        if count < 1:
            print('Некорректное число записей.')
        else:
            return count

''' *** Пункты меню *** '''

# Пункт меню 1: Выбор файла.

def choice_file():
    while True:
        file_name = input('\nВведите название файла: ')
        try:
            open(file_name)
            return file_name
        except:
            print('В дирректории нет такого файла.')

# Пункт меню 2 и 3: Очищение и/или добавление записей.

def records_change(file_name, string_input, argument_file):
    count_strings_add = count_strings(string_input)
    file = open(file_name, argument_file)
    print('Введите', count_strings_add, 'записи (построчно): ')
    for i in range(count_strings_add):
        while True:
            line = input()
            if line.count(' ') != 2 or line[0] == ' ':
                print('Некорректный ввод. Должно быть 3 аргумента: название ЯП, \
категория и оценка популярности.')
            else:
                file.write(line + '\n')
                break
    file.close()

    return menu(file_name)

# Пункт меню 4: Вывод всех записей.

def print_all_set(file_name):
    file = open(file_name)
    drawing_table(file)
    file.close()

    return menu(file_name)

# Пункт меню 5: Поиск по одному заданному полю.

def single_field_search(file_name):
    file = open(file_name)
    need_find_fields = choice_search_field('поле, по которому', 1)
    drawing_table(view_all_strings(need_find_fields, file))
    file.close()

    return menu(file_name)

# Пункт меню 6: Поиск по двум заданным полям.

def two_field_search(file_name):
    file = open(file_name)
    need_find_fields = choice_search_field('поля, по которым', 2)
    drawing_table(view_all_strings(need_find_fields, file))
    file.close()

    return menu(file_name)

''' 
******** Меню и вызов комманд из этого меню ********
'''

def commands_menu(choice, file_name):
    if choice > 1 and file_name is None:
        print('Вы не выбрали файл для работы.')
        return menu(file_name)
    if choice == 0:
        exit()
    elif choice == 1:
        menu(choice_file())
    elif choice == 2:
        records_change(file_name, 'записать', 'w')
    elif choice == 3:
        records_change(file_name, 'добавить', 'a')
    elif choice == 4:
        print_all_set(file_name)
    elif choice == 5:
        single_field_search(file_name)
    else:
        two_field_search(file_name)

def menu(file_name = None):
    print()
    print('МЕНЮ'.rjust(15))
    print('\n1. Выбрать файл. \n'
'2. Создать в файле новый набор записей. \n'
'3. Добавить запись. \n'
'4. Вывести все записи. \n'
'5. Поиск по одному полю.\n'
'6. Поиск по двум полям.\n'
'0. Выход')

    while True:
        try:
            key = int(input('\nВведите пункт из меню: '))
        except ValueError:
            print('Некорректный ввод.')
            continue
        if key > 6 or key < 0:
            print('Вы ввели некорректный пункт.')
        else:
            commands_menu(key, file_name)

menu()


