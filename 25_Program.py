# to insert & delete elements in list.

li = ['A', 'B', 'C', 'D', 'E']

print("\nInsert an element the list...")
li.insert(0,'w') # insert on selected location
li.append('h') # insert in last
print (li)

print("\nDelete an element the list...")
li.remove('w') # delete by element
print(li)

li.pop(1) # delete by index
print(li)

del li[0]
print (li)

li.clear()
print(li)

