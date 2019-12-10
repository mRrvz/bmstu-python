from math import *
from tkinter import *
from tkinter import messagebox as mb
import numpy as np
import pylab

def about_program():
    mb.showinfo("Информация о программе", "Напиши тут что-нибудь сама")


def code_errors():
    mb.showinfo("Коды ошибок", "1. Превышено количество итераций")


def f(x):
    return sin(x)


def f1(x):
    return cos(x)


def cleaning_label():

    for labels in label_list:
        labels["text"] = ""


def create_point(list, color, name):

    i = 0
    for roots in list:
        y = roots
        if i == 0:
            pylab.scatter(roots, f(y), color=color,
                          label=name)
        else:
            pylab.scatter(roots, f(y), color=color)
        i+= 1


def create_graph(xmin, xmax, roots_list, extremum_list):

    dx = 0.001
    fig = pylab.gcf()
    fig.canvas.set_window_title("F(x)")
    xlist = np.arange(xmin, xmax, dx)
    ylist = [f(x) for x in xlist]
    x_list_OX = np.arange(xmin, xmax, dx)
    y_list_OX = [0 for x in (x_list_OX)]

    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.plot(xlist, ylist, label="f(x)")
    pylab.plot(x_list_OX, y_list_OX)
    create_point(roots_list, "blue", "Solutions")
    create_point(extremum_list, "red", "Extremums")

    pylab.legend()
    pylab.title("f(x)")
    pylab.tick_params(labelsize=14)
    pylab.show()


def update_labels(a, b, x, curr_iterations, count_roots, code_error):

    label_number["text"] += str(count_roots) + "\n\n"
    label_interval["text"] += "[{:.2f}, {:.2f}]".format(a, b) + "\n\n"
    label_x["text"] += "{:.6f}".format(x) + "\n\n"
    label_fx["text"] += "{:.0e}".format(f(x)) + "\n\n"
    label_iterations["text"] += str(curr_iterations) + "\n\n"
    label_code_error["text"] += str(code_error) + "\n\n"


def extremum_find(interval):

    a = interval[0]
    DEF_ITER = 1000; DEF_EPS = 0.00001
    extremum_list = []
    flag = True
    while flag:
        b = a + 0.5
        if b > interval[1]:
            b = interval[1]
            flag = False
        try:
            x, curr_iterations = brent(f1, a, b, DEF_ITER, DEF_EPS)
            extremum_list.append(x)
        except:
            pass
        a = b

    return extremum_list


def update_table(interval, step, iterations, epsilon):

    a = interval[0]
    flag = True
    count_roots = 0
    roots_list = []
    while flag:
        code_error = "0"
        b = a + step
        if b > interval[1]:
            b = interval[1]
            flag = False
        try:
            x, curr_iterations = brent(f, a, b, iterations, epsilon)
            count_roots += 1
            if curr_iterations > iterations:
                code_error = "1"
            else:
                roots_list.append(x)
            update_labels(a, b, x, curr_iterations, count_roots, code_error)
        except:
            pass
        a = b

    extremum_list = extremum_find(interval)
    if count_roots == 0:
        mb.showerror("Ошибка", "На заднном интервале нет корней.")
    else:
        graph_button = Button(root, text="Показать график функции", command=lambda: create_graph(interval[0],
                                                                                                 interval[1],
                                                                                                 roots_list,
                                                                                                 extremum_list))
        graph_button.place(x=335, y=60)


# Validation of entered data
def check_entry(interval, step, iterations, epsilon):

    cleaning_label()
    try:
        interval = list(map(float, interval.split()))
    except:
        mb.showerror("Ошибка", "Некорректный ввод интервала поиска.")
        return
    if not (1 < len(interval) < 3):
        mb.showerror("Ошибка", "Интервал поиска должен содержать 2 числа.")
        return
    if interval[0] > interval[1]:
        mb.showerror("Ошибка", "Введеная правая граница меньше левой границы интервала.")
        return

    try:
        step = float(step)
        iterations = int(iterations)
        epsilon = float(epsilon)
    except:
        print(type(iterations), type(epsilon))
        mb.showerror("Ошибка", "Некорректный ввод исходных данных.")
        return

    update_table(interval, step, iterations, epsilon)


