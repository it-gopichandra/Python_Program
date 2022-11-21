# to print to check prime number.

n = int(input('Enter the value of n: '))
f = 0
for i in range(2, (n//2) + 1):
    if (n % i) == 0:
        f = 1
        print('Number is not prime')
        break
    if (f == 0):
        print("Number is prime.")
