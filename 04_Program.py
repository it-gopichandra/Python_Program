# to find the greatest among three number
x = int(input("Enter number value of x: "))
y = int(input("Enter number value of y: "))
z = int(input("Enter number value of z: "))

if x > y and x > z :
    print('{0} is greater than {1} and {2}'.format(x,y,z))
elif y > z and y > x :
    print('{1} is greater than {2} and {0}'.format(x,y,z))
else :
    print('{2} is greater than {0} and {1}'.format(x,y,z))