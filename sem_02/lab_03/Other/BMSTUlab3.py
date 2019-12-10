from tkinter import *
from tkinter import messagebox
from BMSTUlab3_steffensen import *
import matplotlib.pyplot as plt
import matplotlib.patches as ptch


def label_writer(to_write, label_out):
    """ Функция записи в Label.

    Данная функция изменяет содержимое поля text в Label.

    Передаваемые параметры:
    * to_write - что будет записано в Label
    * label_out - Label, в который будет произведена запись

    """

    label_out["text"] = ""
    label_out["text"] += to_write


def clean_entry(*entries):
    """ Функция очистки полей ввода.

    Данная функция очищает поля ввода/вывода данных.
    Очистка может производиться как одного, так и сразу
    нескольких полей.

    Передаваемые параметры:
    * *entries - поля ввода, которые надо очистить

    """

    for entry in entries:
        entry.config(state="normal")
        entry.delete(0, END)


def float_list_getter_dim(in_entry):
    """ Функция формирования вещественного списка.

    Данная функция формирует вещественный список для
    получения интервала итерации при уточнении корней.

    Передаваемые параметры:
    * in_entry - поле ввода, из которого формируется список

    Возвращаемые значения:
    * float_list - сформированный вещественный список

    """

    try:
        float_list = [float(x) for x in in_entry.get().strip().split()]

        if len(float_list) == 0 or len(float_list) > 2 or \
                isinstance(float_list, (str, type(None))):
            raise ValueError

        return float_list

    except ValueError:
        messagebox.showerror("Ошибка ввода данных", "Данные введены "
                                                    "некорректно, проверьте "
                                                    "правильность ввода!")


def clean_label(*labels):
    """ Функция очистки Label'ов.

    Данная функция очищает Label'ы
    (изменяет их поля text на пустую строку "")

    Передаваемые параметры:
    * *labels - Label'ы, которые надо очистить

    """

    for label in labels:
        label["text"] = ""


def calculate_roots(dim_entry, step_entry, eps_entry, maxiter_entry):
    """ Функция нахождения корней по заданным параметрам.

    Данная функция находит корни уравнения по диапазону измерений,
    шагу итерации, точности измерений и максимальному количеству
    итераций.

    Передаваемые параметры:
    * dim_entry - поле ввода диапазона
    * step_entry - поле ввода шага итерации
    * eps_entry - поле ввода точности измерений
    * maxiter_entry - поле ввода максимального количества итераций

    """

    try:
        dim_list = float_list_getter_dim(dim_entry)
        if dim_list[0] >= dim_list[1]:
            messagebox.showerror("Ошибка ввода данных", "Интервал должен "
                                                        "быть возрастающим "
                                                        "(start < end)")
            return False

        step = float(step_entry.get().strip())
        if step < 0:
            messagebox.showerror("Ошибка ввода данных", "Шаг должен "
                                                        "быть положительным "
                                                        "(step > 0)")
            return False

        eps = float(eps_entry.get().strip())
        if not (0 < eps < step / 2):
            messagebox.showerror("Ошибка ввода данных", "Точность должна "
                                                        "лежать в интервале "
                                                        "(0 < eps < step/2)")
            return False

        maxiter = int(maxiter_entry.get().strip())
        if maxiter < 0:
            messagebox.showerror("Ошибка ввода данных", "Количество итераций "
                                                        "строго положительное "
                                                        "(maxiter > 0)")
            return False

        n = 1

        n_list = list()
        x_root = list()
        fx_root = list()
        left_verge_list = list()
        right_verge_list = list()
        iters_list = list()
        error_code_list = list()

        while dim_list[0] + step * (n - 1) < dim_list[1]:
            left_verge = dim_list[0] + step * (n - 1)
            right_verge = dim_list[0] + step * n if \
                dim_list[0] + step * n < dim_list[1] else dim_list[1]

            froot, iter_num, error_code = steffensen_root_finding(left_verge,
                                                                  right_verge,
                                                                  eps,
                                                                  maxiter,
                                                                  x_curr=left_verge)

            if error_code == 2:
                froot, iter_num, error_code = steffensen_root_finding(left_verge,
                                                                      right_verge,
                                                                      eps,
                                                                      maxiter,
                                                                      x_curr=right_verge)

                if error_code == 2:
                    froot, iter_num, error_code = steffensen_root_finding(left_verge,
                                                                          right_verge,
                                                                          eps,
                                                                          maxiter,
                                                                          x_curr=((left_verge + right_verge) / 2))
            if (error_code == 0 or error_code == 1) and (len(x_root) == 0 or abs(froot - x_root[-1]) > 2 * eps):
                n_list.append(n)
                x_root.append(froot)
                fx_root.append(f(froot))
                left_verge_list.append(left_verge)
                right_verge_list.append(right_verge)
                iters_list.append(iter_num)
                error_code_list.append(error_code)

            n += 1

        return n_list, x_root, fx_root, left_verge_list, right_verge_list, iters_list, error_code_list, dim_list

    except ValueError:
        messagebox.showerror("Ошибка ввода данных", "Проверьте корректность "
                                                    "введенных данных")

    except TypeError:
        pass


