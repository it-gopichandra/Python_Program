# to reverse digit of given number.

n = int(input('Enter the value of n: '))
a = n
rev = 0
while (n > 0):
    rem = n % 10
    rev = (rev*10)+rem
    n //= 10
print("Reverse number of {0} are {1}".format(a, rev))