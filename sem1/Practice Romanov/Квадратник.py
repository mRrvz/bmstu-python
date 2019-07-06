'''

*** Задача:

На вход программа получает текстовый файл, в котором содержатся
множества точек, которые содержат линии, соединяющие смежные точки.
Нужно подсчитать количество и размер квадратов, которые образуют эти
линии. 

Обозначение переменных: см. программу.

*** Тестовые примеры:
* Файлы:
test1.txt
test2.txt
test3.txt
test4.txt
test5.txt

'''

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

'''

****** Вывод результатов подсчёта ******

Функция info_about_game получает список с данными количества квадратов
и их размере, и выводит их.

* Обозначение переменных:
numb_of_game - номер текущей партии. count_squares_total - подсчёт общего кол-ва
квадратов; string_with_info - строка содержащая всю информацию о текущей партии.

'''


def info_about_game(count_of_squares, canvas, info):
    global numb_of_game
    numb_of_game += 1
    count_squares_total = 0
    string_with_info = '     Партия № ' + str(numb_of_game) +  '\n\n'
    for i in range(len(count_of_squares)):
        if count_of_squares[i] != 0:
            count_squares_total += 1
            string_with_info += str(count_of_squares[i]) \
                                + ' квадрат(а) размером ' + str(i + 1) + '\n'
    if count_squares_total == 0:
        string_with_info += 'Нет составленных квадратов'
    info['text'] = string_with_info


'''' 

****** Построение линий на игровом поле *******

*** Функции:

1. drawing
Функция отвечающая за вывод и построений на игровом поле.
В функцию передаётся ключ-значение матрицы, от которого зависит,
какая функция будет вызвана в дальнейшем (ф-ции 2-4)

* Обозначение переменных:
canvas - полотно; i, j - координаты точки из которой будет рисоваться
линия / точка. LINE_SIZE - размер линий.

2. points
Построение точек на игровом поле (в виде квадрата)

3. horizintal_line
Построение горизонатльных линий на игровом поле

4. verticale_line
Построение вертикальных линий на игровом поле

'''


def points(canvas, LINE_SIZE, i, j):
    canvas.create_rectangle(j * LINE_SIZE - 3, i * LINE_SIZE - 3, \
                            j * LINE_SIZE + 3, i * LINE_SIZE + 3, \
                            fill="black", width=3)


def horizontal_line(canvas, LINE_SIZE, i, j):
    canvas.create_line(j * LINE_SIZE, i * LINE_SIZE, LINE_SIZE * j + LINE_SIZE, \
                       i * LINE_SIZE, width=5, fill='blue')


def vertical_line(canvas, LINE_SIZE, i, j):
    canvas.create_line(j * LINE_SIZE, i * LINE_SIZE, LINE_SIZE * j, \
                       i * LINE_SIZE + LINE_SIZE, width=5, fill='blue')


def drawing(matrix, canvas, i, j):
    key = matrix[i][j]
    i += 0.5;
    j += 0.5

    # Размер линий зависит от размера игрового поля:
    if len(matrix) >= 7:
        LINE_SIZE = 50
    elif len(matrix) >= 4:
        LINE_SIZE = 90
    else:
        LINE_SIZE = 110

    # Вывод линий и точек:
    if key == 3:
        horizontal_line(canvas, LINE_SIZE, i, j)
        vertical_line(canvas, LINE_SIZE, i, j)
        points(canvas, LINE_SIZE, i, j)
    elif key == 2:
        horizontal_line(canvas, LINE_SIZE, i, j)
        points(canvas, LINE_SIZE, i, j)
    elif key == 1:
        vertical_line(canvas, LINE_SIZE, i, j)
        points(canvas, LINE_SIZE, i, j)
    else:
        points(canvas, LINE_SIZE, i, j)


'''

****** Запись и обработка матрицы. Подсчёт квадратов. *******

*** Функции:

1. matrix_fill
Заполнение матрицы. Если из условной точки игрового поля (матрицы)
проведена горизонтальная линия - то прибавляем к данной точке два.
Если вертикальная - еденицу. Таким образом, точки из которых 
проведены две линии, будут иметь значение трёх. Точки из которых
нет линий, будут иметь значение ноль.

* Обозначение переменных:
num - переменная содержит положение линии (вертикальное или горизонтальное)
i, j - координаты точки, из которой проведена линия.

2. pass_matrix
Прохождение каждого элемента матрицы. Для каждого элемента запускается
ф-ция drawing (описание см. выше). Если значение элемента равно трём,
запускает функция square_count (описание см. ниже). Т.к. квадрат
может быть образован только из точки, из которой выходит вертикальная
и горизонтальная линия, то есть значение элемента этой точки равно
трём.

3. square_count.
Из просматриваемой точки (координаты передаются из ф-ции pass_matrix)
проверяются наличие сторон, которые должны образовывать квадрат (на 4-х измерениях):
1) Верхняя горизонатль; 2) Нижняя горизонатль
3) Левая вертикаль; 4) Правая вертикаль
Каждый раз проходим эти 4 измерения от начальной координаты, начиная с размера
квадрата 1, 2 ... до максимально возможного размера квадрата
Максимальная сторона вычислеяется в переменной max_square(). Если квадрат не
образуется - переходим к проверке квадрата с размером + 1.

* Обозначение переменных:
i_pos, j_pos - начальные координаты точки, из которой проверяем наличие квадрата
existence_square - переменная значением True / False в зависимости от наличии квадрата
k - начало цикла просмотра наличие квадрата.

'''


