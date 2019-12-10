from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog
from math import *
import numpy

# [MENU] How to enter data
def how_to_input():
    mb.showinfo("Как нужно вводить координаты", "Координаты точек вводятся в формате:\n\
x y.\nНапример точка с координатами (4, 3) вводится как 4 3.\n\nКоординаты \
вершин треугольников вводятся в формате: \nx1 y1 x2 y2 x3 y3.\nНапример, \
треугольник с вершинами (3, 1), (6, 2), (6, 6) вводится как \
3 1 6 2 6 6.")


# [MENU] INFO about programm
def about_program():
    mb.showinfo("Информация о программе", "Данная программа из задаваемого \
множества точек А, и задаваемого множества треугольников Б находит две такие \
точки из множества А, что если через них провести прямую, она будет пересекаться \
с максимальным количеством треугольников из множества Б.\n\n\
Разработчик: Романов Алексей. Группа: ИУ7-23Б.")


# Cleaning matrix with last entered coordinates
def cleaning_matrix():
    index_del = 0
    while len(matrix_triangle) != 0:
        matrix_triangle.pop(index_del)

    index_del = 0
    while len(matrix_points) != 0:
        matrix_points.pop(index_del)

# Output coordinates to label
def parser_to_label(list_points, type):
    if type == "triangle":
        info_coordinates_triangles["text"] += \
                    "({0}, {1}), ({2}, {3}), ({4}, {5})".format(*list_points) + "\n"
    else:
        info_coordiantes_points["text"] += "({0}, {1})".format(*list_points) + "\n"

# Existence triangle check
def triangle_check(tr_list):
    # 0 0 4 0 0 4#0 - 

    if (tr_list[4] - tr_list[0]) * (tr_list[5] - tr_list[3]) == \
                    (tr_list[4] - tr_list[2]) * (tr_list[5] - tr_list[1]):
        return "NOT_EXIST"
    else:
        return "EXIST"


# Check && enter coordinates
def enter_coordinates():
    answer_triangles["text"] = ""
    VALID_VALUE_TRIANGLES = 6; VALID_VALUE_POINTS = 2
    TYPE_TR = "triangle"; TYPE_POINTS = "points"
    while True:
        count_triangles = simpledialog.askinteger("Количество треугольников", \
                "Укажите количество треугольников в множестве А:", parent=root)
        if count_triangles == None:
            return
        if count_triangles > 0:
            break
        else:
            mb.showerror("Ошибка", "Размер множества А должен быть больше нуля.")
            continue

    while True:
        count_points = simpledialog.askinteger("Количество точек", \
            "Укажите количество точек в множестве Б (минимум две):", parent=root)
        if count_points == None:
            return
        if count_points > 1:
            break
        else:
            mb.showerror("Ошибка", "Размер множества Б должен быть больше единицы.")
            continue

    # Enter triangles coordinates
    for i in range(count_triangles):
        while True:
            triangle_string = simpledialog.askstring("Треугольник № " + str(i + 1), \
                                    "Введите координаты треугольника № " + str(i + 1))

            if triangle_string == "":
                return
            try:
                list_triangles = list(map(int, triangle_string.split()))
            except:
                mb.showerror("Ошибка", "Некорректный ввод.")
                continue
            if len(list_triangles) != VALID_VALUE_TRIANGLES:
                mb.showerror("Ошибка", "Вы ввели некорректное количество координат вершин треугольника.")
                continue
            if triangle_check(list_triangles) == "NOT_EXIST":
                mb.showerror("Ошибка", "Треугольник с заданными вершинами не существует.")
                continue
            if list_triangles in matrix_triangle:
                mb.showerror("Ошибка", "Треугольник с заданными вершинами уже содержится в множестве А.")

            # End cycle if all data of triangles is OK
            info_coordinates_triangles["text"] += "Треугольник № " + str(i + 1) + ":  "
            matrix_triangle.append(list_triangles)
            parser_to_label(list_triangles, TYPE_TR)
            break
    info_coordinates_triangles["text"] += "\nКоличество треугольников: " + str(count_triangles)

    # Enter points coordinates
    for i in range(count_points):
        while True:
            points_string = simpledialog.askstring("Точка № " + str(i + 1), \
                                    "Введите координаты точки № " + str(i + 1))

            if points_string == "":
                return
            try:
                list_points = list(map(int, points_string.split()))
            except:
                mb.showerror("Ошибка", "Некорректный ввод.")
                continue
            if len(list_points) != VALID_VALUE_POINTS:
                mb.showerror("Ошибка", "Точка должна содержать только координату Х и Y.")
                continue
            if list_points in matrix_points:
                mb.showerror("Ошибка", "Точка с такими координатами уже содержится в множестве Б.")
                continue

            # End cycle if all data of points is OK
            info_coordiantes_points["text"] += "Точка № " + str(i + 1) + ": "
            parser_to_label(list_points, TYPE_POINTS)
            matrix_points.append(list_points)
            break
    info_coordiantes_points["text"] += "\nКоличество точек: " + str(count_points)


