'''

Задача: Выполнение действий над текстом, выбираемых пользователем.
Действия выбираются в меню; всего действий 7
1) Выравнивание исходного текста по ширине.
2) Выравнивание исходного текста по левому краю.
3) Выравнивание исходного текста по правому краю.
4) Замена слова в тексте.
5) Удаление слова в тексте.
6) Замена арифм. выражений с умножением и делением на их рез-тат.
7) Индивидуальное задание.

Обозначение переменных:
text_matrix, text_list - исходная матрица и исходный список
list_symbols array_check - рабочие списки
max_len, max_len_without_spaces - максимальная длина строки c / без пробелов
count - рабочая переменная
curr_string, len_string - текущая строка и ее длинна
item, key - значения отвечающиее за выбор пункта в меню
expression, type_actions - локальные переменные функции арифметика
check, Flag - рабочие флаги
string_temp, current - текущая отформатированная строка / число (функция арифм.)
DivisionZero - флаг присутствия деления на ноль
start - переменная обозначающая начало цикла
temp_spaces, temp_spaces_remain, add_spaces - лок. перем. для формат. текста

Тестовые примеры:
1) При вызове 1 пунта: расширение текста
2) При вызове 2 пункта: удаление всех пробелов слева
3) При вызове 3 пункта: добавляются пробелы слева
4) При вызове 4 пункта: замена слова
5) При вызове 5 пункта: удаление слова
6) При вызове 6 пункта: преобразование арифм. выраж.

'''

# Инициализация и заполнение матрицы

text_list = [' ааkhjhjhjhа',\
             '    aaaaааа ',\
             'sssssssssss qqqqааааааааффф.',
            'jhhjhjg jhjhh jhnjh.']
'''
             'Кафедра «Программное обеспечение кафедра ЭВМ и информационные',\
             'технологии» была организована в 1989 году. К этому ', \
             'времени в передовых областях науки и промышленности уже', \
             'сформировалась серьезная  потребность в использовании бурно', \
             'развивавшихся информационных технологий на базе средств', \
             'вычислительной техники. Перед кафедрой была поставлена', \
             'задача теоретически и практически знакомить всех студентов', \
             'университета с возможностями применения компьютеров в будующей',\
             'профессиональной деятельности выпускников. Однако уже через', \
             'год кафедра стала выпускающей. Она начала готовить', \
             'высококвалифицированных специалистов в области разработки', \
             'сложных системных и прикладных программных комплексов,', \
             'информационных систем и баз данных. Настоящее время кафедра',\
             'готовит как бакалавров, магистров, так дипломированных', \
             'специалистов инженеров специальности 2204 «Программное',\
             'обеспечение вычислительной техники автоматизированных', \
             'систем» продолжая обучать практически всех первокурсников', \
             'университета основам информатики.']
'''
text_matrix = []; list_symbols = [' ', '*', '/']
text_local = []; 
max_len = 0; max_len_without_spaces = 0
DivisionZero = False; Flag = False
check_array = [0, 5]
array_check = [' ', ',', '!', '?', '"',"'",'[',']','(',')','{','}']

def text():
    print('Исходный текст:\n')
    for j in range(len(text_matrix)):
        print(text_matrix[j][0])

def spaces_to_1st_symbol(curr_string):
    count = 0
    for j in range(len(curr_string)-1):
        if curr_string[j] == ' ':
            count += 1
        if curr_string[j+1] != ' ':
            return count
        
def parsing_text(curr_sring, i):
    global temp_string
    #curr_string = text_matrix[i][0]
    if i != 0:
        temp_string += ' '
    for j in range(len(curr_string)):
        if curr_string[j] != '.':
            temp_string += curr_string[j]
        else:
            text_local.append(temp_string)
            temp_string = ''
    return
    #print(curr_string)
    #curr_string = text_matrix[i][0]

# Заполнение матрицы

for i in range(len(text_list)):
    text_matrix.append([])
    text_matrix[i].append(text_list[i])
    count = 0; curr_string = text_matrix[i][0]

    for j in range(len(curr_string)-1):
        count_to_1st = spaces_to_1st_symbol(curr_string)
        
        if curr_string[j] != ' ':
            count += 1
        if curr_string[j] == ' ' and curr_string[j+1] != ' ':
            count += 1
        if DivisionZero == False:
            if '/ 0' in curr_string:
                DivisionZero = True

    if (len(curr_string) - count_to_1st) > max_len:
        max_len = len(curr_string) - count_to_1st

    if count > max_len_without_spaces:
        max_len_without_spaces = count



# Функция повторного вызова меню

