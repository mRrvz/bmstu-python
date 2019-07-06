def pars(line):
    numb = ''
    while len(line) >= 1 and line[0] != ' ':
        numb += line[0]
        line = line[1:]
    return line[1:], numb

def PrintFile(numb, line):
    print(numb + line, end='')


f1 = open('f1.txt')
f2 = open('f2.txt')
f3 = open('f3.txt', 'a')

line1 = f1.readline()
line2 = f2.readline()

line1, numb1 = pars(line1)
line2, numb2 = pars(line2)

while len(line1) > 0 and len(line2) > 0:

    if numb1 < numb2:
        f3.write(numb1 + ' ')
        line1, numb1 = pars(line1)
    else:
        f3.write(numb2 + ' ')
        line2, numb2  = pars(line2)

if numb1 < numb2:
    f3.write(numb1 + ' ' + numb2 + ' ')
else:
    f3.write(numb2 + ' ' + numb1 + ' ')

if len(line1) != 0:
    f3.write(line1)
else:
    f3.write(line2)

f3.close()
f3 = open('f3.txt')
line3 = f3.readline()
PrintFile('f3.txt - ', line3)
f3.close()
print()
f4 = open('f4.txt', 'a')

while len(line3) > 0:
    line3, numb1 = pars(line3)
    if numb1 not in line3:
        f4.write(numb1 + ' ')

f4.close()
f4 = open('f4.txt')
line4 = f4.readline()
PrintFile('f4.txt - ', line4)
f4.close()
print()

g = open('g.txt', 'a')

while len(line4) > 0:
    line4, numb = pars(line4)
    if int(numb) % 2 == 0:
        g.write(numb + '\n')
    else:
        if int(numb) == 1:
            g.write(numb + ' one \n')
        elif int(numb) == 2:
            g.write(numb + ' two \n')
        elif int(numb) == 3:
            g.write(numb + ' three \n')
        elif int(numb) == 4:
            g.write(numb + ' four \n')
        elif int(numb) == 5:
            g.write(numb + ' five \n')
        elif int(numb) == 6:
            g.write(numb + ' six \n')
        elif int(numb) == 7:
            g.write(numb + ' seven \n')
        elif int(numb) == 8:
            g.write(numb + ' eight \n')
        elif int(numb) == 9:
            g.write(numb + ' nine \n')
        else:
            g.write(numb + '\n')
g.close()
g = open('g.txt')
gline = g.readline()
while gline != '':
    PrintFile('', gline)
    gline = g.readline()

