# LEN() FUNCTION IN PYTHON
F_name = "ahmad"
print(len(F_name)) # We use from len function to understand how many chracters in a string.


# ENDSWITH() FUNCTION
my_name = "hamayon"
print(my_name.endswith("yon")) # This function is return boolean like true or false
print(my_name.endswith("abc"))


# STARTSWITH() FUNCTION
name = "mahmod"
print(name.startswith("mah")) # It's return true because the name varicle is starts with "mah" characters. 
print(name.startswith("abc")) # It's return false because the name varicle is not starts with "abc" characters.


# COUNT() FUNCTION
name2 = "Hi I am good good"
print(name2.count("g"))


# CAPITALIZE() FUNCTION
capitalize = "hamayon"
print(capitalize.capitalize()) # This function capitalize the first letter of a word or sentence.

# TITLE() FUNCTION 
title = "hamayon I am good good"
print(title.title()) # This function is capitalize the first letter of every word in a content.

# UPPER() FUNCTION
sbs = "smart bit system"
print(sbs.upper()) # This function is convert all of the characters of a string to uppercase.


# LOWER() FUNCTION 
sms = "SCHOOL MANAGEMENT SYSTEM" # This function is convert all of the characters of a string to lwercase.
print(sms.lower())



str = " Hamayon is a good good boy "
print(str.strip()) # Remove whitespace from left and right. Becarecul this function is not remove whitespaces between two words.
print(str.rstrip()) # This function's remove the whitespaces from right.
print(str.lstrip()) # This function's remove the whitespaces from left.
print(str.replace("Hamayon", "Jamayon")) # Output: Jamayon
print(str.split())
print("Python is fun".split())
print(str.find("y")) # This function's used for finding a letter and word between a sentence. If the find value is not found this function's return -1. but the index function is not return -1 it's return an error.
print(str.index("H"))
print(str.join())