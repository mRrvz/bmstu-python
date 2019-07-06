#-*- coding: utf -*-

"""

==============================================================================

Python. Лабораторная работа №3. Уточнение корней уравнения.
Метод: комбинированный (хорд и касательных)

Данная программа вычисляет приблизительные корни заданого не линейного уравн.
на заданном интервале и с заданным шагом поиска корней. Данные о найденных
корнях выводится в таблицу. Так же, программа показывает график заданной 
функции, найденные корни, точки перегиба.

График функции:

x^6-24x^5+208x^4-768x^3+1024x^2-10x-400

Разработчик: Романов Алексей ИУ7-23Б

==============================================================================


"""

from matplotlib import mlab
import pylab
from math import *
import numpy as np
from tkinter import *
from tkinter import messagebox as msb


# Информация о программе

def about_program():
    msb.showinfo("Информация о программе", "Данная программа вычисляет приближенное \
значение корней уравнения с помощью комбинированного метода (метод хорд и касательных). \
Пользователь может задать интервал поиска, шаг поиска, точность ε и максимальное \
количество итераций. Все данные выводятся в таблицу. Так же показывается \
график функции, найденных решений и точек перегиба.\n\n\
Разработчк: Романов Алексей, группа ИУ7-23Б")


# Очищение всех лэйблов

def clear_all_labels():
    list_with_all_labels = [label_number, label_interval, \
                label_approximate, label_approximate_func, \
                label_count_iteration, label_code_error]
    
    for labels_list in list_with_all_labels:
        labels_list["text"] = ""
        labels_list["font"] = "Arial 12"


# Поиск значения второй производной

def second_derivative_f(x):
    function = -sin(x)#2
    return function
    #return 30 * (x ** 4) - 480 * (x ** 3) + 2496 * (x ** 2) - 4608 * x + 2048


# Поиск значения первой производной

def derivative_f(x):
    function = cos(x)#2 * x
    return function
    #return 6 * (x ** 5) - 120 * (x ** 4) + 832 * (x ** 3) - 2304 * (x ** 2) + 2048 * x - 10


# Поиск значения f(x)

def f(x):
    function = sin(x)#x * x - 4
    return function
    #return  (x ** 2) * ((x-4) ** 2) * ((x-8) ** 2) - 10 * x - 400
 

# Создание графика

def create_graph(xmin=-1, xmax=9, list_x_approximate=False):
    dx = 0.001
    fig = pylab.gcf()
    fig.canvas.set_window_title("Fuction graph")
    xlist = np.arange(xmin, xmax, dx)
    ylist = [f(x) for x in xlist]
    x_list_OX = np.arange(xmin, xmax, dx)
    y_list_OX = [0 for x in (x_list_OX)]

    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.plot(xlist, ylist, label="f(x)")
    pylab.plot(x_list_OX, y_list_OX) 
    
    if list_x_approximate:
        for i in range(len(list_x_approximate)):
            y = f(list_x_approximate[i])
            if i == 0:
                pylab.scatter(list_x_approximate[i], y, color="red", \
                              label="Solutions")
            else:
                pylab.scatter(list_x_approximate[i], y, color="red")
    
    pylab.legend()
    pylab.title("f(x)")
    pylab.tick_params(labelsize=14)

    pylab.show()


# Обновление лейблов

def update_labels(count_roots, temp_a, temp_b, border, \
                  code_error, count_iterations):
    
    list_with_all_labels = [label_number, label_interval, \
                label_approximate, label_approximate_func, \
                label_count_iteration, label_code_error]
    
    if count_roots > 16:
        for labels in list_with_all_labels:
            labels["font"] = "Arial 5"
    elif count_roots >= 13:
        for labels in list_with_all_labels:
            labels["font"] = "Arial 6"
    elif count_roots >= 10:
        for labels in list_with_all_labels:
            labels["font"] = "Arial 7"
    elif count_roots > 7:
        for labels in list_with_all_labels:
            labels["font"] = "Arial 10"
        
    label_number["text"] += str(count_roots) + "\n\n"
    label_interval["text"] += "[{:.2f}, {:.2f}]" \
        .format(temp_a, temp_b) + "\n\n"
    if int(code_error) == 0:
        label_approximate["text"] += \
        "{:.6f}".format(border) + "\n\n"
        label_approximate_func["text"] += \
        "{:.0e}".format(f(border)) + "\n\n"
    else:
        label_approximate["text"] += "-\n\n"
        label_approximate_func["text"] += "-\n\n"
        
    label_count_iteration["text"] += \
        str(count_iterations) + "\n\n"
    label_code_error["text"] += str(code_error) + "\n\n"


# Комбинированный метод

