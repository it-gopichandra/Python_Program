# to extract the element using tuple.

tpl = ('a', 'b', 'c', 'd')

(first,second,third,fourth) = tpl
print(first)
print(second)
print(third)
print(fourth)

print() # new line

(first,second,*third) = tpl
print(first)
print(second)
print(third)