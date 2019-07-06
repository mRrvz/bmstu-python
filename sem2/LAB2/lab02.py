
"""
=============================== О Программе =================================

По своей сути программа составляет сортировку вставками, дополненную бинарным
поиском с элементами интерфейса. В программе можно отсортировать введеный 
массив (до 10 чисел), либо же случайный, задав параметры этого массива. 
На экран выводится время сортировки разных типов массивов. Так же, можно
посмотреть пошаговый алгоритм сортировки массиве, введенным пользователем.


=============================================================================

"""


from tkinter import *
from tkinter import messagebox as mb
import numpy as np
import time 

# Функция обновления label-виджета при изменения поля Entry

def checked_entry(sv):
    if "\n" in steps_sort_label["text"]:
        steps_sort_label["text"] = "Введите массив\n(до десяти чисел)"
        steps_sort_label["font"] = "Arial 24"   


# Изменение текста в Label-виджете (для пошагового вывода сортировки)

def change_text_in_label(text):
    steps_sort_label["text"] += "\n" + text 


# Информация о программе

def about_programm():
    mb.showinfo("Информация о программе", "Данная программа сортирует несколько \
типов случайных массивов (упорядоченный, отсортированный и т.д) с помощью \
сортировки простыми вставками с бинарным поиском. Программа выводит время сортировки \
для каждого из массивов. Так же, пользователь может ввести свой массив, и посмотреть \
пошаговый алгоритм сортировки.\n\nРазработчик: Романов Алексей, группа ИУ7-23Б.")


# Сортировка вставками с бинарным поиском

def sort_binary_find(list_to_sort, flag = False):
    start_time = time.time()

    # Алгоритм сортировки

    for i in range(1, len(list_to_sort)):
        key = list_to_sort[i]; left = -1; right = i

        # Бинарный поиск

        while left < right - 1:
            mid = (right + left) // 2
            if list_to_sort[mid] >= key:
                right = mid
            else:
                left = mid

        # Смещение текущнго элемента и сзади стоящих по индексу,
        # который был найден с помощью бинарного поиска

        for j in range(i, right, -1):
            list_to_sort[j] = list_to_sort[j-1]
        list_to_sort[right] = key

        if not flag:
            message_list = " ".join(map(str, list_to_sort))
            change_text_in_label(message_list)
            if i != len(list_to_sort) - 1:
                steps_sort_label["text"] += "\n"

    now_time = time.time()
    
    if flag == True:
        time_sort = now_time - start_time    
        return list_to_sort, time_sort
    

# Сортировка разных массивов и измерение времени сортировки.

def sort_random_array(low_range, high_range, size_list, window):
    random_array = np.random.randint(low=low_range, high=high_range + 1, \
            size = size_list)
    random_array_copy = random_array.copy()
    
    if window == 1:
        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_first["text"] = "{0:.9f}".format(time_sort)

        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_second["text"] = "{0:.9f}".format(time_sort)

        random_array = random_array[::-1]
        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_third["text"] = "{0:.9f}".format(time_sort)

        now_time = time.time()
        random_array_copy.sort()
        time_sort = time.time() - now_time
        time_std_sort["text"] = "{0:.9f}".format(time_sort)
        
    elif window == 2:
        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_first_second_arr["text"] = "{0:.9f}".format(time_sort)

        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_second_second_arr["text"] = "{0:.9f}".format(time_sort)

        random_array = random_array[::-1]
        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_third_second_arr["text"] = "{0:.9f}".format(time_sort)

        now_time = time.time()
        random_array_copy.sort()
        time_sort = time.time() - now_time
        table_time_std_second_arr["text"] = "{0:.9f}".format(time_sort)
        
    elif window == 3:
        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_first_third_arr["text"] = "{0:.9f}".format(time_sort)

        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_second_third_arr["text"] = "{0:.9f}".format(time_sort)

        random_array = random_array[::-1]
        random_array, time_sort = sort_binary_find(random_array, True)
        table_time_third_third_arr["text"] = "{0:.9f}".format(time_sort)

        now_time = time.time()
        random_array_copy.sort()
        time_sort = time.time() - now_time
        table_time_std_third_arr["text"] = "{0:.9f}".format(time_sort)


# Вызов окна - ошибки

