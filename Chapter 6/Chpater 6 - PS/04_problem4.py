# Write a program to find whether a given username contains less than 10 characters or not.

user_name = input("Enter your name: ")

if(len(user_name) >= 10): 
    print("Your name is should less than 10 characters.")
else:
    print("Your name is less than 10 characters you can register.")