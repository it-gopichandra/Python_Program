# to find the sum of digit of given number.

n = int(input('Enter the value of n: '))
a = n
sum = 0
while (n > 0):
    rem = n % 10
    sum += rem
    n //= 10
print("Sum of digit of given number {0} are {1}".format(a, sum))