# Cleaning labels info with current sets A && B
def cleaning_lables_info():
    info_coordinates_triangles["text"] =  "Введенные треугольники множества Б: \n\n"
    info_coordiantes_points["text"] = "Введенные точки множества А: \n\n"


# Calculating equation straight line
def straight_equation(x1, y1, x2, y2):
    try:
        A = (y1 - y2) / (x1 - x2)
    except ZeroDivisionError:
        return 1, 0, x1
    C = y2 - A * x2
    return -A, 1, C


# Check if the found point belongs to the segment of triangle
def ownership_check(x0, x1, x_check, y0, y1, y_check):
    if x0 > x1:
        x0, x1 = x1, x0
    if y1 < y0:
        y0, y1 = y1, y0

    if float(x0) <= float(x_check) <= float(x1) and float(y0) <= float(y_check) <= float(y1):
        return "BELONG"
    else:
        return "NOT_BELONG"


# Solving a system of equations
def solving_system(A_p, B_p, C_p, A_t, B_t, C_t, x0):
    M1 = numpy.array([[float(A_p), float(B_p)],[float(A_t), float(B_t)]])
    V1 = numpy.array([float(C_p), float(C_t)])
    try:
        list_solutions = numpy.linalg.solve(M1, V1)
    except:
        return 'NO_ROOTS', 'NO_ROOTS'
    return list_solutions[0], list_solutions[1]

# Brute force all triangles
def selection_triangle(A_point, B_point, C_point, x0, x1):
    number_intersections = 0; intersection_list = list()
    for i in range(len(matrix_triangle)):
        intersect = False
        for j in range(0, 6, 2):
            index_x = (j + 2) % 6
            index_y = (j + 3) % 6
            # Find triangle equation
            A_triangle, B_triangle, C_triangle = straight_equation(matrix_triangle[i][j],
                                                       matrix_triangle[i][j + 1],
                                                       matrix_triangle[i][index_x],
                                                       matrix_triangle[i][index_y])
            # Find intersection (coordinate X)
            solution_x, y = solving_system(A_point, B_point, C_point, A_triangle, B_triangle, C_triangle, x0)
            if str(solution_x) == 'NO_ROOTS':
                continue

            # Check, does point belong to a segment
            if ownership_check(matrix_triangle[i][j], \
                               matrix_triangle[i][index_x], solution_x, matrix_triangle[i][j + 1], \
                               matrix_triangle[i][index_y], y) == "BELONG":
                if not intersect:
                    number_intersections += 1
                    intersect = True

                intersection_list.append(solution_x)
                intersection_list.append(float(y))

    return number_intersections, intersection_list


# Brute force all points
def selection_two_points():
    max_intersection_list = list()
    best_points = list()
    max_number_intersections = 0
    for i in range(len(matrix_points) -1):
        for j in range((i + 1), len(matrix_points)):
            A, B, C = straight_equation(matrix_points[i][0],
                                     matrix_points[i][1],
                                     matrix_points[j][0],
                                     matrix_points[j][1])
            number_intersections, intersection_list = \
                selection_triangle(A, B, C, matrix_points[i][0], matrix_points[j][0])
            #print('POINTS: ', matrix_points[i][0], matrix_points[i][1], matrix_points[j][0], matrix_points[j][1], intersection_list, number_intersections)
            if number_intersections > max_number_intersections:
                best_points = list()
                max_number_intersections = number_intersections
                max_intersection_list = intersection_list
                best_points.append(matrix_points[i][0])
                best_points.append(matrix_points[i][1])
                best_points.append(matrix_points[j][0])
                best_points.append(matrix_points[j][1])

    return best_points, max_number_intersections, max_intersection_list


