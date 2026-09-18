# 5. Write a program which finds out whether a given name is present in a list or not.

names = ["hamayon", "ali", "hamid", "ahmad", "shafiq", "hasib", "bahram", "hamed"]


user = input("Enter your name to find out it: ")

if(user in names or user.capitalize()):
    print("your name is found")
    print(f"Name is you want to find out it: \"{user}\"")
else:
    print("Your name is not found from our list")
    print(f"Name is you want to find out it: \"{user}\"")