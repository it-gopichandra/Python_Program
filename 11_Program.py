# to print the sum of n even number upto n.

n = int(input('Enter the value of n: '))
sum = 0
for i in range(1, n+1):
    if (i % 2 == 0):
        sum += i
print('Sum of all even number is', sum)