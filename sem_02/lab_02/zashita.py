from tkinter import *

def change_text(list_to_sort):

    for i in range(len(list_to_sort)):
        label_sort["text"] += str(list_to_sort[i]) + " "

    label_sort["text"] += "\n\n"

    
def bubble_sort(entry):
    label_sort["font"] = "Arial 10"
    list_to_sort = entry.get()
    list_to_sort = list(map(int, list_to_sort.split()))
    #print(list_to_sort)

    label_sort["text"] = ""
    change_text(list_to_sort)
    count = 0
    
    for i in range(len(list_to_sort)):
        barrier = True
        for j in range(len(list_to_sort) - 1):
            count += 1
            if list_to_sort[j + 1] < list_to_sort[j]:
                list_to_sort[j + 1], list_to_sort[j] = list_to_sort[j], list_to_sort[j + 1]
                barrier = False

        change_text(list_to_sort)
        
        if barrier:
            break

    if count == len(list_to_sort) - 1:
        label_sort["font"] = "Arial 12"
        label_sort["text"] = ""
        change_text(list_to_sort)
        label_sort["text"] += "\n\nМассив уже отсортирован!"
    else:
        label_sort["text"] += "Количество итераций: " + str(count)
    

root = Tk()
root.geometry("600x300")
root.maxsize(width=300, height=600)
root.minsize(width=300, height=600)
root.title("Сортировка пузырьком с баррьером")

entry_array = Entry(root)
start_sort = Button(root, text="Сортировать!", command=lambda:bubble_sort(entry_array))
label_sort = Label(root, text="Введите массив для сортировки", justify=CENTER, font="Arial 10", bg="green")

label_sort.place(x=20, y=90, width=265, height=490)
entry_array.place(x=10, y=18, width=280)
start_sort.place(x=10, y=40, width=280, height=30)
