# Multy if statement:


age = int(input("Enter your age: "))

# What happen if I write here another if statement for age value:

# if statement no : 1
if(age%2 == 0):
    print("age is even")
# end of if statement no : 1


# if statement no : 2
if(age>= 18):
    print("You are above the age of consent")

elif(age<0):
    print("You are entering an invalid negative age")

elif(age == 0):
    print("You are entering 0 which is not a valid age")

else:
    print("Your age is smaller than consent age")
# end of if statement no : 1

# We can make also another if statements 