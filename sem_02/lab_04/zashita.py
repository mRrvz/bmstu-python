from tkinter import *
from tkinter import simpledialog as sd

def painting_solution(answer):
    coordinate_system.place(x=350, y=30)
    coordinate_system.delete("all")
    WinX = 786; WinY = 586
    xmax = list_points[0][0]; ymax = list_points[0][1]
    xmin = list_points[0][0]; ymin = list_points[0][1]

    for i in range(len(list_points)):
        if list_points[i][0] > xmax:
            xmax = list_points[i][0]
        if list_points[i][0] < xmin:
            xmin = list_points[i][0]
        if list_points[i][1] > ymax:
            ymax = list_points[i][1]
        if list_points[i][1] < ymin:
            ymin = list_points[i][1]

    scalex = (WinX - 20) / (xmax - xmin)
    scaley = (WinY - 20) / (ymax - ymin)
    offsetx = -xmin * scalex + 10
    offsety = -ymin * scaley + 10

    for i in range(len(answer)):
        x = answer[i][0] * scalex + offsetx
        y = WinY - (answer[i][1] * scaley + offsety)
        x1 = answer[i][2] * scalex + offsetx
        y1 = WinY - (answer[i][3] * scaley + offsety)
        coordinate_system.create_line(x, y, x1, y1, fill="red", width=3)

    for i in range(len(list_points)):
        x_new = list_points[i][0] * scalex + offsetx
        y_new = WinY - (list_points[i][1] * scaley + offsety)
        coordinate_system.create_oval(x_new - 6, y_new - 6, x_new + 6, y_new + 6, fill="green")
    label = Label(root, text="")
    label["text"] = "Answer is: \n"
    for i in range(len(answer)):
        label["text"] += str(answer[i][0]) + " " + str(answer[i][2]) + " " + str(answer[i][1]) + " " + str(answer[i][1]) + "\n"
    label.place(x=20, y=60, width=100, height=100)

def coef(x1, y1, x2, y2):
    try:
        k = (y2 - y1) / (x2 - x1)
    except:
        k = "par"
    return str(k)

def go_find():
    lines = []
    for i in range(len(list_points) -1):
        for j in range(i + 1, len(list_points)):
            arr = []
            arr.append(list_points[i][0])
            arr.append(list_points[i][1])
            arr.append(list_points[j][0])
            arr.append(list_points[j][1])

            lines.append(arr)

    res = -1
    for a in range(len(lines) - 1):
        new_res = 1
        new_res_lines = [[lines[a][0], lines[a][1], lines[a][2], lines[a][3]]]
        for b in range(a + 1, len(lines)):
            try:
                first_slope = (lines[a][3]- lines[a][1])/(lines[a][2]- lines[a][0])
            except:
                first_slope = 6666
            try:
                second_slope = (lines[b][3]- lines[b][1])/(lines[b][2]- lines[b][0])
            except:
                second_slope = 6666
            if first_slope == second_slope:
                new_res += 1
                new = []
                new.append(lines[b][0])
                new.append(lines[b][1])
                new.append(lines[b][2])
                new.append(lines[b][3])
                new_res_lines.append(new)

        if new_res > res:
            res = new_res

            res_lines = new_res_lines
    print("Answer is: ", res_lines)
    painting_solution(res_lines)
                        
def cleaning_matrix():
    index_del = 0
    while len(list_points) != 0:
        list_points.pop(index_del)

def enter_coord():
    cleaning_matrix()
    count_points = sd.askinteger("Количество точек", "Введите количество точек", parent=root)
    for i in range(count_points):
        point = sd.askstring("Введите координаты точки №" + str(i + 1), "Введите координаты точки: ", parent=root)
        point = list(map(int, point.split()))
        list_points.append(point)
    go_find()

    
root = Tk()
root.maxsize(width=1200, height=640)
root.minsize(width=1200, height=640)

list_points = []
button_enter = Button(root, text="Решить задачу", command=enter_coord)
button_enter.place(x=20, y=20)
coordinate_system = Canvas(root, width=786, height=586, bg="#66A3D2")

root.mainloop()
