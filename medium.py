import sys

intege = int(input("Please enter a number : "))

sys.stdout.write('%s -> ' % intege)
for i in range(2, intege):
    prime = []
    amount = 0
    for j in range(2, intege):
        if i % j == 0:
            prime.append(i)
            amount += 1
    if (amount < 2):
        sys.stdout.write("%s " % i)
