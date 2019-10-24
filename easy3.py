import sys

step = input("Please enter a number : ")
intege = int(step)


# 3.1
def solution_3_1(intege):
    for i in range(intege):
        for j in range(i + 1):
            sys.stdout.write('*')
        print('')


# 3.2
def solution_3_2(intege):
    for i in range(intege):
        intege = int(step) - i
        for intege in range(intege - 1, 0, -1):
            sys.stdout.write(' ')
        for j in range(i + 1):
            sys.stdout.write('*')
        print('')


#3.3
def solution_3_3(intege):
    amount = 0
    for i in range(intege):
        intege = int(step) - i
        for intege in range(intege - 1, 0, -1):
            sys.stdout.write(' ')
        sys.stdout.write('*')
        for k in range(i + amount):
            sys.stdout.write(' ')
        if i != 0:
            sys.stdout.write('*')
            amount += 1
        print('')



# 3.4
def solution_3_4(intege):
    intege = int(step)
    star1 = 0
    star2 = intege - 1
    for i in range(intege):
        for j in range(intege):
            if ((j == star1) or (j == star2)):
                sys.stdout.write('*')
            else:
                sys.stdout.write(' ')
        print('')
        star1 += 1
        star2 -= 1



#3.5
def solution_3_5(intege):
    intege = int(step)
    x = int(float(intege / 2) + 0.5)
    l = 0
    a = 0
    for i in range(intege):
        for j in range(intege):
            if (j + 1 <= x + l and j + 1 >= x - l):
                sys.stdout.write('*')
            else:
                sys.stdout.write(' ')
        print('')
        if (i >= x - 1 or a == 1):
            if (intege % 2 == 0 and a==0):
                l += 1
            l -= 1
            a = 1
        else:
            l += 1


# 3.6
def solution_3_6(intege):
    intege = int(step) * 2 - 1
    x = int(float(intege / 2) + 0.5)
    l = 0
    z = 0
    letter1 = 'A'
    letter2 = 'B'
    for i in range(intege):
        for j in range(intege):
            if (j + 1 == x + l or j + 1 == x - l):
                sys.stdout.write('+')
            elif (j + 1 <= x + l and j + 1 >= x - l):
                sys.stdout.write('E')
            elif (j + 1 <= x - l):
                sys.stdout.write(letter1)
            elif (j + 1 >= x + l):
                sys.stdout.write(letter2)
        print('')
        if (x + l == intege or z == 1):
            l -= 1
            z = 1
            letter1 = 'C'
            letter2 = 'D'
        else:
            l += 1


solution_3_1(intege)
