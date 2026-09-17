# LIST METHODS IN PYTHON
# Consider the following list

l1 = [1,8,7,2,21,15]
print(l1)


# 1. SORT() METHOD: Updates the list to [1, 2, 7, 8, 15, 21]
l1.sort()
print(l1)

# 2. REVERSE() METHOD: Updates all lists to [21, 15, 8, 7, 2, 1]
l1.reverse()
print(l1)

# 3. APPEND() METHOD: We can using from this method add items at the end of a list.
l1.append("Hamayon")
print(l1)


# 4. INSERT METHOD: .insert() method is used to add an item at a specific position (index) in a list.
fruits = ["Apple", "Banana", "Orange"]
print(fruits)
fruits.insert(2, "Mango")
print(fruits)


# 5. POP METHOD: In this method we gave index for pop method and pop method find the value of that index and remove it and this method remove's return value.
l2 = ["hamayon", "ahmad", "mahmod", "ali", 'reza', "malek"]
print(l2)
removed_item = l2.pop(3)
print(removed_item)


# 6. REMOVE METHOD: We can remove an item of a list using from this method. But this method removes the items using from values not indexs.
students = ["ahmad", "ali", "karim", "timor", "murad"]
print(students)
removed_std = students.remove("ali")
print(removed_std) # output : None // because remove() method is not return the remove item like pop() method.

# 7. INDEX() METHOD: Find the index of a value inside an array.
friends = ["ali", "azeem", "bahram", "hamed", "osman"]
print(friends)
index = friends.index("bahram")
print(index)


# DIFFERENCE BETWEEN sort(reverse = True) and reverse() function
# 1. numbers.sort(reverse = True)
numbers = [1, 3, 5, 9, 2, 11, 34]
numbers.sort(reverse = True)
print(numbers)
# RESULT = [34, 11, 9, 5, 3, 2, 1]
# If we use from this syntax, It sorts the numbers from largest to smallest.

# 2. .reverse()
numbers2 = [2, 34, 21, 12, 11, 9]
numbers2.reverse()
print(numbers2) # output : [9, 11, 12, 21, 34, 2]
# It simply reverses the existing order.



# COUNT() FUNCTION : Count how many times a value appears
num1 = [1, 21, 12, 11, 8, 5, 9, 1, 7, 12, 8]
print("Count of 12 in num2 list is:", num1.count(12))
# count() function is helpful whin working with repeated data.


# 10. EXTAND() FUNCTION: Add multiple items
list1 = ["Tobah", "Jeran", "Muzhgan"]
list2 = ["Hamayon", "Ali", "Reza"]