def repeat_menu():
    print('\n1. Вызвать меню.')
    print('\n0. Выход.\n')

    item = check_item_existence(1)

    if item == 1:
        menu()
    else:
        exit()

# *** Подфункции для функций ***

# Функция - пустая строка

def empty_line():
    print()

# Подсчёт пробелов справа

def spaces_right(curr_string):
    if curr_string[len(curr_string) - 1] == ' ':
        return 1
    else:
        return 0

# Объявление функции подсчёта. арифм. выражений

def arithmetic(curr_string, j):
    current = ''; type_actions = 'multip'; expression = 1

    while curr_string[j].isdigit() or curr_string[j] in list_symbols:

        # Рассмотр случая с умножением

        if curr_string[j] == '*':
            if type_actions == 'multip':
                expression *= float(current)
            else:
                expression /= float(current)
            current = ''; type_actions = 'multip'

        # Рассмотр случая с делением

        elif curr_string[j] == '/':

            if type_actions == 'multip':
                expression *= float(current)
            else:
                expression /= float(current)
            current = ''; type_actions = 'division'

        # Обработка пробела в арифм. выражении

        elif curr_string[j] != ' ':
            current += curr_string[j]
        j += 1
        if j >= len(curr_string):
            break

    # Конечная обработка строки с числом и вывод

    if type_actions == 'multip':
        expression *= float(current)
    else:
       expression /= float(current)

    if expression == round(expression):
        expression = int(expression)

    print(round(expression, 4), end = ' ')
    return (j - 1)

# Подфункция функции выравнивания по ширине

def count_spaces_add(curr_string, len_string):
    k = 0; start = 0; j = 0; spaces_count = 0
    count_spaces_right = spaces_right(curr_string)
    
    if curr_string[0] == ' ':
        start = spaces_to_1st_symbol(curr_string)
    spaces_add = max_len - len_string + start

    # Вычисление кол-во "интервалов" из пробелов

    for j in range(start, len_string - 1):
        if curr_string[j] == ' ' and curr_string[j+1] != ' ':
            k += 1
        if curr_string[j] == ' ':
            spaces_count += 1

    spaces_all = spaces_count + spaces_add
    return spaces_all // k,(spaces_all % k) + count_spaces_right, start

# *** Объявление функций-проверок вводимых данных ***

# Проверка на более одного введённого слова:

def word_count_check(string, key):
    word_to_replace = input('\nВведите слово ' + string)
    if ' ' in word_to_replace:
        print('Вы ввели более одного слова.')
        return word_count_check(string, key)
    if key == 0:
        return word_existence_check(word_to_replace, string)
    else:
        return word_to_replace

# Проверка на существование слова в тексте

def word_existence_check(word_to_replace, string):
    key = 0; check = False

    if word_to_replace == '':
        print('Вы ничего не ввели.')
        return word_count_check(string, key)

    for i in range(len(text_matrix)):
        curr_string = text_matrix[i][0]
        if check == True:
            break
        k = 0
        for j in range(len(curr_string)):
            if curr_string[j] == word_to_replace[k]:
                k += 1
            else:
                k = 0

            if k == len(word_to_replace):
                try:
                    if curr_string[j + 1] in array_check:
                        check = True
                        break
                    else:
                        k = 0
                        continue
                except IndexError:
                    check = True
                    break

    if k < len(word_to_replace):
        print('Данного слова нет в исходном тексте.')
        return word_count_check(string, key)

    return(word_to_replace)

# Проверка ввдённого пункта меню

def check_item_existence(key):
    try:
        item = int(input('Выберите пункт из меню: '))
        if item < 0 or item > key:
            print('Такого пункта нет в меню.\n')
        else:
            return item
    except ValueError:
        print('Некорректный ввод.\n')

    return check_item_existence(key)

# *** Функции из меню ***

# Выравнивание текста по ширине

def text_formatting_width():
    empty_line()

    for i in range(len(text_matrix)):
        curr_string = text_matrix[i][0]; len_string = len(curr_string)
        string_temp = ''
        temp_spaces, temp_spaces_remain, start = \
                     count_spaces_add(curr_string, len_string)

        # Постепенное добавление пробелов

        for j in range(start, len_string):
            if curr_string[j] != ' ':
                string_temp += curr_string[j]
                check = True

            elif curr_string[j] == ' ' and check == True:
                string_temp += (' ' * temp_spaces)
                if temp_spaces_remain != 0:
                    temp_spaces_remain -= 1
                    string_temp += ' '
                check = False
        print(string_temp)

    return repeat_menu()

