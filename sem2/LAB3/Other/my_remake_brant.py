from matplotlib.pyplot import *
from numpy import *
from tkinter import *
from tkinter.ttk import Treeview
import tkinter.messagebox as box

from scipy.optimize import brenth

DEF_LEFT = 0
DEF_RIGHT = 10

DEF_STEP = 1
DEF_EPS = 10**(-4)
DEF_MAX_N = 10**2

ER_CONV = 1


def my_f(x):
    return sin(x)

def pro_f(x):
    return cos(x)


def brent(f, x0, x1, max_iter=DEF_MAX_N, eps=DEF_EPS):

    fx0 = f(x0)
    fx1 = f(x1)

    if (fx0 * fx1) > 0:
        raise ValueError("Root does not exist")

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


def find_extreme(a, b):
    step = 10e-3
    x_t = a + step
    x_prev = b
    mx = max(my_f(a), my_f(b))
    mm = min(my_f(a), my_f(b))
    while x_t < b:
        if pro_f(x_t) * pro_f(x_prev) < 0:
            mx = max(my_f(x_t), mx)
            mm = min(my_f(x_t), mm)
        x_prev = x_t
        x_t += step
    return mm, mx


def plot(diap1, diap2, n1, n2, n3, err):
    err.set("")
    try:
        a = int(float(diap1.get()))
        b = int(float(diap2.get()))
        h = float(n1.get())
        eps = float(n2.get())
        n_max = int(n3.get())
        chk_border(a, b)
    except ValueError:
        err.set("Неверные данные")
        return 1
    x = linspace(a, b, 10000)
    y = my_f(x)
    fig, ax = subplots()
    min_, max_ = find_extreme(a, b)
    ax.plot(x, y, color="red", label="f(x)")
    ax.plot(x, min_ + x * 0, color="green", label="min ~ " + str(round(min_, 3)))
    ax.plot(x, max_ + x * 0, color="green", label="max ~ " + str(round(max_, 3)))
    ax.plot(x, x * 0, color="black", label="y = 0")
    a1 = a
    b1 = a + h
    while b1 < b:
        y1 = x
        ax.plot(x * 0 + a1, y1, color="black")
        ax.plot(x * 0 + b1, y1, color="black")
        try:
            st, num = brent(my_f, a1, b1, n_max, eps)
        except ValueError:
            ax.plot(x * 0 + (b-a)/2, y1, color="red")
        a1 = b1
        b1 += h
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    show()


def chk_border(mn, mx):
    if mn > mx:
        raise ValueError("Invalid borders")


def launch_table(win, table, diap1, diap2, n1, n2, n3, err, wait):
    err.set("")
    try:
        a = float(diap1.get())
        b = float(diap2.get())
        h = float(n1.get())
        eps = float(n2.get())
        n_max = int(n3.get())
        chk_border(a, b)
    except ValueError:
        err.set("Неверные данные")
        return 1

    wait.set("Идет обработка данных")

    win.update()

    roots_arr = []
    a1 = a
    b1 = a + h
    itr = 1
    while a1 < b:
        limits = str("[" + str(a1) + "; " + str(b1) + "]")
        try:
            st, num = brent(my_f, a1, b1, n_max, eps)
        except ValueError:
            a1 = b1
            b1 += h
            continue

        x_res = str(round(st, 5)) if a1 <= st <= b1 else '-'
        if a1 <= st <= b1 and my_f(st) == 0:
            y_res = '0'
        else:
            y_res = '1e' + f'{fabs(my_f(st)):.0g}'[2:] if a1 <= st <= b1 else '-'
            if len(y_res) <= 3 and y_res != '-':
                y_res = '1e-6'

        if num == str(num) or num >= n_max:
            table.insert('', str(itr), text=str(itr),
                         values=(limits, '-', '-', n_max, str(ER_CONV)))
        else:
            if x_res != '-':
                if x_res not in roots_arr:
                    table.insert('', str(itr), text=str(itr),
                                 values=(limits, x_res, y_res, str(num), '-'))
                else:
                    itr -= 1
                roots_arr.append(x_res)

        win.update()

        a1 = b1
        b1 += h
        if b1 >= b:
            b1 = b
        itr += 1

    wait.set("")
    return 1