def find_roots(dim_entry, step_entry, eps_entry, maxiter_entry):
    """ Функция вывода корней по заданным параметрам.

    Данная функция выводит корни уравнения по диапазону измерений,
    шагу итерации, точности измерений и максимальному количеству
    итераций.

    Передаваемые параметры:
    * dim_entry - поле ввода диапазона
    * step_entry - поле ввода шага итерации
    * eps_entry - поле ввода точности измерений
    * maxiter_entry - поле ввода максимального количества итераций

    """

    calculated = calculate_roots(dim_entry, step_entry, eps_entry, maxiter_entry)

    if calculated:
        find_roots_window = Toplevel(root)
        find_roots_window.grab_set()
        find_roots_window.focus_set()
        find_roots_window.iconbitmap("icon.ico")
        find_roots_window.geometry("605x500+840+200")
        find_roots_window.resizable(False, False)
        find_roots_window.title("Таблица найденных приближенных значений корней. "
                                "Steffenson Root-Finder")
        find_roots_window.config(bg="#000080")

        f_r_w_welcome_label = Label(find_roots_window,
                                    text="Таблица найденных приближенных "
                                         "значений корней",
                                    font="consolas 10 bold",
                                    bg="white",
                                    fg="#000080")
        f_r_w_welcome_label.place(x=303, y=25, anchor="center")

        num_label = Label(find_roots_window,
                          text="#",
                          font="consolas 10 bold",
                          bg="white",
                          fg="#000080",
                          width=4,
                          height=1)
        num_label.place(x=10, y=50)

        int_label = Label(find_roots_window,
                          text="[x(i), x(i + 1)]",
                          font="consolas 10 bold",
                          bg="white",
                          fg="#000080",
                          width=20,
                          height=1)
        int_label.place(x=50, y=50)

        root_label = Label(find_roots_window,
                           text="~x",
                           font="consolas 10 bold",
                           bg="white",
                           fg="#000080",
                           width=8,
                           height=1)
        root_label.place(x=202, y=50)

        froot_label = Label(find_roots_window,
                            text="f(~x)",
                            font="consolas 10 bold",
                            bg="white",
                            fg="#000080",
                            width=12,
                            height=1)
        froot_label.place(x=270, y=50)

        iter_label = Label(find_roots_window,
                           text="Кол-во итераций",
                           font="consolas 10 bold",
                           bg="white",
                           fg="#000080",
                           width=15,
                           height=1)
        iter_label.place(x=367, y=50)

        err_label = Label(find_roots_window,
                          text="Код ошибки",
                          font="consolas 10 bold",
                          bg="white",
                          fg="#000080",
                          width=15,
                          height=1)
        err_label.place(x=484, y=50)

        cur_y = 50

        for i in range(len(calculated[0])):
            num_label = Label(find_roots_window,
                              text=str(calculated[0][i]),
                              font="consolas 10 bold",
                              bg="white",
                              fg="#000080",
                              width=4,
                              height=1)
            num_label.place(x=10, y=cur_y+25)

            int_label = Label(find_roots_window,
                              text="[{:.4f}; {:.4f}]".format(calculated[3][i], calculated[4][i]),
                              font="consolas 10 bold",
                              bg="white",
                              fg="#000080",
                              width=20,
                              height=1)
            int_label.place(x=50, y=cur_y+25)

            root_label = Label(find_roots_window,
                               text="{:.4f}".format(calculated[1][i]),
                               font="consolas 10 bold",
                               bg="white",
                               fg="#000080",
                               width=8,
                               height=1)
            root_label.place(x=202, y=cur_y+25)

            froot_label = Label(find_roots_window,
                                text="{:.4e}".format(calculated[2][i]),
                                font="consolas 10 bold",
                                bg="white",
                                fg="#000080",
                                width=12,
                                height=1)
            froot_label.place(x=270, y=cur_y+25)

            iter_label = Label(find_roots_window,
                               text=str(calculated[5][i]),
                               font="consolas 10 bold",
                               bg="white",
                               fg="#000080",
                               width=15,
                               height=1)
            iter_label.place(x=367, y=cur_y + 25)

            err_label = Label(find_roots_window,
                              text=str(calculated[6][i]),
                              font="consolas 10 bold",
                              bg="white",
                              fg="#000080",
                              width=15,
                              height=1)
            err_label.place(x=484, y=cur_y+25)

            cur_y += 25