def square_count(i_pos, j_pos, matrix, count_of_squares):
    existence_square = False
    k = 0
    max_square = min(len(matrix) - 1 - i_pos, len(matrix) - 1 - j_pos)
    for i in range(max_square):
        for j in range(k, i + 1):
            
            # Просмотр верхней горизонтали:
            if matrix[i_pos][j_pos + j] >= 2:
                pass
            else:
                existence_square = False
                break

            # Просмотр правой вертикали:
            if matrix[i_pos + j][j_pos + i + 1] == 1 \
                    or matrix[i_pos + j][j_pos + i + 1] == 3:
                pass
            else:
                existence_square = False
                break

            # Просмотр нижней горизонатли:
            if matrix[i_pos + i + 1][j_pos + j] >= 2:
                pass
            else:
                existence_square = False
                break

            # Просмотр левой вертекали:
            if matrix[i_pos + j][j_pos] == 1 or matrix[i_pos + j][j_pos] == 3:
                existence_square = True
            else:
                existence_square = False
                break
            k += 1
            
        # Прибавление квадрата, если он прошёл все проверки:
        if existence_square == True:
            count_of_squares[i] += 1


def matrix_fill(lines_count, infile, matrix):
    for k in range(lines_count):
        try:
            num, i, j = infile.readline().split()
        except ValueError:
            continue
        i, j = int(i) - 1, int(j) - 1
        if num == 'H':
            matrix[i][j] += 2
        else:
            matrix[j][i] += 1


def pass_matrix(matrix, count_of_squares, canvas):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            drawing(matrix, canvas, i, j)
            if matrix[i][j] == 3 and i != len(matrix) - 1 \
                    and j != len(matrix) - 1:
                square_count(i, j, matrix, count_of_squares)


'''

****** Создание игрового поля и запуск функции подсчёта квадратов ******
*** Функции: 

1. main
Данный блок программы срабатывает при нажатии клавиши "Запуск программы".
Создаётся новое окно, которое визуализирует задачу и выводит результаты ее выполнения.
После создания окна запускается функция one_game - обработка одной партии.

* Обозначение переменных:

numb_of_game - номер партии. infile - текстовый файл
file_name, root - название текстового файла и корневого окна.
* Настройки root_son:
root_son - новое окно; geomethry, title  - размер и название окна.
maxsize, minsize - макс. и мин. размер окна.
canvas - игровое поле; info - текст. информация о партии 

2, one_game
Одна из ключевых функций, запускающая обработку одной партии.
Вызывает сама себя при нажатии кнопки "Следующая партия",
которую сама и создаёт. Вызывает функции matrix_fill, 
pass_matrix, info_about (описание см. выше). 

* Обозначение переменных: 

line - текущая линия; numb_of_game - текущий номер партии.
matrix, matrix_size - кв. матрица игрового поля и её размер
count_of_squares - пустой список, в которой будут добавляться
результаты подсчётов. lines_count - кол-во строк в партии.
button_go_next - кнопка "Слеудщая партия". Вызывает эту же 
функцию one_game.

'''


def one_game(infile, canvas, info, root_son, button_go_next=None):
    ''' Очищение игрового поля '''
    canvas.delete('all')
    line = infile.readline()
    while line != '\n' and line != '':
        matrix_size = int(line)
        matrix = [[0] * matrix_size for i in range(matrix_size)]
        count_of_squares = [0] * matrix_size
        lines_count = int(infile.readline())

        # Заполнение матрицы:
        matrix_fill(lines_count, infile, matrix)
        # Просмотр заполненной матрицы:
        pass_matrix(matrix, count_of_squares, canvas)
        # Вывод результатов
        info_about_game(count_of_squares, canvas, info)
        line = infile.readline()
        # Создание кнопки "Следующая партия"
        if line != '' and numb_of_game == 1:
            button_go_next = Button(root_son, text='Следующая партия', \
                                    command=lambda: one_game(infile, canvas, \
                                                info, root_son, button_go_next))
            button_go_next.place(x=550, y=400)
        if line == '' and button_go_next is not None:
            button_go_next.place_forget()