def combined_method(step, interval_list, epsilon, max_iterations):
    border_a = interval_list[0]
    border_b = interval_list[1]
    list_x_approximate = []
    total_interval = border_b - border_a
    temp_a = border_a
    count_roots = 0

    for i in range(ceil(total_interval / step)):
        temp_b =  temp_a + step
        code_error = "0"
        count_iterations = 1
        try_search = 1

        if temp_b > border_b:
            temp_b = border_b

        if (f(temp_b) * f(temp_a)) < 0:
            count_roots += 1

            while try_search < 3:

                if try_search == 1:
                    left_border = temp_a + ((f(temp_a) * \
                                             (temp_a - temp_b)) / (f(temp_a) - f(temp_b)))
                    right_border = temp_b - (f(temp_b) / derivative_f(temp_b))

                    while abs(right_border - left_border) > epsilon \
                          and count_iterations < max_iterations:
                        left_border = left_border + ((f(left_border) * \
                                                      (right_border - left_border)) / \
                                                     (f(left_border) - f(right_border)))
                        right_border = right_border - (f(right_border) / derivative_f(right_border))
                        count_iterations += 1

                    if temp_a < (right_border + left_border) / 2 < temp_b:
                        break

                else:
                    left_border = temp_a - (f(temp_a) / derivative_f(temp_a))
                    right_border = temp_b + ((f(temp_b) * (temp_b - temp_a)) / (f(temp_b) - f(temp_a)))

                    while abs(right_border - left_border) > epsilon and \
                          count_iterations < max_iterations:
                        right_border = right_border + ((f(right_border) * \
                                                        (right_border - left_border)) \
                                                       / (f(left_border) - f(right_border)))
                        left_border = left_border - (f(left_border) / derivative_f(left_border))
                        count_iterations += 1

                try_search += 1

            if not (temp_a < ((right_border + left_border) / 2) < temp_b):
                code_error = "3"
            else:
                list_x_approximate.append((right_border + left_border) / 2)

            if max_iterations <= count_iterations:
                code_error = "2"

            update_labels(count_roots, temp_a, temp_b, (right_border + left_border) / 2, \
                          code_error, count_iterations)

        temp_a = temp_b

    return list_x_approximate, count_roots


# Метод Хорд

def chord_method(step, interval_list, epsilon, max_iterations):
    border_a = interval_list[0]
    border_b = interval_list[1]
    list_x_approximate = []
    total_interval = border_b - border_a
    temp_a = border_a
    count_roots = 0

    for i in range(ceil(total_interval / step)):
        temp_b = temp_a + step
        code_error = "0"
        count_iterations = 1
        try_search = 1

        if temp_b > border_b:
            temp_b = border_b

        if (f(temp_b) * f(temp_a)) < 0:
            count_roots += 1

            while try_search < 3:

                if try_search == 1:
                    root, root_previous = temp_a, temp_a + 2 * epsilon
                else:
                    root, root_previous = temp_b, temp_b - 2 * epsilon

                while abs(root - root_previous) > epsilon and \
                      count_iterations < max_iterations:
                    root, root_previous = root_previous - f(root_previous) \
                                          / (f(root) - f(root_previous)) * (root - root_previous), root
                    count_iterations += 1

                #print(root, try_search)
                if temp_a < (root) < temp_b:
                    break
                try_search += 1

            if not (temp_a < root < temp_b):
                code_error = "3"
            else:
                list_x_approximate.append(root)

            if max_iterations <= count_iterations:
                code_error = "2"

            update_labels(count_roots, temp_a, temp_b, root, code_error, count_iterations)

        temp_a = temp_b

    return list_x_approximate, count_iterations


# Метод Ньютона

def Newton_method(step, interval_list, epsilon, max_iterations):
    border_a = interval_list[0]
    border_b = interval_list[1]
    list_x_approximate = []
    total_interval = border_b - border_a
    temp_a = border_a
    count_roots = 0

    for i in range(ceil(total_interval / step)):
        temp_b = temp_a + step
        code_error = "0"
        count_iterations = 1

        if temp_b > border_b:
            temp_b = border_b

        if (f(temp_b) * f(temp_a)) < 0:
            count_roots += 1
            try_search = 1

            while try_search < 3:
                count_iterations = 1
                if try_search == 1:
                    x_o = temp_a
                else:
                    x_o = temp_b

                root_previous = x_o - (f(x_o) / derivative_f(x_o))
                root = root_previous - (f(root_previous) / \
                                        derivative_f(root_previous))

                while abs(root - root_previous) > epsilon and \
                      count_iterations < max_iterations:
                    root_previous = root
                    root = root_previous - (f(root_previous) / \
                                            derivative_f(root_previous))
                    count_iterations += 1

                if temp_a < root < temp_b:
                    break

                try_search += 1

            if not (temp_a < (root) < temp_b):
                code_error = "3"
            else:
                list_x_approximate.append(root)

            if max_iterations <= count_iterations:
                code_error = "2"

            update_labels(count_roots, temp_a, temp_b, root, code_error, count_iterations)

        temp_a = temp_b

    return list_x_approximate, count_roots

