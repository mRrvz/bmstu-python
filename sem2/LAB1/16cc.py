dict_16 = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
dict_16_reverse = {"10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F"}
temp = 0; answer = ""

def addition(numb1, numb2, temp):
    addened1 = int(dict_16[numb1[len(numb1) - 1]])
    addened2 = int(dict_16[numb2[len(numb2) - 1]])
    fin_number.append((addened1 + addened2 + temp) % 16)
    temp = (addened1 + addened2) // 16

    numb1 = numb1[:len(numb1) - 1]
    numb2 = numb2[:len(numb2) - 1]

    return numb1, numb2, temp
    

def remainder(numb1, temp):
    while temp != 0 and numb1 != "":
        addened = int(dict_16[numb1[len(numb1) - 1]])
        fin_number.append((temp + addened) % 16)
        temp = (temp + addened) // 16
        numb1 = numb1[:len(numb1) - 1]
    
    return numb1, temp

def last_remain(numb1, numb2, temp):
    if temp != 0:
        fin_number.append(temp)
    
    if numb1 != "":
        fin_number.append(numb1[::-1])
    elif numb2 != "":
        fin_number.append(numb2[::-1])


numb1 = input("Введите первое число в 16СС: ")
numb2 = input("Введите второе число в 16СС: ")

fin_number = []
list_numb1 = numb1.split(".")
list_numb2 = numb2.split(".")

if len(list_numb1) != len(list_numb2):
    if len(list_numb2) == 2:
        fin_number.append(list_numb2[1][::-1])
        fin_number.append(".")
    else:
        fin_number.append(list_numb1[1][::-1])
        fin_number.append(".")

    numb1 = list_numb1[0]
    numb2 = list_numb2[0]
    
    while numb1 != "" and numb2 != "":
        numb1, numb2, temp = addition(numb1, numb2, temp)

    if numb1 != "":
        numb1, temp = remainder(numb1, temp)

    elif numb2 != "":
        numb2, temp = remainder(numb2, temp)

    last_remain(numb1, numb2, temp)

    
else:
    numb1 = list_numb1[1][::-1]
    numb2 = list_numb2[1][::-1]
    
    while len(numb1) != len(numb2):
        if len(numb1) > len(numb2):
            fin_number.append(numb1[0]) 
            numb1 = numb1[1:]
        else:
            fin_number.append(numb2[0])
            numb2 = numb2[1:]

    numb1 = numb1[::-1]
    numb2 = numb2[::-1]

    while numb1 != "" and numb2 != "":
        numb1, numb2, temp = addition(numb1, numb2, temp)
    
    fin_number.append(".")

    numb1 = list_numb1[0]
    numb2 = list_numb2[0]

    while numb1 != "" and numb2 != "":
        numb1, numb2, temp = addition(numb1, numb2, temp)
    
    if numb1 != "":
        numb1, temp = remainder(numb1, temp)
    elif numb2 != "":
        numb2, temp = remainder(numb2, temp)
    last_remain(numb1, numb2, temp)


for i in range(len(fin_number)):
    if str(fin_number[i]).isdigit() and 10 <= int(fin_number[i]) <= 16:
        answer += str(dict_16_reverse[str(fin_number[i])])
    else:
        answer += str(fin_number[i])
answer = answer[::-1]

print("Их сумма равна: ", answer)

    