# Выравнивание текста по левому краю

def text_formatting_left():
    empty_line()

    for i in range(len(text_matrix)):
        check = False; string_temp = ''
        curr_string = text_matrix[i][0]; len_string = len(curr_string)

        # Удаление пробелов слева

        start = spaces_to_1st_symbol(curr_string)
        for k in range(start, len_string):
            if curr_string[k] != ' ':
                string_temp += curr_string[k]
                check = True
            if curr_string[k] == ' ' and check == True:
                string_temp += ' '
                check = False
        print(string_temp)

    return repeat_menu()

# Выравнивание текста по правому краю

def text_formatting_right():
    empty_line()

    for i in range(len(text_matrix)):
        count = 0; string_temp = ''; check = False
        curr_string = text_matrix[i][0]; len_string = len(curr_string)
        start = spaces_to_1st_symbol(curr_string)
        count_spaces_right = spaces_right(curr_string)

        for k in range(start, len_string-1):
            if curr_string[k] != ' ':
                count += 1
            elif curr_string[k] == ' ' and curr_string[k+1] != ' ':
                count += 1
        N = max_len_without_spaces - count + count_spaces_right

        # Постепенное добавление пробелов слева

        for j in range(N):
            string_temp += ' '

        # Формирование строки

        for k in range(len_string):
            if curr_string[k] != ' ':
                string_temp += curr_string[k]
                check = True
            elif curr_string[k] == ' ' and check == True:
                string_temp += ' '
                check = False
        print(string_temp)

    return repeat_menu()

# Замена слова

def text_formatting_word_replacement(word_to_replace, word_replacement):
    empty_line()

    for i in range(len(text_matrix)):
        curr_string = text_matrix[i][0]
        temp_string = ''
        if word_to_replace in curr_string:
            k = 0; start = 0
            for j in range(len(curr_string)-1):
                if curr_string[j] == word_to_replace[k]:
                    k += 1

                else:
                    k = 0
                
                if k == len(word_to_replace) \
                and curr_string[j+1] in array_check and curr_string[j-1] \
                in array_check:
                    temp_string += curr_string[start:j-k+1] + word_replacement
                    start = j+1
                    k = 0
                if k == len(word_to_replace) \
                and (curr_string[j+1] not in array_check \
                     or curr_string[j-1] not in array_check):
                    k = 0
            temp_string += curr_string[start:len(curr_string)]
            print(temp_string)
        else:
            print(curr_string)
    return repeat_menu()

# Удаление слова

def text_formatting_word_to_delete(word_to_delete):
    empty_line()

    for i in range(len(text_matrix)):
        curr_string = text_matrix[i][0]
        temp_string = ''
        if word_to_delete in curr_string:
            k = 0; start = 0
            for j in range(len(curr_string)-1):
                if curr_string[j] == word_to_delete[k]:
                    k += 1
                else:
                    k = 0
                
                if k == len(word_to_delete) \
                and curr_string[j+1] in array_check and curr_string[j-1] in array_check:
                    temp_string += curr_string[start:j-k+1]
                    start = j+1
                    k = 0
                if k == len(word_to_delete) \
                and (curr_string[j+1] not in array_check or curr_string[j-1] not in array_check):
                    k = 0
            temp_string += curr_string[start:len(curr_string)]
            print(temp_string)
        else:
            print(curr_string)
    return repeat_menu()

# Преобразование арифм. выражений

def text_formatting_arithmetic_expressions():
    empty_line()

    if DivisionZero == True:
        print('В тексте присутствует деление на ноль.')
        return repeat_menu()

    for i in range(len(text_matrix)):
        curr_string = text_matrix[i][0]; len_string = len(curr_string)
        temp_string = ''; j = 0

        # Рассмотр случая, если в строке есть знаки / или *

        if '/' in curr_string or '*' in curr_string:
            while j < len_string:
                Flag = curr_string[j].isdigit()
                if Flag == True:
                    print(temp_string, end = '')
                    temp_string = ''
                    j = arithmetic(curr_string, j)    # Вызов ф-ции обрабат. рез-тат.
                else:
                    temp_string += curr_string[j]
                j += 1
            print(temp_string)

        else:   # Если в строке нет / или *
            print(curr_string)

    return repeat_menu()

# Индивидуальное задание

