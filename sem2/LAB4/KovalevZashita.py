from tkinter import *
lines = []
 
res = -1
res_lines = []
 
SIZE = 3
BSIZE = 5
 
def main():
    for i in range(len(lines)):
        canvas.create_line(lines[i][0], lines[i][1], lines[i][2], lines[i][3])
 
    for a in range(len(lines) - 1):
        new_res = 1
        new_res_lines = [[lines[a][0], lines[a][1], lines[a][2], lines[a][3]]]
        for b in range(a, len(lines)):
            first_slope = (lines[a][3]- lines[a][1])/(lines[a][2]- lines[a][0])
            second_slope = (lines[b][3]- lines[b][1])/(lines[b][2]- lines[b][0])
            if first_slope == second_slope:
                new_res += 1
                new = []
                new.append(lines[b][0])
                new.append(lines[b][1])
                new.append(lines[b][2])
                new.append(lines[b][3])
                new_res_lines.append(new)
        global res
        if new_res > res:
            res = new_res
            global res_lines
            res_lines = new_res_lines
 
    for i in range(len(res_lines)):
        canvas.create_line(res_lines[i][0], res_lines[i][1], res_lines[i][2], res_lines[i][3], fill="yellow")
 
def clear():
    canvas.delete("all")
    global lines
    lines = []
 
def add_point(x1, y1, x2, y2):
    canvas.create_oval(x1 - SIZE, y1 - SIZE, x1 + SIZE, y1 + SIZE, fill="red")
    canvas.create_oval(x2 - SIZE, y2 - SIZE, x2 + SIZE, y2 + SIZE, fill="red")
    canvas.create_line(x1, y1, x2, y2)
 
    new = []
    new.append(x1)
    new.append(y1)
    new.append(x2)
    new.append(y2)
    global lines
    lines.append(new)
 
def add_from_but():
    x_1 = arg_x_1.get()
    y_1 = arg_y_1.get()
    x_2 = arg_x_2.get()
    y_2 = arg_y_2.get()
 
    if 0 <= x_1 <= 1000 and 0 <= x_2 <= 1000 and 0 <= y_1 <= 1000 and 0 <= y_2 <= 1000:
        add_point(x_1, y_1, x_2, y_2)
    else:
        print("ошибка")
 
 
root = Tk()
root.title('Solution search')
root["bg"] = "#edeef0"
 
root.geometry("1200x1000")
root.resizable(height=False, width=False)
 
Label(root, font=('Ubuntu', 13), text='Введите новую точку').grid(row=0, column=0, columnspan=2)
 
 
arg_x_1 = IntVar()
arg_y_1 = IntVar()
 
EntryX_1 = Entry(root, textvariable=arg_x_1, width=5, font='Arial 16').grid(row=1, column=0)
EntryY_1 = Entry(root, textvariable=arg_y_1, width=5, font='Arial 16').grid(row=1, column=1)
 
arg_x_2 = IntVar()
arg_y_2 = IntVar()
 
EntryX_2 = Entry(root, textvariable=arg_x_2, width=5, font='Arial 16').grid(row=2, column=0)
EntryY_2 = Entry(root, textvariable=arg_y_2, width=5, font='Arial 16').grid(row=2, column=1)
add_button = Button(text="Добавить линию", command=add_from_but).grid(row=3, column=0, columnspan=2)
search_button = Button(text="Произвести расчет", command=main).grid(row=4, column=0, columnspan=2)
clean_button = Button(text="Очистить", command=clear).grid(row=16, column=0, columnspan=2)
 
canvas = Canvas(root, width=1000, height=1000, bg='grey')
canvas.grid(row=0, column=2, rowspan=17)
 
root.mainloop()
