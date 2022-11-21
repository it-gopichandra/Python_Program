# to count the digit of a given number.

n = int(input('Enter the value of n: '))
a = n
count = 0
while (n > 0):
    n //=10
    count += 1
print("Count the digit of {0} are {1}".format(a, count))
