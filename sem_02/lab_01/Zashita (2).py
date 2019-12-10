from tkinter import *

def abs_transform_to_3sim(number):

    result_number = list()
    number = abs(int(number))

    while number > 0:
        if number % 3 == 0:
            result_number.append("0")
            number //= 3
        elif number % 3 == 1:
            result_number.append("+")
            number //= 3
        elif number % 3 == 2:
            result_number.append("-")
            number = number // 3 + 1

    result_number.reverse()

    return result_number


def transform_to_3sim(number):
    
    result_number = abs_transform_to_3sim(number)
    if int(number) > 0:

        return "".join(result_number)

    elif int(number) < 0:
        for i in range(len(result_number)):
            if result_number[i] == "-":
                result_number[i] = "+"
            elif result_number[i] == "+":
                result_number[i] = "-"

        return "".join(result_number)

    else:
        return 0


def equal(entry_one, entry_two, flag):

    check_t = 0
    
    number_three = 1
    
    final_number_one_10cc = 0; final_number_two_10cc = 0
    text_one = entry_one.get(); text_two = entry_two.get()
    text_one = text_one.replace("-", "t"); text_one = text_one.replace("+", "1")
    text_two = text_two.replace("-", "t"); text_two = text_two.replace("+", "1")
    text_one = text_one[::-1]; text_two = text_two[::-1]

    
    for i in range(len(text_one)):
        if text_one[i] == "t":
            final_number_one_10cc -= number_three
        elif text_one[i] == "1":
            final_number_one_10cc += number_three

        number_three *= 3

    number_three = 1

    for i in range(len(text_two)):
        if text_two[i] == "t":
            final_number_two_10cc -= number_three
        elif text_two[i] == "1":
            final_number_two_10cc += number_three

        number_three *= 3

    if flag == "+":
        final = final_number_one_10cc + final_number_two_10cc
    elif flag == "*":
        final = final_number_two_10cc * final_number_one_10cc

    final = transform_to_3sim(final)

    label_second["text"] = "Ответ: " + str(final)

    
def flag_func(flag):
    if flag == "Сложить":
        label["text"] = "+"
    elif flag == "Умножить":
        label["text"] = "*"

def add_symb(symb):
    entry_one.insert(0, END, symb)
    

root = Tk()
root.geometry("400x250")

button_plus = Button(root, text ="Сложить", font="Times 15", command=lambda:flag_func("Сложить"))
button_umn = Button(root, text= "Умножить", font="Times 15", command=lambda:flag_func("Умножить"))

button_minus = Button(root, text ="+", font="Times 15", command=lambda:flag_func("+"))
button_null = Button(root, text ="0", font="Times 15", command=lambda:flag_func("+"))
button_plus_ = Button(root, text ="-", font="Times 15", command=lambda:flag_func("+"))

button_plus.place(x=25, y=5, width=140)
button_umn.place(x=235, y=5, width=140)

entry_one = Entry(root)
entry_one.place(x=25, y=50)

entry_two = Entry(root)
entry_two.place(x=25, y=70)

text_one = entry_one.get()
text_two = entry_two.get()

button_equal = Button(root, text="=", font="Times 15", command=lambda:equal(entry_one, entry_two, label["text"]))
button_equal.place(x=170, y=5, width=60)

label = Label(root, text="+", font="Times 15")
label_second = Label(root, text="Ответ: ", font="Times 15")
label_second.place(x=0, y=100, width = 200)
label.place(x =150, y=60)

root.mainloop()