def error(string):
    mb.showerror("Ошибка", string)


# Проверка введеных данных пользователем для сортировки случайного массива

def checked_correcntess_random_array(entry_size, entry_range, window):
    size_list = entry_size.get()
    size_list = size_list.strip()
    range_list = entry_range.get()
    
    try:
        range_list = list(map(int, range_list.split()))
    except:
        error("Диапазон должен содержать два значения, \
введеных через пробел. Например: 10 -150.")
        return
    
    if len(range_list) != 2:
        error("Диапазон должен содержать два значения, \
введеных через пробел. Например: 10 - 150.")
        return
    
    if range_list[0] >= range_list[1]:
        error("Первое число в диапазоне должно быть меньше, чем второе.")
        return

    if not(size_list.isdigit()) or \
                              int(size_list) < 2 or int(size_list) > 9000000000:
        error("Вы ввели некорректную размерность массива.")
        return
    
    if int(size_list) < 10000:
        table_size_list["font"] = "Arial 28"
    elif int(size_list) >= 100000000:
        table_size_list["font"] = "Arial 13"
    elif int(size_list) >= 1000000:
        table_size_list["font"] = "Arial 15"
    elif int(size_list) >= 10000:
        table_size_list["font"]= "Arial 23"

    if window == 1:
        table_size_list["text"] = size_list
    elif window == 2:
        table_size_list_third["text"] = size_list
    elif window == 3:
        table_size_list_second["text"] = size_list

    sort_random_array(range_list[0], range_list[1], int(size_list), window)


# Проверка корректности введеного массива
    
def checked_correctness(list_entry):
    text_string = list_entry.get()
    text_string = text_string.strip()
    checked_list = ["-", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i in range(len(text_string)):
        if text_string[i] not in checked_list:
            error("Массив должен состоять только из чисел.")
            return
        if text_string[i] == "-" and text_string[i-1] != " ":
            if i == 0:
                continue
            else:
                error("Некорректный ввод.")
                return
        
    example_list = text_string.split()

    if " " not in text_string or len(example_list) > 10:
        error("Массив должен содержать от 2 до 10 элементов.")
        return

    example_list = list(map(int, example_list))
   
    if len(text_string) < 16:
        steps_sort_label["font"] = "Arial 14"
    elif len(text_string) < 24:
        steps_sort_label["font"] = "Arial 11"
    elif len(text_string) < 48:
        steps_sort_label["font"] = "Arial 9"
    elif len(text_string) < 55:
        steps_sort_label["font"] = "Arial 6"
    elif len(text_string) < 59:
        steps_sort_label["font"] = "Arial 3"

    steps_sort_label["text"] = text_string + "\n"
    sort_binary_find(example_list)
    

# Создание главного окна и его настройка

root = Tk()
root.geometry("1300x400")
root.title("Бинарная сортировка вставками")
root.maxsize(height=400, width=1300)
root.minsize(height=400, width=1300)

# Label's

bg_image = PhotoImage(file="bg_main_lab02.png")
bg_label = Label(image=bg_image)

table_size_list = Label(root, text="", font="Arial 36", \
        bg="#8cea3f", justify=CENTER)
table_size_list_second = Label(root, text="", font="Arial 22", \
        bg="#8cea3f", justify=CENTER)
table_size_list_third = Label(root, text="", font="Arial 22", \
        bg="#8cea3f", justify=CENTER)

# Время (первый массив)

table_time_first = Label(root, text="", font="Arial 12", \
        justify=CENTER, bg="#8cea3f")
table_time_second = Label(root, text="", font="Arial 12", \
        justify=CENTER, bg="#8cea3f")
table_time_third = Label(root, text="", font="Arial 12", \
        justify=CENTER, bg="#8cea3f")
time_std_sort = Label(root, text="", font="Arial 12", \
        justify=CENTER, bg="#8cea3f")

# Время (второй массив)

table_time_first_second_arr = Label(root, text="", font="Arial 10", \
        justify=CENTER, bg="#8cea3f")
table_time_second_second_arr = Label(root, text="", font="Arial 10", \
        justify=CENTER, bg="#8cea3f")
table_time_third_second_arr = Label(root, text="", font="Arial 10", \
        justify=CENTER, bg="#8cea3f")
table_time_std_second_arr = Label(root, text="", font="Arial 10", \
        justify=CENTER, bg="#8cea3f")

# Время (третий массив)

table_time_first_third_arr = Label(root, text="", font="Arial 10", \
        justify=CENTER, bg="#8cea3f")
table_time_second_third_arr = Label(root, text="", font="Arial 10", \
        justify=CENTER, bg="#8cea3f")
table_time_third_third_arr = Label(root, text="", font="Arial 10", \
        justify=CENTER, bg="#8cea3f")
table_time_std_third_arr = Label(root, text="", font="Arial 10", \
        justify=CENTER, bg="#8cea3f")

steps_sort_label = Label(root, text="Введите массив\n(до десяти чисел)", \
        font = "Arial 24", bg="#AFEEEE", justify=CENTER)
info_about_enter_diapazon = Label(root, text="Введите   размеры   массивов:", \
        font = "Arial 9", bg="#9eeef7")
info_about_enter_size = Label(root, text="Введите диапазоны массивов:\n(через пробел)", \
        font = "Arial 9", bg="#9eeef7")


# Entry's

size_list_label = Entry(root)
range_list_entry = Entry(root)

size_list_label_second = Entry(root)
range_list_entry_second = Entry(root)

size_list_label_third = Entry(root)
range_list_entry_third = Entry(root)

# Button's

butt_sort = Button(root, text="Начать сортировку", \
        command=lambda:checked_correctness(list_entry))
butt_start_random_sort = Button(root, text="Сортировать", \
        command=lambda:checked_correcntess_random_array(size_list_label, range_list_entry, 1))
butt_start_random_sort_second = Button(root, text="Сортировать", \
        command=lambda:checked_correcntess_random_array(size_list_label_second, range_list_entry_second, 2))
butt_start_random_sort_third = Button(root, text="Сортировать", \
        command=lambda:checked_correcntess_random_array(size_list_label_third, range_list_entry_third, 3))

# Menu

mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="О программе", command=about_programm)
mainmenu.add_command(label="Выйти", command=exit)

