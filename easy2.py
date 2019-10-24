
while True:
    intege = input("Please enter a year : ")
    if not intege:
        break
    year = int(intege)

    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(year, ' -> true')
    else:
        print(year, ' -> false')