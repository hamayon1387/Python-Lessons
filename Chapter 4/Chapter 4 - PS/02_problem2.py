# Write a program to accept marks of 6 students and display them in a stored manner.

marks = []

mark1 = int(input("Enter marks1: "))
marks.append(mark1)
mark2 = int(input("Enter marks2: "))
marks.append(mark2)
mark3 = int(input("Enter marks3: "))
marks.append(mark3)
mark4 = int(input("Enter marks4: "))
marks.append(mark4)
mark5 = int(input("Enter marks5: "))
marks.append(mark5)
mark6 = int(input("Enter marks6: "))
marks.append(mark6)
mark7 = int(input("Enter marks7: "))
marks.append(mark7)

marks.sort()
print(marks)