def func7():
    text()
    maxcount = 0; count = 0;
    temp_string = '';
    text_local = []
    for i in range(len(text_matrix)):
        curr_string = text_matrix[i][0]
        if i != 0:
            temp_string += ' '
        for j in range(len(curr_string)):
            if curr_string[j] != '.':
                temp_string += curr_string[j]
            else:
                text_local.append(temp_string + '.')
                temp_string = ''
                
    for i in range(len(text_local)):
        count = 0
        for j in range(len(text_local[i])):
            if text_local[i][j] != ' ':
                count += 1
            else:
                count = 0
            
        if count > maxcount:
            maxcount = count
            index_need = i
        
    print('Предложение с самым длинным словом: \n')
    k = 1
    for i in range(len(text_local[index_need])// 79):
        print((text_local[index_need])[k:k+79])
        k += 79
        
    return repeat_menu()

def func8():
    text()
    text_local = []
    words = ['А', 'е', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    finn = []; temp_string =''
    for i in range(len(text_matrix)):
        curr_string = text_matrix[i][0]
        if i != 0:
            temp_string += ' '
        for j in range(len(curr_string)):
            if curr_string[j] != '.':
                temp_string += curr_string[j]
            else:
                text_local.append(temp_string)
                temp_string = ''

    for i in range(len(text_local)):
        spaces = 0
        count = 0
        for j in range(0, len(text_local[i])-1, 2):
            if text_local[i][j] != ' ':
                if (text_local[i][j] in words and text_local[i][j+1] \
                    not in words) or (text_local[i][j] not \
                                      in words and text_local[i][j+1] in words): 
                    count += 2
            else:
                spaces += 1
    if len(check_array) >= 0:
        print('\nПредложения, в которых во всех словх гласные чередуются с согласными: \n')
        for i in range(len(text_local)):
            if i in check_array:
                print(text_local[i])

def func9():
    text()
    temp_string = ''; text_local = []
    for i in range(len(text_matrix)):
        curr_string = text_matrix[i][0]
        temp_string += ' '
        for j in range(len(curr_string)):
            if curr_string[j] != '.':
                temp_string += curr_string[j]
            else:
                text_local.append(temp_string + ' ')
                temp_string = ''
                
    len_words_min = 21; fin_index = 0
    fin_word = ''; count_words_max = 0
    word_min = ''
    for i in range(len(text_local)):
        count_words = 0; len_words = 0; word = ''; len_words_min = 21
        for j in range(len(text_local[i])-1):
            if text_local[i][j] == ' ' and text_local[i][j+1] != ' ':
                count_words += 1
                word = ''
                len_words = 0
            elif text_local[i][j] != ' ':
                word += text_local[i][j]
                len_words += 1
            if text_local[i][j] != ' ' and text_local[i][j+1] == ' ' and len_words < len_words_min:
                len_words_min = len_words
                word_min = word
                word = ''
        if count_words > count_words_max:
            count_words_max = count_words
            fin_index = i
            fin_word = word_min
        
    print('\nМаксимальное предложение:\n', (text_local[fin_index])[1:], '\nСамое короткое слово в нём:\n', fin_word, sep ='')
                
            

# Объявление функции вызывающей функции меню

def calling_func(item):
    if item == 0:
        exit()

    elif item == 1:
        return text_formatting_width()

    elif item == 2:
        return text_formatting_left()

    elif item == 3:
        return text_formatting_right()

    elif item == 4:
        string = 'которое вы хотите заменить: '; string1 = 'замену: '
        word_to_replace = word_count_check(string, 0)
        word_replacement = word_count_check(string1, 1)
        return text_formatting_word_replacement(word_to_replace, \
                                                word_replacement)

    elif item == 5:
        string = 'которое вы хотите удалить: '
        word_to_delete = word_count_check(string, 0)
        return text_formatting_word_to_delete(word_to_delete)

    elif item == 6:
        return text_formatting_arithmetic_expressions()

    elif item == 7:
        return func7()

    elif item == 8:
        return func8()
    else:
        return func9()
# Объявление функции меню

def menu():
    empty_line()
    text()
    empty_line()
    
    print('{:^20s}'.format('Меню:'))
    print('1. Выравнивание текста по ширине. ')
    print('2. Выравнивание текста по левому краю.')
    print('3. Выравнивание текста по правому краю.')
    print('4. Замена во всем тексте одного слова другим.')
    print('5. Удаление заданного слова из текста.')
    print('6. Заменить арифметические выражения состоящие \
из умножения и деления на результат их вычисления.')
    print('7. Найти предложение с самым длинным словом.')
    print('8. Найти предложения, в которые гласные буквы чередуются с согласными.')
    print('9. Найти минимальное слово в самом длинном по кол-ву слов предложении.')
    print('0. Выход.\n')

    item = check_item_existence(9)

    return calling_func(item)

# Мейн функция

menu()

