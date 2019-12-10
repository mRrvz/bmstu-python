""" 

O программе.

Данная программа - калькулятор действительных чисел в двоичной системе.
В программе присутствует экранный интерфейс и меню. 
Кнопка "Повтор действия" - выполняет последнее действие, произведенное калькулятором.
(например: при вводе 11110 + 111.01 и нажатии на эту кнопку, калькулятор прибавит 111.01)
Кнопка "Очистить ввод" полностью очищает поле ввода.
Кнопка "О программе" выводит соответствующую информацию о программе 


Тестовые примеры.

В квадратных скобка обозначены ответы, которые должен выдать калькулятор.

1. 101111.01 + 10001.101 = [1000000.111] // Жмем "Повтор действия" /// 
(на экране должно появится + 10001.101) = 1010010.1

2. 1111 - 11111.01 = [-10000.01] - 1111111 = [-10001111.01]

3. -11111 + 11111 = [0] + 111111.01 - 1111.010101010 = [101111.11101011]

4. 111111.0000101 - 111111111 + 111111.0101 = [-110000000.1010011]

5. 101010 + 1111.000001 - 1.00000000000001 = [111000.00000011111111]

"""

from tkinter import *
from tkinter import messagebox

# Вывод информации о программе

def info_about():
    messagebox.showinfo("Информация о программе", "Данная программа выполняет \
сложение и вычитание\nдействительных чисел в двочиной системе \
счисления.\n\nРазработчик: \nРоманов Алексей. Группа ИУ7-23Б.")


# Проверка наличия минуса перед первым знаком

def check_sign(check, number):

    if check == False:
        fin_numb = number
    else:
        fin_numb = "-" + number
    return fin_numb


# Перевод из десятичного числа в двоичное

def to_binary(number):
    
    minus = False
    if str(number)[0] == "-":
        number = float(str(number)[1:])
        minus = True

    Flag = False
    list_point = str(number).split(".")
    bin_number = ""
    try:
        list_point[1] = "0." + list_point[1]
    except:
        Flag = True

    bin_number_point = ""

    while list_point[0] != 0:
        bin_number += str(int(list_point[0]) % 2)
        list_point[0] = int(list_point[0]) // 2
    
    bin_number = bin_number[::-1]

    while Flag == False:
        temp = float(list_point[1]) * 2
        list_point[1] = str(temp) 
        if list_point[1][0] == "1":
            bin_number_point += "1"
            list_point[1] = "0." + list_point[1][2:]
        else:
            bin_number_point += "0"

        for i in range(2, len(list_point[1])):
            if list_point[1][i] == "0":
                Flag = True
            else:
                Flag = False
                break

    if len(list_point) == 2:
        finnaly_number = check_sign(minus, bin_number + "." + bin_number_point)
    else:
        finnaly_number = check_sign(minus, bin_number)

    return finnaly_number    


# Подсчёт результата (в 10 СС)  

def equal(text_in):
   
    global repeat_number

    if text_in == "" or text_in == "-":
        return

    if text_in[len(text_in)-2] == "+" or text_in[len(text_in)-2] == "-":
        text_in = text_in[:len(text_in)-3]

    try:
        text_in = text_in[text_in.index("=")+3:]
    except:
        text_in = text_in
    list_parsing = ["+"]    
    list_parsing += text_in.split()

    if list_parsing[1][0] == "-":
        list_parsing[0] = "-"
        list_parsing[1] = list_parsing[1][1:]

    if len(list_parsing) < 4:
        return

    finnaly_number = 0 

    for i in range(len(list_parsing)):
        number = 0; number_point = 0 
        if list_parsing[i] != "+" and list_parsing[i] != "-":
            list_point = list_parsing[i].split(".")

            for j in range(len(list_point)):
                
                if j == 0:
                    list_point[j] = list_point[j][::-1]
                    power_two = 1
                    number_point = 0
                    for k in range(len(list_point[j])):
                        number_point += int(list_point[j][k]) * power_two
                        power_two *= 2 
                else:
                    power_two = 2
                    number = 0
                    for k in range(len(list_point[j])):
                        number += int(list_point[j][k]) / power_two
                        power_two *= 2
            
            if list_parsing[i-1] == "+":
                finnaly_number += number + number_point
            else:
                finnaly_number -= number + number_point
        
    finnaly_number = to_binary(finnaly_number)
    output["text"] = text_in + " = \n" + str(finnaly_number)


# Парсинг чисел

def parsing(text_in):
    string = ""
    if len(text_in) == 0:
        return string
    i = len(text_in) - 1

    while text_in[i] != " ":
        string += text_in[i]
        i -= 1
        if i == -1:
            break
    return string
    
