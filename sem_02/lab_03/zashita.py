from tkinter import *
from math import sin, cos, ceil
from tkinter import messagebox as mb


def derivative_f(x):
    return -sin(x)


def f(x):
    return cos(x)


def empty_labels():
    for label in label_list:
        label["text"] = ""

def update_labels(count_roots, temp_a, temp_b, root, code_error, max_iterations):
    label_roots["text"] += str(count_roots) + "\n\n"
    label_interval["text"] += "[{:.2f}, {:.2f}]".format(temp_a, temp_b) + "\n\n"

    if int(code_error) != 0:
        label_x["text"] += "-" + "\n\n"
        label_fx["text"] += "-" + "\n\n"
        label_iterations["text"] += "-" + "\n\n"
    else:
        label_x["text"] += "{:.7f}".format(root) + "\n\n"
        label_fx["text"] += "{:.0e}".format(f(root)) + "\n\n"
        label_iterations["text"] += str(max_iterations) + "\n\n"

    label_error["text"] += str(code_error) + "\n\n"
    

def Newton_method(step, border_a, border_b, epsilon, max_iterations):
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
                root = root_previous - (f(root_previous) / derivative_f(root_previous))

                while abs(root - root_previous) > epsilon and count_iterations < max_iterations:
                    root_previous = root
                    root = root_previous - (f(root_previous) / derivative_f(root_previous))
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


def find_roots(interval, step, eps, iterations):

    interval_list = interval.split()
    border_a = int(interval_list[0])
    border_b = int(interval_list[1])
    step = float(step); epsilon = float(eps); max_iterations = int(iterations)
    border_a -= 0.001
    border_b += 0.001

    empty_labels()
    list_approximate, roots = Newton_method(step, border_a, border_b, epsilon, max_iterations)
    if roots == 0:
        mb.showerror("Ошибка", "На заданном промежутке корней не найдено.")
    
root = Tk()
root.geometry("650x600")
root.title("Метод касательных")
root.config(bg="yellow")

enter_interval = Entry(root)
enter_interval.place(x=20, y=30)
enter_step = Entry(root)
enter_step.place(x=160, y=30)
enter_eps = Entry(root)
enter_eps.place(x=300, y=30)
enter_iterations = Entry(root)
enter_iterations.place(x=440, y=30, width=175)

button_find = Button(root, text="Начать поиск корней", command=lambda: find_roots(enter_interval.get(),
                                                                                  enter_step.get(),
                                                                                  enter_eps.get(),
                                                                                  enter_iterations.get()))
button_find.place(x=20, y=55)

info_roots = Label(root, text="№")
info_roots.place(x=20, y=100, width=70)
info_interval = Label(root, text="Интервал")
info_interval.place(x=92, y=100, width=90)
info_x = Label(root, text="x")
info_x.place(x=184, y=100, width=100)
info_fx = Label(root, text="f(x)")
info_fx.place(x=286, y=100, width=100)
info_iterations = Label(root, text="Кол-во итераций")
info_iterations.place(x=388, y=100, width=100)
info_error = Label(root, text="Код ошибки")
info_error.place(x=490, y=100, width=100)

bg_color = "pink"
label_roots = Label(root, text="", bg=bg_color)
label_roots.place(x=20, y=140, height=440, width=70)
label_interval = Label(root, text="",bg=bg_color)
label_interval.place(x=92, y=140, height=440, width=90)
label_x = Label(root, text="", bg=bg_color)
label_x.place(x=184, y=140, height=440, width=100)
label_fx = Label(root, text="", bg=bg_color)
label_fx.place(x=286, y=140, height=440, width=100)
label_iterations = Label(root, text="",  bg=bg_color)
label_iterations.place(x=388, y=140, height=440, width=100)
label_error = Label(root, text="",  bg=bg_color)
label_error.place(x=490, y=140, height=440, width=100)

label_interval_ent = Label(root, text="Введите интервал:")
label_interval_ent.place(x=20, y=5, width=125)
label_step_ent = Label(root, text="Введите шаг:")
label_step_ent.place(x=160, y=5, width=125)
label_eps_ent = Label(root, text="Введите Epsilon:")
label_eps_ent.place(x=300, y=5, width=125)
label_iter_ent = Label(root, text="Введите макс. кол-во итераций")
label_iter_ent.place(x=440, y=5, width=175)

label_list = [label_roots, label_interval, label_x, label_fx, label_iterations, label_error]

root.mainloop()