# Вывод виджетов и настройка координат
    
butt_sort.place(x=220, y=43)

butt_start_random_sort.place(x=640, y=89)
butt_start_random_sort_second.place(x=840, y=89)
butt_start_random_sort_third.place(x=1140, y=89)

bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Окна ввода (первый массив)

size_list_label.place(x=640, y=45)
range_list_entry.place(x=640, y=66)

# Окна ввода (второй массив)

size_list_label_second.place(x=840, y=45)
range_list_entry_second.place(x=840, y=66)

# Окна ввода (третий массив)

size_list_label_third.place(x=1140, y=45)
range_list_entry_third.place(x=1140, y=66)

#  Размеры массивов

table_size_list.place(x=663, y=172, width=115, height=204)
table_size_list_second.place(x=1098, y=172, width=80, height=205)
table_size_list_third.place(x=897, y=172, width=103, height=205)

# Время сортировок (первый массив)

table_time_first.place(x=783, y=172, width=109, height=35)
table_time_second.place(x=783, y=212, width=109, height=41)
table_time_third.place(x=783, y=257, width=109, height=59)
time_std_sort.place(x=783, y=320, width=109, height=57)

# Время сортировок (второй массив)

table_time_first_second_arr.place(x=1005, y=172, heigh=35, width=88)
table_time_second_second_arr.place(x=1005, y=212, height=42, width=88)
table_time_third_second_arr.place(x=1005, y=258, height=58, width=88)
table_time_std_second_arr.place(x=1005, y=320, height=57, width=88)

# Время сортировк (третий массив)

table_time_first_third_arr.place(x=1183, y=172, heigh=35, width=84)
table_time_second_third_arr.place(x=1183, y=212, height=42, width=84)
table_time_third_third_arr.place(x=1183, y=258, height=58, width=84)
table_time_std_third_arr.place(x=1183, y=320, height=57, width=84)

steps_sort_label.place(x=143, y=73, width=273, height=301)
info_about_enter_diapazon.place(x=450, y=46)
info_about_enter_size.place(x=450, y=66) 

# Проверка на изменение Entry

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: checked_entry(sv))
list_entry = Entry(root, textvariable=sv)
list_entry.place(x=180, y=23, width=200)

root.mainloop()