# Поиск корней

def start_find_roots(step, interval_list, epsilon, max_iterations, method):
    clear_all_labels()

    if method == "Newton":
        list_x_approximate, count_roots = Newton_method(step, \
                                                interval_list, epsilon, max_iterations)
    elif method == "chord":
        list_x_approximate, count_roots = chord_method(step, \
                                                interval_list, epsilon, max_iterations)
    else:
        list_x_approximate, count_roots = combined_method(step, \
                                                interval_list, epsilon, max_iterations)

    if count_roots == 0:
        msb.showerror("Ошибка", "На заданном интервале нет корней.")
    else:
        button_see_graph = Button(root, \
                    text="Показать график функции\n на заданном интервале", \
                    command=lambda:create_graph(interval_list[0], \
                                                interval_list[1], list_x_approximate))
        button_see_graph.place(x=780, y=440, width=160)


# Функция проверки введеных данных в окна ввода

def check_entry(entry_step, entry_interval, entry_epsilon, entry_max_iterations, method):
# Проверка первого окна (количество шагов)
    try:
        step = float(entry_step.get())
    except:
        msb.showerror("Ошибка", "Некорректный ввод шага разбиения \
на интервалы.")
        return

    if step <= 0:
        msb.showerror("Ошибка", "Шаг должен быть больше нуля.")
        return

# Проверка второго окна (интервал)

    interval_list = list(map(float, entry_interval.get().split()))
    if len(interval_list) != 2:
        msb.showerror("Ошибка", "Интервал поиска корней \
должен состоять из двух чисел.")
        return

    if interval_list[0] > interval_list[1]:
        msb.showerror("Ошибка", "Левая граница интервала \
должна быть больше правой границы.")
        return

    interval_list[0] -= 0.001
    interval_list[1] += 0.001
    
# Проверка третьего окна (точность epsilon)

    try:
        epsilon = float(entry_epsilon.get())
    except:
        msb.showerror("Ошибка", "Некорректный ввод точности ε.")
        return

    if epsilon <= 0:
        msb.showerror("Ошибка", "Точность ε должна быть больше нуля.")
        return

# Проверка четвертого окна (количество итераций)
    
    try:
        iterations = int(entry_max_iterations.get())
    except:
        msb.showerror("Ошибка", "Некорректный ввод \
максимального количества итераций.")
        return

    if iterations <= 0:
        msb.showerror("Ошибка", "Максимальное количество \
итераций должно быть нуля. ")
        return

    start_find_roots(step, interval_list, epsilon, iterations, method)


# Настроки корневого окна

root = Tk()
root.geometry("500x100")
root.maxsize(width=1000, height=500)
root.minsize(width=1000, height=500)
root.title("Уточнение корней уравнения смешаным способм")

# Настройка фонового изображения
    
bg_image = PhotoImage(file="bg_image_lab03.png")
label_bg = Label(image=bg_image)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# Создание и настройка меню

mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="О программе", command=about_program)
mainmenu.add_command(label="Показать график функции", command=create_graph)
mainmenu.add_command(label="Выйти", command=exit)

# Лэйблы

label_enter_step = Label(root, text="Введите шаг разбиения на интервалы:")
label_enter_interval = Label(root, text="Введите интервал для поиска корней:")
label_enter_epsilon = Label(root, text="Введите точность ε: ")
label_enter_max_iterations = Label(root, \
                            text="Введите максимальное количество итераций: ")
label_info_about_codes = Label(root, text="Коды выполнения:\n\n0. Метод сошелся\n\n\
1. Превышено максимальное \nкол-во итераций.\n\n2. Метод не сошелся.\n\
\n3. Из-за особенностей графика \nкасательная в одной из точек \nвышла за \
интервалы разбиения.",justify=CENTER,bg="#4682B4", font="Arial 12")

# Вывод лэйблов

label_enter_step.place(x=255, y=8, width=227)
label_enter_interval.place(x=10, y=8, width=227)
label_enter_epsilon.place(x=500, y=8, width=200)
label_enter_max_iterations.place(x=725, y=8, width=260)
label_info_about_codes.place(x=735, y=200, width=250)

# Кнопки

find_roots_newton = Button(root, text="Найти корни (метод Ньютона)", \
        command=lambda:check_entry(enter_step, enter_interval, \
        enter_epsilon, enter_max_iterations, "Newton"))
find_roots_chord = Button(root, text="Найти корни (метод Хорд)", \
        command=lambda:check_entry(enter_step, enter_interval, \
        enter_epsilon, enter_max_iterations, "chord"))
