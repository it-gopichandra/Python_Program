# to access then replace, insert & delete element in tuples.

tpl = ('a', 'b', 'c', 'd', 'e')

li = list(tpl)
li[1] = 'x'
tpl = tuple(li)
print (tpl)

li = list(tpl)
li.append('z')
tpl = tuple(li)
print (tpl)

li = list(tpl)
li.remove('e')
tpl = tuple(li)
print (tpl)