def main(file_name, root):
    global numb_of_game
    numb_of_game = 0
    if file_name == '':
        mb.showerror('Ошибка', 'Вы не выбрали файл для работы.')
        return
    else:
        infile = open(file_name)

    ''' Настройка окна игрового поля. '''
    root_son = Toplevel(root, bg='#81F7D8')
    root_son.title('Квадратники. Игровое поле. [УВП №1]')
    root_son.geometry('680x450')
    root_son.maxsize(width=680, height=450)
    root_son.minsize(width=680, height=450)
    canvas = Canvas(root_son, width=450, height=450, bg='#81BEF7')
    canvas.pack(anchor=W)
    info = Label(root_son, text='', font='Garamond 12', bg='#81F7D8')
    info.place(x=465, y=20)
    one_game(infile, canvas, info, root_son)


'''

****** Создание корневого графического окна, кнопок и надписей. ******

*** Обозначение переменных:

root - корневое граф. окно; infile - название файла для работы.
bg_label - текстовая метка для вывода фона. bg_image - фон корневого окна.
root.maxsize; root.minsize - макс. и мин. размер окна.
root.title, root.geometry название окна и размер окна.
info_about - информация о программе.

*** Кнопки:

button1 - Запустить программу
button2 - Выбрать текстовый файл
button3 - О программе
button_exit - Выйти из программы
button_menu - Вернуться в меню

*** Функции:

1. about_programm - вызывается при нажатии на клавишу "О программе" (button3).
Суть функции: делает невидимыми 4 кнопки из главного меню из-за место
них показывает текстовое поле с информацией о программе.
Так же делает видимой кнопку "Вернуться в меню" (button_menu).

2. back_to_menu - вызывается при нажатии на кнопку "Вернуться в меню" (button_menu)
Суть функции: делает видимыми 4 клавиши главного меню, скрывает текст и
клавишу "Вернуться в меню".

3. choice_file - вызывается при нажатии клавиши "Выбрать файл для работы" (button2)
Суть функции: вызывает диалоговое окно выбора текстового файла. В случае выбора
НЕ текстового файла, окно вызывается снова. При повторном выборе файла, предыдущий
закрывается.

'''


def choice_file(infile):
    global file_name
    if infile != '':
        infile.close()
    while True:
        file_name = fd.askopenfilename()
        if file_name == '':
            return
        if (file_name[len(file_name) - 4:]) != '.txt':
            mb.showerror('Ошибка', 'Вы выбрали не текстовый файл.')
        else:
            return


def back_to_menu():
    # Скрытие, показ кнопок и текста.
    button_menu.pack_forget()
    info_about.pack_forget()
    button1.pack(ipady=5, pady=12)
    button2.pack(ipady=5, pady=12)
    button3.pack(ipady=5, pady=12)
    button_exit.pack(ipady=5, pady=12)


def about_programm():
    # Скрытие, показ кнопок и текста.
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button_exit.pack_forget()
    info_about.pack(pady=50)
    button_menu.pack(ipady=5, pady=5)


''' Создаём корневое окно настраем его '''

root = Tk()
file_name = ''
infile = ''
bg_image = PhotoImage(file='bg_main.png')
bg_label = Label(image=bg_image)

button1 = Button(root, text= \
    'Запустить программу', width=21, bg='#58ACFA', \
                 command=lambda: main(file_name, root))

button2 = Button(root, text= \
    'Выбрать файл для работы', bg='#58ACFA', command=lambda: choice_file(infile))

button3 = Button(root, text= \
    'О программе', width=21, bg='#58ACFA', command=about_programm)

button_exit = Button(text= \
                         'Выйти', width=21, bg='red', command=exit)

button_menu = Button(text= \
                         'Вернуться в меню', width=21, bg='#58ACFA', command=back_to_menu)

info_about = Label(text= \
                       'Данная программа подсчитывает количество\nквадратов \
на игровом поле и их размер.\nКвадраты на игровом поле задаются линиями\n\
проведенными из смежных точек игрового поля.', bg='#A9F5E1')

label = Label(root, text='by Alexey Romanov\nIU7-13', \
              justify='right', bg='#013ADF')

# Настройка окна и кнопок:

bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root.maxsize(width=290, height=450)
root.minsize(width=290, height=450)
root.title('Квадратники [УВП №1]')
root.geometry('290x450')
button1.pack(ipady=5, pady=12)
button2.pack(ipady=5, pady=12)
button3.pack(ipady=5, pady=12)
button_exit.pack(ipady=5, pady=12)
label.place(x=175, y=410)
root.mainloop()
