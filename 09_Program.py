# to print total, average and percentage of some subject
eng = int(input("Enter minimum marks of English: "))
hin = int(input("Enter minimum marks of Hindi: "))
math = int(input("Enter minimum marks of Maths: "))
pcb = int(input("Enter minimum marks of Science: "))
comp = int(input("Enter minimum marks of Computer: "))
max = int(input("Enter maximum marks of Exam: "))

total = eng + hin + math + pcb + comp
print('The total marks is', total)

avg = total // 5
print('The average marks is', avg)

perc = (total * 100) / max
print('Your percentage is', perc)