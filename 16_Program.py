# to check palendrome number.

n = int(input('Enter the value of n: '))
a = n
rev = 0
while (n > 0):
    rem = n % 10
    rev = (rev*10)+rem
    n //= 10
if(a==rev):
    print("Input number is palendrome.")
else:
    print("input number is not palendrome")
    