# Brent method
def brent(f, x0, x1, max_iter, eps):

    fx0 = f(x0)
    fx1 = f(x1)

    if (fx0 * fx1) > 0:
        return

    if abs(fx0) < abs(fx1):
        x0, x1 = x1, x0
        fx0, fx1 = fx1, fx0

    x2, fx2 = x0, fx0

    flag = True
    d = x1
    cur_n = 0
    while cur_n < max_iter and abs(x1-x0) > eps and f(x1) != 0:
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)

        if fx0 != fx2 and fx1 != fx2:
            L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
            L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
            L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
            new = L0 + L1 + L2

        else:
            new = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))

        if ((new < ((3 * x0 + x1) / 4) or new > x1) or
            (flag == True and (abs(new - x1)) >= (abs(x1 - x2) / 2)) or
            (flag == False and (abs(new - x1)) >= (abs(x2 - d) / 2)) or
            (flag == True and (abs(x1 - x2)) < eps) or
            (flag == False and (abs(x2 - d)) < eps)):
            new = (x0 + x1) / 2
            flag = True

        else:
            flag = False

        fnew = f(new)
        d, x2 = x2, x1

        if (fx0 * fnew) < 0:
            x1 = new
        else:
            x0 = new

        if abs(fx0) < abs(fx1):
            x0, x1 = x1, x0

        cur_n += 1

    return x1, cur_n

# Create & setting main window
root = Tk()
root.geometry("700x520")
root.maxsize(width=700, height=520)
root.minsize(width=700, height=520)
root.title("Уточнение корней методом Брента")
root.configure(bg="blue")

# Crete menu
mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="О программе", command=about_program)
mainmenu.add_command(label="Коды ошибок", command=code_errors)
mainmenu.add_command(label="Выйти", command=exit)

# Entry's
entry_interval = Entry(root)
entry_interval.place(x=30, y=30)
entry_step = Entry(root)
entry_step.place(x=180, y=30)
entry_iterations = Entry(root)
entry_iterations.place(x=335, y=30, width=172)
entry_eps = Entry(root)
entry_eps.place(x=530, y=30, width=147)


# Label's (info)
info_interval = Label(root, text="Введите интервал:", bg="yellow")
info_interval.place(x=30, y=8, width=124)
info_step = Label(root, text="Введите шаг:", bg="yellow")
info_step.place(x=180, y=8, width=124)
info_iterations = Label(root, text="Введите макс. кол-во итераций:", font="Arial 8", bg="yellow")
info_iterations.place(x=335, y=8)
info_epsilon = Label(root, text="Введите точность Epsilon:", bg="yellow")
info_epsilon.place(x=530, y=8)


# Button's
find_root = Button(root, text="Начать поиск корней", command=lambda: check_entry(entry_interval.get(), \
                                                                                 entry_step.get(), \
                                                                                 entry_iterations.get(), \
                                                                                 entry_eps.get()))
find_root.place(x=180, y=60)


# Canvas (table)
table = Canvas(root)
table.place(x=50, y=100, width=600, height=400)
table.create_line(0, 0, 0, 400, width=10)
table.create_line(0, 400, 600, 400, width=10)
table.create_line(0, 0, 600, 0, width=10)
table.create_line(600, 0, 600, 400, width=10)

table.create_line(70, 0, 70, 400, width=5)
table.create_line(180, 0, 180, 400, width=5)
table.create_line(290, 0, 290, 400, width=5)
table.create_line(400, 0, 400, 400, width=5)
table.create_line(510, 0, 510, 400, width=5)
table.create_line(0, 40, 650, 40, width=5)

# Label's (canvas)
label_number = Label(table, text="", bg="pink")
head_number = Label(table, text="№", bg="violet")
head_number.place(x=5, y=5, width=63, height=33)
label_number.place(x=5, y=42, width=63, height=352)
label_interval = Label(table, text="", bg="pink")
head_interval = Label(table, text="Интервал", bg="violet")
head_interval.place(x=73, y=5, width=105, height=33)
label_interval.place(x=73, y=42, width=105, height=352)
label_x = Label(table, text="", bg="pink")
head_x = Label(table, text="x̅", bg="violet")
head_x.place(x=183, y=5, width=105, height=33)
label_x.place(x=183, y=42, width=105, height=352)
label_fx = Label(table, text="", bg="pink")
head_fx = Label(table, text="f(x̅)", bg="violet")
head_fx.place(x=293, y=5, width=105, height=33)
label_fx.place(x=293, y=42, width=105, height=352)
label_iterations = Label(table, text="", bg="pink")
head_iterations = Label(table, text="Количество\nитераций", bg="violet")
head_iterations.place(x=403, y=5, width=105, height=33)
label_iterations.place(x=403, y=42, width=105, height=352)
label_code_error = Label(table, text="", bg="pink")
error_head = Label(table, text="Код\nошибки", bg="violet")
error_head.place(x=513, y=5, width=82, height=33)
label_code_error.place(x=513, y=42, width=82, height=352)
label_list = [label_number, label_interval, label_x, label_fx, label_iterations, label_code_error]

root.mainloop()