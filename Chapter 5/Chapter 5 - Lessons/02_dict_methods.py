# DICTIONARY METHODS
std_info = {
    "name": "Hamayon",
    "from": "AFG",
    "id": 1387,
    "marks": [99, 100, 99]
}

# 1. ITEM() FUNCTION
# print(std_info.items(), type(std_info.items())) # Returns a list of(key, value) tuples.


# 2. KEYS() METHOD
# print(std_info.keys()) # Returns a list containing dictionary's keys.


# 3. UPDATE() METHOD
# std_info.update({"marks": [98, 99, 90], "degree": "first"}) # Adds new data or changes existing data.
# print(std_info) 


# Let's use this dictionary throughout: 
student = {
    "name": "Hamayon",
    "age": 18,
    "marks": 85,
    "city": "Kabul",
    "grade": "A"
}

# 4. GET() METHOD
# Gets a value from a key without causing an error if the key doesn't exist.

# print(student.get("name")) # Hamayon

# print(student.get("grade")) # None
# print(student.get("grade", "Not available"))
# Not available // Because Python is can't find the grade key and give us Not available.



# 5. POP() METHOD: Removes a key and return it's value.
# print(student) # You can see after the poping the grade key from student dictionary grade key-value is removed but POP() METHOD return the grade value.
# grade = student.pop("grade")
# print(grade)
# print(student)

# phone = student.pop("phone", "Not found")
# print(phone) # output : Not found // If Python is not found the phone key inside the student dectionary POP() method is return the "Not found".


# 6. .popitem() ⭐

# Removes and returns the last key-value pair. And return value of the POPITEM() METHOD is tuple.

# item = student.popitem()

# print(item, type(item))

# DIFFERENCE BETWEEN POP AND POPITEM METHOD: pop method remove key and value and returns value of the removed key if we gave them a key of the dictionary. But popitem method removes last key and value pairs of a dictionary, and the pop method is doesn't need an argument.


# 8. .setdefault() ⭐

# Gets a value if the key exists. If it doesn't, it creates the key with a default value.

# student.setdefault("country", "Afghanistan")

# print(student)

# student.setdefault("name", "Ahmad")
# print(student)


# 9. .copy()

# Creates a copy of the dictionary.

# student_copy = student.copy()
# print(student_copy)
# print(student)
# This is useful when you want another dictionary without modifying the original.



# 10. .clear()

# Removes everything from the dictionary.

# my_info = {
#     "name": "Hamayon",
#     "age": 18,
#     "marks": 85,
#     "city": "Kabul",
#     "grade": "A"
# }

# my_info.clear()

# print("When a dictionary is cleared remaining is an empty brackets: ", my_info)

# Result: {}



# 🔥 The ones I want you to master first

# Don't treat all of these equally.

# Method	Importance	Main job
# .get()	⭐⭐⭐	Safely get a value
# .items()	⭐⭐⭐	Get key + value
# .update()	⭐⭐⭐	Add/change data
# .keys()	⭐⭐	Get keys
# .values()	⭐⭐	Get values
# .pop()	⭐⭐	Remove a specific key
# .copy()	⭐⭐	Copy dictionary
# .setdefault()	⭐	Get/create a key
# .popitem()	⭐	Remove last pair
# .clear()	⭐	Empty dictionary


# FORMKEYS() METHOD: It creates a new dictionary using a list/collection of keys, and gives all those keys the same value.

personal_info = {
    "name": "Hamayon",
    "last_name": "Nadim",
    "Age": 18,
    "from": "AFG"
}

print(personal_info)
keys = ["favorate_colors", "skills", "face_color"]
print(personal_info.fromkeys(keys, "Unknown"))
print(personal_info)