# Painting && scaling
def painting_solution(intersection_list, best_points):
    coordinate_system.place(x=350, y=30)
    coordinate_system.delete("all")
    WinX = 786; WinY = 586
    xmax = matrix_points[0][0]; ymax = matrix_points[0][1]
    xmin = matrix_points[0][0]; ymin = matrix_points[0][1]

    # Scaling canvas
    # Find min && max coordinates
    for i in range(len(matrix_points)):
        if matrix_points[i][0] > xmax:
            xmax = matrix_points[i][0]
        if matrix_points[i][0] < xmin:
            xmin = matrix_points[i][0]
        if matrix_points[i][1] > ymax:
            ymax = matrix_points[i][1]
        if matrix_points[i][1] < ymin:
            ymin = matrix_points[i][1]
    for i in range(len(matrix_triangle)):
        for j in range(0, 6, 2):
            if matrix_triangle[i][j] > xmax:
                xmax = matrix_triangle[i][j]
            if matrix_triangle[i][j] < xmin:
                xmin = matrix_triangle[i][j]
            if matrix_triangle[i][j + 1] > ymax:
                ymin = matrix_triangle[i][j + 1]
            if matrix_triangle[i][j + 1] < ymin:
                ymin = matrix_triangle[i][j + 1]

    # Coef of scaling
    scalex = (WinX - 20) / (xmax - xmin)
    scaley = (WinY - 20) / (ymax - ymin)
    offsetx = -xmin * scalex + 10
    offsety = -ymin * scaley + 10

    # Painting triangle
    for i in range(len(matrix_triangle)):
        for j in range(0, 6, 2):
            index_x = (j + 2) % 6
            index_y = (j + 3) % 6
            x_new = matrix_triangle[i][j] * scalex + offsetx
            y_new = WinY - (matrix_triangle[i][j + 1] * scaley + offsety)
            x_new2 = matrix_triangle[i][index_x] * scalex + offsetx
            y_new2 = WinY - (matrix_triangle[i][index_y] * scaley + offsety)
            coordinate_system.create_line(x_new, y_new, x_new2, y_new2, width=3)

    # Painting line solution line

    if best_points[0] < best_points[2]:
        x = best_points[0]; x1 = best_points[2]
        y = best_points[1]; y1 = best_points[3]
    else:
        x = best_points[2]; x1 = best_points[0]
        y = best_points[3]; y1 = best_points[1]

    SHIFT = 400
    A, B, C = straight_equation(x, y, x1, y1)
    if B != 0:
        y = -A * (x - SHIFT) + C
        y1 = -A * (x1 + SHIFT) + C
    else:
        y = -x + C - SHIFT
        y1 = -x1 + C + SHIFT
        SHIFT = 0

    x_new = (x - SHIFT) * scalex + offsetx
    y_new = WinY - (y * scaley + offsety)
    x_new2 = (x1 + SHIFT) * scalex + offsetx
    y_new2 = WinY - (y1 * scaley + offsety)
    coordinate_system.create_line(x_new , y_new, x_new2, y_new2, fill="red", width=3)
    #coordinate_system.create_line(0, y_new * i, x_new2, y_new2 * i, fill="red", width=3)

        # Painting points
    for i in range(len(matrix_points)):
        x_new = matrix_points[i][0] * scalex + offsetx
        y_new = WinY - (matrix_points[i][1] * scaley + offsety)
        coordinate_system.create_oval(x_new - 6, y_new - 6, x_new + 6, y_new + 6, fill="green")
        # Painting intersection coordinates
    for i in range(0, len(intersection_list), 2):
        x_new = intersection_list[i] * scalex + offsetx
        y_new = WinY - (intersection_list[i + 1] * scaley + offsety)
        coordinate_system.create_oval(x_new - 6, y_new - 6, x_new + 6, y_new + 6, fill="yellow")
        # Painting solutiongs coordinates
    for i in range(0, len(best_points), 2):
        x_new = best_points[i] * scalex + offsetx
        y_new = WinY - (best_points[i + 1] * scaley + offsety)
        coordinate_system.create_oval(x_new - 7, y_new - 7, x_new + 7, y_new + 7, fill="blue")


# Start finding a solution to the problem
def solution_of_problem():
    # Update labels info
    cleaning_lables_info()
    cleaning_matrix()
    enter_coordinates()
    # Place label's with info about triangles && points coordinates
    info_coordinates_triangles.place(x=10, y=315, width=275, height=270)
    info_coordiantes_points.place(x=10, y=40, width=275, height=270)
    # Counting the two best points
    best_points, intersections, intersection_list = selection_two_points()
    answer_triangles.place(x=10, y=590, height=35, width=275)
    print(best_points)
    answer_triangles["text"] = "Решение: ({0}, {1}), ({2}, {3})".format(best_points[0],best_points[1], best_points[2], best_points[3])
    painting_solution(intersection_list, best_points)

# Root setting's (main window)
root = Tk()
root.maxsize(width=1200, height=640)
root.minsize(width=1200, height=640)
root.title("Лабораторная работа №4")
bg_image = PhotoImage(file="bg_image_lab04.png")
label_bg = Label(image=bg_image)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)
mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="О программе", command=about_program)
mainmenu.add_command(label="Формат ввода данных", command=how_to_input)
mainmenu.add_command(label="Выйти", command=exit)

# Label's
info_coordiantes_points = Label(root, text="Введенные точки множества Б:\n\n",
                                justify=LEFT, bg="#8BA100", anchor=W, font="Sylfaen 10")
info_coordinates_triangles = Label(root, text="Введенные треугольники множества А:\n\n",
                                   justify=LEFT, bg="#8BA100", anchor=W, font="Sylfaen 10")
answer_triangles = Label(root, text="", justify=LEFT, bg="#8BA100", anchor=W, font="Sylfaen 10")

# Button's
button_find_solution = Button(root, text="Ввести координаты множеств и решить задачу",
                                    command=solution_of_problem)
button_find_solution.place(x=10, y=10, width=275)

# Matrix with DATA (points && triangles coordinates)
matrix_triangle = list()
matrix_points = list()

# Canvas
coordinate_system = Canvas(root, width=786, height=586, bg="#66A3D2")
root.mainloop()
