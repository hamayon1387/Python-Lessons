# 7. Write a program to find out whether a given post is talking about “Harry” or not.

capitalize = "Hamayon"
lower = "hamayon"

post = input("Enter your post: ")
if(capitalize in post or lower in post):
    print("This post is about Hamayon.")
else:
    print("This post is not about Hamayon.")