def launch_scipy(win, table, diap1, diap2, n1, n2, n3, err, wait):
    err.set("")
    try:
        a = float(diap1.get())
        b = float(diap2.get())
        h = float(n1.get())
        eps = float(n2.get())
        n_max = int(n3.get())
        chk_border(a, b)
    except ValueError:
        err.set("Неверные данные")
        return 1

    wait.set("Идет обработка данных")

    win.update()
    roots_arr = []
    a1 = a
    b1 = a + h
    itr = 1
    while a1 < b:
        limits = str("[" + str(a1) + "; " + str(b1) + "]")
        try:
            st, dat = brenth(my_f, a1, b1, xtol=eps, maxiter=n_max,
                             full_output=True)
        except ValueError:
            a1 = b1
            b1 += h
            continue
        except RuntimeError:
            table.insert('', str(itr), text=str(itr),
                         values=(limits, '-', '-', '-', str(ER_CONV)))
        else:
            x_res = str(round(st, 5)) if a1 <= st <= b1 else '-'
            if a1 <= st <= b1 and my_f(st) == 0:
                y_res = '0'
            else:
                y_res = '1e' + f'{fabs(my_f(st)):.0g}'[
                               2:] if a1 <= st <= b1 else '-'

            num = dat.iterations
            if num == str(num) or num >= n_max:
                table.insert('', str(itr), text=str(itr),
                             values=(limits, '-', '-', n_max, str(ER_CONV)))
            else:
                if x_res != '-':
                    if x_res not in roots_arr:
                        table.insert('', str(itr), text=str(itr),
                                     values=(
                                     limits, x_res, y_res, str(num), '-'))
                    else:
                        itr -= 1
                    roots_arr.append(x_res)
        win.update()

        a1 = b1
        b1 += h
        if b1 >= b:
            b1 = b
        itr += 1

    wait.set("")
    return 1


def clear_table(window, tbl):
    tbl.delete(*tbl.get_children())
    window.update()
    return 1


def code_box():
    box.showinfo('Коды', '1-Превышено макс. кол. итераций')


def about_box():
    box.showinfo('О программе', 'Программа для демонстрации работы '
                                'метода Брента уточнения корней.\n'
                                'Использует две версии алгоритма:\n'
                                'функцию brenth из модуля scipy\n'
                                'и написанную внучную функцию.\n'
                                )


def clear_table_by_event(event, window, *args):
    but = event.keycode
    if 48 <= but <= 57 or 65 <= but <= 90 or but == 8 or but == 46:
        for tbl in args:
            tbl.delete(*tbl.get_children())
        window.update()
    return 1


root = Tk()
root.title("Уточнение корней")
root.geometry("600x650")

menubar = Menu(root)

menubar.add_command(label="Коды ошибок", command=code_box)
menubar.add_command(label="О программе", command=about_box)
menubar.add_command(label="Выйти", command=root.quit)

root.config(menu=menubar)


text0 = Label(root, width=50, height=1, text="Укажите границы" 
                                             " (действительные числа): ")
text0.grid(row=1, column=1, columnspan=6)

diap1 = Entry(root, width=7, bg="white")
diap1.grid(row=2, column=3, sticky=W)
diap1.bind("<Key>", lambda event: clear_table_by_event(event, root, res_table,
                                                       res_table2))
text3 = Label(root, width=4, height=1, text="a = ")
text3.grid(row=2, column=2, sticky=E)
diap2 = Entry(root, width=7, bg="white")
diap2.bind("<Key>", lambda event: clear_table_by_event(event, root, res_table,
                                                       res_table2))
diap2.grid(row=2, column=5, sticky=W)
text30 = Label(root, width=4, height=1, text="b = ")
text30.grid(row=2, column=4, sticky=E)

text_01 = Label(root, width=50, height=1, text="Укажите шаг, погрешность "
                                               "и макс. кол. итераций: ")
text_01.grid(row=3, column=2, columnspan=6)
text4 = Label(root, width=4, height=1, text="h ")
text4.grid(row=4, column=1, sticky=E)
n1 = Entry(root, width=7, bg="white")
n1.grid(row=4, column=2)
n1.bind("<Key>", lambda event: clear_table_by_event(event, root, res_table, res_table2))
text5 = Label(root, width=4, height=1, text="eps ")
text5.grid(row=4, column=3, sticky=E)
n2 = Entry(root, width=7, bg="white")
n2.grid(row=4, column=4)
n2.bind("<Key>", lambda event: clear_table_by_event(event, root, res_table, res_table2))
text6 = Label(root, width=4, height=1, text="Nmax ")
text6.grid(row=4, column=5, sticky=E)
n3 = Entry(root, width=7, bg="white")
n3.grid(row=4, column=6)
n3.bind("<Key>", lambda event: clear_table_by_event(event, root, res_table, res_table2))


err_var = StringVar()
wait_var = StringVar()



Button(root, text='Показать график', width=60,
       command=lambda: plot(diap1, diap2, n1, n2, n3, err_var)).place(x=10, y=580,
                                                                  height=30)

root.mainloop()