find_roots_combined = Button(root, text="Найти корни (комбинированный метод)", \
        command=lambda:check_entry(enter_step, enter_interval, \
        enter_epsilon, enter_max_iterations, "combined"))

# Вывод кнопок

find_roots_newton.place(x=745, y=150, width=235)
find_roots_chord.place(x=745, y=120, width=235)
find_roots_combined.place(x=745, y=90)

# Поля ввода

enter_step = Entry(root)
enter_interval = Entry(root)
enter_epsilon = Entry(root)
enter_max_iterations = Entry(root)

# Вывод окон полей ввода

enter_step.place(x=255, y=30, width=227)
enter_interval.place(x=10, y=30, width=227)
enter_epsilon.place(x=500, y=30, width=200)
enter_max_iterations.place(x=725, y=30, width=260)

# ================= CANVAS =================== 

table = Canvas(root)
table.place(x=30, y=120, width=650, height=350)

# Таблица

# Основная рамка

table.create_line(0, 0, 0, 350, width=10)
table.create_line(0, 350, 650, 350, width=10)
table.create_line(0, 0, 650, 0, width=10)
table.create_line(650, 0, 650, 350, width=10)

# Линии внутри

table.create_line(90, 0, 90, 350, width=5)
table.create_line(210, 0, 210, 350, width=5)
table.create_line(320, 0, 320, 350, width=5)
table.create_line(430, 0, 430, 350, width=5)
table.create_line(540, 0, 540, 350, width=5)

table.create_line(0, 40, 650, 40, width=5)

# Лэйблы внутри таблицы 

# Заголовки таблицы

label_number = Label(table, text="№", font="Arial 14", bg="#9370DB")
label_interval = Label(table, text="Интервал", font="Arial 14", bg="#9370DB")
label_approximation = Label(table, text="x̅", font="Arial 14", bg="#9370DB")
label_approximation_function = Label(table, text="f(x̅)", font="Arial 14", \
        bg="#9370DB")
label_count_iterations = Label(table, text="Количество \nитераций", \
        font="Arial 12", bg="#9370DB")
label_code_error = Label(table, text="Код \nвыполнения", font="Arial 12", \
        bg="#9370DB")

# Вывод заголовков

label_number.place(x=5, y=5, width=84, height=33)
label_interval.place(x=93, y=5, width=115, height=33)
label_approximation.place(x=213, y=5, width=105, height=33)
label_approximation_function.place(x=323, y=5, width=105, height=33)
label_count_iterations.place(x=433, y=5, width=105, height=33)
label_code_error.place(x=543, y=5, width=102, height=33)

# == Лэйблы с значениями ==


# Номера поиска

#list_label_number = []
y_coord = 44

"""
for i in range(6):
    label_numbers = Label(table, text="", bg="#008080", font="Arial 14")
    label_numbers.place(x=5, y = y_coord, width=83, height=50)
    list_label_number.append(label_numbers)
    y_coord += 50
"""

label_number = Label(table, text="", bg="#008080", font="Arial 12")
label_number.place(x=5, y=44, width=83, height=300)

# Интервалы поиска

#list_label_intervals = []

#for i in range(6):
label_interval = Label(table, text="", bg="#008080", font="Arial 12")
label_interval.place(x=93, y = 43.7, width=115, height=300)
    #list_label_intervals.append(label_intervals)
    #y_coord += 50

# Приближенное значение

list_label_approximate = []
y_coord = 44

#for i in range(6):
label_approximate = Label(table, text="", bg="#008080", font="Arial 12")
label_approximate.place(x=213, y=44, width=105, height=300)
    #list_label_approximate.append(label_approximates)
    #y_coord += 50

# Приближенное значение от функции 

#list_label_approximate_func = []
#y_coord = 44

#for i in range(6):
label_approximate_func = Label(table, text="", bg="#008080", font="Arial 12")
label_approximate_func.place(x=323, y=44, width=105, height=300)
#list_label_approximate_func.append(label_approximates_func)
#y_coord += 501

# Количество итераций

#list_label_count_iterations = []
#y_coord = 44

#for i in range(6):
label_count_iteration = Label(table, text="", bg="#008080", font="Arial 12")
label_count_iteration.place(x=433, y=44, width=105, height=300)
#list_label_count_iterations.append(label_count_iterations)
#y_coord += 50

# Код ошибки

#list_label_code_error = []
#y_coord = 44

#for i in range(6):
label_code_error = Label(table, text="", bg="#008080", font="Arial 12")
label_code_error.place(x=543, y=y_coord, width=102, height=300)
    #list_label_code_error.append(label_code_error)
    #y_coord += 50

root.mainloop()
