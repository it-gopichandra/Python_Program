# to diaplay N natural number.

n = int(input('Enter the value of n: '))
print('table of {0} is...'.format(n))
for i in range(1, 11):
    print('{0}*{1}={2}'.format(n, i, n*i))
