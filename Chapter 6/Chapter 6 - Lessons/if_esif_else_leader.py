# If elif else leader

age = int(input("Enter your age: "))
if(age>= 18):
    print("You are above the age of consent")
elif(age<0):
    print("You are entering an invalid negative age")
elif(age == 0):
    print("You are entering 0 which is not a valid age")
else:
    print("Your age is smaller than consent age")



# Quick Quiz: Write a program to print yes when the age entered by the user is greater than or equal to 18.
a = int(input("Enter your age: "))
if(a >= 18):
    print("Yes")