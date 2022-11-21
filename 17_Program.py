# find weather give input are character.

ch=input('Type something: ')
if(ch>='a'and ch<='z')or(ch>='A'and ch<='Z'):
    print("The given character",ch,"is alphabet")
else:
    print("The given character",ch,"is not alphabet")