def draw_plot(dim_entry, step_entry, eps_entry, maxiter_entry):
    calculated = calculate_roots(dim_entry, step_entry, eps_entry, maxiter_entry)

    x = [0] * 50000
    fx = [0] * 50000
    step_graph = (calculated[7][1] - calculated[7][0]) / 49999

    for i in range(50000):
        x[i] = calculated[7][0] + step_graph * i
        fx[i] = f(x[i])

    max_graph = fx[0]
    max_graph_dot = 0
    min_graph = fx[0]
    min_graph_dot = 0

    max_min_graph_dots_x = list()
    max_min_graph_dots_y = list()

    for i in range(1, 49999):
        if fx[i] > max_graph:
            max_graph = fx[i]
            max_graph_dot = x[i]
        if fx[i] < min_graph:
            min_graph = fx[i]
            min_graph_dot = x[i]

    max_min_graph_dots_x.append(max_graph_dot)
    max_min_graph_dots_x.append(min_graph_dot)
    max_min_graph_dots_y.append(max_graph)
    max_min_graph_dots_y.append(min_graph)

    plt.clf()
    plt.grid(True)
    plt.plot(x, fx, color='black', linewidth=1)
    plt.scatter(max_min_graph_dots_x, max_min_graph_dots_y, color='red', linewidth=0.5)
    plt.scatter(calculated[1], calculated[2], color='green', linewidth=0.5)

    plt.title(str_f())
    plt.xlabel('x')
    plt.ylabel('y')

    root_patch = ptch.Patch(color='green', label='Roots')
    exs_patch = ptch.Patch(color='red', label='Max/Min')
    patch_list = []
    if len(max_min_graph_dots_x):
        patch_list.append(root_patch)
    if len(calculated[1]):
        patch_list.append(exs_patch)

    plt.legend(handles=patch_list)
    plt.show()


def about():
    """" Вывод окна "О программе" """
    about_window = Toplevel(root)
    about_window.grab_set()
    about_window.focus_set()
    about_window.iconbitmap("icon.ico")
    about_window.geometry("330x200+425+250")
    about_window.resizable(False, False)
    about_window.title("О Steffenson Root-Finder")
    about_window.config(bg="#000080")

    about_label1 = Label(about_window,
                         text="\nВизуализация метода Стеффенсона\n "
                              "для уточнения корней функции.\n"
                              "Программа строит таблицу приближенных корней\n"
                              "и строит по полученной функции график."
                              "\n\n"
                              "Kononenko Sergey ICS7-23B",
                         font="consolas 10",
                         bg="#000080",
                         fg="white")
    about_label1.pack()

    about_label2 = Label(about_window,
                         text="@hackfeed",
                         font="consolas 10 bold",
                         bg="white",
                         fg="#000080")
    about_label2.pack()

    exit_about = Button(about_window, text="Выйти",
                        width=6,
                        height=2,
                        font="consolas 10 bold",
                        bg="#000080",
                        fg="white",
                        relief="flat",
                        command=lambda: exit_run(about_window))
    exit_about.pack()


def exit_run(root):
    """ Выход из программы. """
    root.destroy()


def bind_find_roots(event):
    """ Нахождение корней при нажатии на клавишу Enter. """
    find_roots(dimension_entry, iterstep_entry, epsilon_entry, itercount_entry)


def bind_draw_plot(event):
    """ Вывод графика при нажатии комбинации Control-Alt-P. """
    draw_plot(dimension_entry, iterstep_entry, epsilon_entry, itercount_entry)


""" Создание каскада окна программы. """
root = Tk()
root.iconbitmap("icon.ico")
root.geometry("425x450+400+200")
root.resizable(False, False)
root.title("Steffenson Root-Finder")

""" Создание меню. """
main_menu = Menu(root)
root.config(menu=main_menu, bg="#000080")

func_menu = Menu(main_menu, tearoff=0)
func_menu.add_command(label="Найти корни",
                      command=lambda: find_roots(dimension_entry,
                                                 iterstep_entry,
                                                 epsilon_entry,
                                                 itercount_entry))
func_menu.add_command(label="Построить график",
                      command=lambda: draw_plot(dimension_entry,
                                                iterstep_entry,
                                                epsilon_entry,
                                                itercount_entry))
func_menu.add_separator()
func_menu.add_command(label="Выйти",
                      command=lambda: exit_run(root))

clean_menu = Menu(main_menu, tearoff=0)
clean_menu.add_command(label="Очистить поле ввода диапазона",
                       command=lambda: clean_entry(dimension_entry))
clean_menu.add_command(label="Очистить поле ввода шага итерации",
                       command=lambda: clean_entry(iterstep_entry))