# Проверка наличия пробела (рабочая функция)

def check():
    text = output["text"]
    if text[len(text)-1] == " ":
        output["text"] = text[:len(text)-1]


# Повторение последнего действия

def repeat_act():
    text_in = output["text"]

    if text_in.count("+") == 0 and text_in.count("-") == 0:
        return
    if text_in[len(text_in)-2] == "+" or text_in[len(text_in)-2] == "-":
        return

    try:
        index_equal = text_in.index("=")
    except:
        index_equal = 0

    if text_in.count(" ", index_equal, len(text_in)) == 1: 
        string_num = ""
        for i in range(index_equal - 1, 0, -1):
            if text_in[i] != "+" and text_in[i] != "-":
                string_num += text_in[i]
            else:
                string_num += text_in[i]
                break
        output["text"] += " " + string_num[::-1]
        check()

    else:
        string_num = ""
        for i in range(len(text_in)-1, -1, -1):
            if text_in[i] != "+" and text_in[i] != "-":
                string_num += text_in[i]
            else:
                string_num += text_in[i]
                break
        
        output["text"] += " " + string_num[::-1]
    

# Добавление символов в строку

def add_sign(num, text_in):
    len_string = len(text_in)
    if text_in[len_string-1] == " ":
        text_in = text_in[:len_string-3]
        text_in += num
    else:
        text_in += num
    output["text"] = text_in
    

# Очистка поля ввода

def clear():
    output["text"] = ""


# Добавление символов (функция кнопок)

def add_symb(char):
    text_in = output["text"]


# Кнопка "0"
    if char == "0":
        last_number = parsing(text_in) 
                
        if len(last_number) == 0 or "1" in last_number \
                             or "." in last_number or "-" in last_number:
            output["text"] += char 

# Кнопка "1"
    elif char == "1":
        last_num = parsing(text_in)
        if len(last_num) == 1 and last_num == "0":
            output["text"] = text_in[:len(text_in)-1] 
        output["text"] += char

# Кнопка "+"
    elif char == " + " and len(text_in) != 0:
        if len(text_in) == 1 and text_in[0] == "-":
            clear()
        else:
            add_sign(char, text_in)

# Кнопка "-"
    elif char == " - " and len(text_in) != 0:
        if len(text_in) == 1 and text_in[0] == "-":
            return
        else:
            add_sign(char, text_in)

# Кнопка "."
    elif char == ".":
        last_number = parsing(text_in)
        last_number = last_number[::-1]
        if len(last_number) != 0  and char not in last_number\
                               and last_number[len(last_number)-1].isdigit():
            output["text"] += char

# Кнопка "-" (перед числом)
    elif char == " - " and len(text_in) == 0:
        output["text"] = "-"


# Создание и настройка окна

root = Tk()
root.title("Calculator")
root.geometry("250x400")
root.maxsize(width="400", height="250")
root.minsize(width="400", height="250")

mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="Повтор действия", command=repeat_act)
mainmenu.add_command(label="Очистить ввод", command=clear)
mainmenu.add_command(label="О программе", command=info_about)

# Инициализация кнопок и их настройка

bg_image = PhotoImage(file="bg_main.png")
bg_label = Label(image=bg_image)

button_one = Button(root, text="1", bg="#B0C4DE", \
        font="Times 24", command=lambda:add_symb("1"))
button_null = Button(root, text ="0", bg="#B0C4DE", \
        font="Times 24", command=lambda:add_symb("0"))
button_plus = Button(root, text="+", bg="#FF8C00", \
        font="Times 15", command=lambda:add_symb(" + "))
button_minus = Button(root, text="-", bg="#FF8C00", \
        font="Times 15", command=lambda:add_symb(" - "))
button_equal = Button(root, text="=", bg="#008B8B", \
        font="Times 30", command=lambda:equal(output["text"]))
button_point = Button(root, text=".", bg="#FF8C00", \
        font="Times 15", command=lambda:add_symb("."))

button_null.place(x=25, y=130, width="180", height="40")
button_one.place(x=207, y=130, width="180", height="40")
button_plus.place(x=65, y=175, width="200", height = "20")
button_minus.place(x=65, y=197, width="200", height ="20")
button_equal.place(x=268, y=175, width="65", height="65")
button_point.place(x=65, y = 220, width="200", height="20")

bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создание и настройка окна вывода

output = Label(bg="#6495ED", font = "Times 12", justify=RIGHT)
output.place(x=25, y=20, height="100", width="360")
root.mainloop()

