# Write a program to find the greatest of four numbers entered by the user.

# numbers = []

# user_numbers = int(input("Enter a number: "))
# numbers.append(user_numbers)
# user_numbers = int(input("Enter a number: "))
# numbers.append(user_numbers)
# user_numbers = int(input("Enter a number: "))
# numbers.append(user_numbers)
# user_numbers = int(input("Enter a number: "))
# numbers.append(user_numbers)

# numbers.sort()

# greatest_number = numbers[(len(numbers)) - 1]
# print("Greatest number is: ", greatest_number)


# We can solve the above problem using following way:
number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))
number4 = int(input("Enter number4: "))

if(number1>number2 and number1>number3 and number1>number4):
    print("The greater number is: ", number1)

elif(number2>number1 and number2>number3 and number2>number4):
    print("The greater number is: ", number2)

elif(number3>number1 and number3>number2 and number3>number4):
    print("The greater number is: ", number3)

elif(number4>number1 and number4>number2 and number4>number3):
    print("The greater number is: ", number4)