clean_menu.add_command(label="Очистить поле ввода точности",
                       command=lambda: clean_entry(epsilon_entry))
clean_menu.add_command(label="Очистить поле ввода количества итераций",
                       command=lambda: clean_entry(itercount_entry))
clean_menu.add_separator()
clean_menu.add_command(label="Очистить все поля",
                       command=lambda: (clean_entry(dimension_entry,
                                                    iterstep_entry,
                                                    epsilon_entry,
                                                    itercount_entry)))

about_menu = Menu(main_menu, tearoff=0)
about_menu.add_command(label="О программе", command=lambda: about())

main_menu.add_cascade(label="Выполнить", menu=func_menu)
main_menu.add_cascade(label="Очистка", menu=clean_menu)
main_menu.add_cascade(label="Справка", menu=about_menu)

welcome_label = Label(root,
                      text="Нахождение корней функции с исползованием "
                           "метода Стеффенсона",
                      font="consolas 10 bold",
                      bg="white",
                      fg="#000080")
welcome_label.grid(row=1, column=1, columnspan=3)

split_label_1 = Label(root,
                      text="",
                      bg="#000080",
                      fg="white")
split_label_1.grid(row=2, column=1, columnspan=3)

dimension_label = Label(root,
                        text="Введите диапазон\n измерений",
                        font="consolas 10",
                        bg="#000080",
                        fg="white")
dimension_label.grid(row=3, column=1, rowspan=3, columnspan=2)

dimension_entry_start = "-10 10"
dimension_entry = Entry(root, width=20)
dimension_entry.insert(0, dimension_entry_start)
dimension_entry.grid(row=3, column=3, rowspan=3)

dimension_entry.focus_set()

iterstep_label = Label(root,
                       text="Введите шаг\n итерации измерений",
                       font="consolas 10",
                       bg="#000080",
                       fg="white")
iterstep_label.grid(row=6, column=1, rowspan=3, columnspan=2)

iterstep_entry_start = "1"
iterstep_entry = Entry(root, width=20)
iterstep_entry.insert(0, iterstep_entry_start)
iterstep_entry.grid(row=6, column=3, rowspan=3)

epsilon_label = Label(root,
                      text="Введите точность\n измерений",
                      font="consolas 10",
                      bg="#000080",
                      fg="white")
epsilon_label.grid(row=9, column=1, rowspan=3, columnspan=2)

epsilon_entry_start = "0.0001"
epsilon_entry = Entry(root, width=20)
epsilon_entry.insert(0, epsilon_entry_start)
epsilon_entry.grid(row=9, column=3, rowspan=3)

itercount_label = Label(root,
                        text="Введите количество\n итераций",
                        font="consolas 10",
                        bg="#000080",
                        fg="white")
itercount_label.grid(row=12, column=1, rowspan=3, columnspan=2)

itercount_entry_start = "20"
itercount_entry = Entry(root, width=20)
itercount_entry.insert(0, itercount_entry_start)
itercount_entry.grid(row=12, column=3, rowspan=3)

current_func_label = Label(root,
                           text="Текущая функция",
                           font="consolas 10 bold",
                           bg="white",
                           fg="#000080")
current_func_label.place(anchor="center", x=212, y=215)

current_func_label_ex = Label(root,
                              text="",
                              font="consolas 10 bold",
                              bg="#000080",
                              fg="white")
current_func_label_ex.place(anchor="center", x=212, y=245)

entry_list = [dimension_entry, iterstep_entry, itercount_entry, epsilon_entry]

label_writer(str_f(), current_func_label_ex)

find_roots_button = Button(root, text="Найти корни",
                           width=16,
                           height=2,
                           font="consolas 10 bold",
                           bg="white",
                           fg="#0ad325",
                           command=lambda: find_roots(dimension_entry,
                                                      iterstep_entry,
                                                      epsilon_entry,
                                                      itercount_entry))
find_roots_button.place(anchor="center", x=212, y=285)

draw_plot_button = Button(root, text="Построить график",
                          width=16,
                          height=2,
                          font="consolas 10 bold",
                          bg="white",
                          fg="#570099",
                          command=lambda: draw_plot(dimension_entry,
                                                    iterstep_entry,
                                                    epsilon_entry,
                                                    itercount_entry))
draw_plot_button.place(anchor="center", x=212, y=335)

exit_button = Button(root, text="Выйти",
                     width=16,
                     height=2,
                     font="consolas 10 bold",
                     bg="white",
                     fg="#ff0000",
                     command=lambda: exit_run(root))
exit_button.place(anchor="center", x=212, y=385)

for entry in entry_list:
    entry.bind("<Return>", bind_find_roots)
    entry.bind("<Control-Alt-KeyPress-p>", bind_draw_plot)

root.mainloop()
