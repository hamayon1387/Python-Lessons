# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take ahmads_mark as an
# input from the user.

# ahmads_mark = {}
# ahmads_total_mark = 0

# subject = input("Enter the subject: ")
# mark = int(input(f"Enter your score from {subject}: "))
# ahmads_mark.update({subject: mark})
# ahmads_total_mark += mark

# subject = input("Enter the subject: ")
# mark = int(input(f"Enter your score from {subject}: "))
# ahmads_mark.update({subject: mark})
# ahmads_total_mark += mark

# subject = input("Enter the subject: ")
# mark = int(input(f"Enter your score from {subject}: "))
# ahmads_mark.update({subject: mark})
# ahmads_total_mark += mark

# subject = input("Enter the subject: ")
# mark = int(input(f"Enter your score from {subject}: "))
# ahmads_mark.update({subject: mark})
# print("Marks of the Ahmad is: ", ahmads_mark)


# ahmads_total_mark += mark
# ahmads_average_marks = ahmads_total_mark/3
# print(ahmads_average_marks)

# if(ahmads_average_marks <= 33):
#     print("you fail in exam")
# else:
#     print("Congradulations you pass from exam! and your average marks is: ", ahmads_average_marks)


marks = {}

subject1 = input("Enter your subject: ")
mark1 = int(input("Enter mark1: "))
marks.update({subject1: mark1})

subject2 = input("Enter your subject: ")
mark2 = int(input("Enter mark2: "))
marks.update({subject2: mark2})

subject3 = input("Enter your subject: ")
mark3 = int(input("Enter mark3: "))
marks.update({subject3: mark3})


average = (mark1 + mark2 + mark3) / 3


if mark1 < 0 or mark1 > 100 or \
   mark2 < 0 or mark2 > 100 or \
   mark3 < 0 or mark3 > 100:

    print("Marks must be between 0 and 100.")

elif average >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33:

    print(f"Congratulations! You passed: {average}")
    print(f"Your results: {marks}")

else:

    print(f"You failed. Try again next year: {average}")
    print(f"Your results: {marks}")