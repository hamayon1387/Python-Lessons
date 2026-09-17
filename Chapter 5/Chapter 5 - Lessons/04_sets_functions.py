# Operators in Set

# 1. LEN() METHOD: Return the length of the set.
s = {1, 8, 2, 3}
# print(s)
s_length = len(s)
# print(s_length)

# 2. REMOVE() METHOD: The remove() method is used to remove a specific element from a set and update it.
s1 = {1, 2, 3, 2, 5, 7, 0}
s1.remove(2)
# print("You can see 2 is removed: " ,s1)

# ADD() METHOD: Usen for adding elements on a set.
set1 = {1, 2, 3}
# print(set1)
set1.add(4)
# print("You can see 4 is added: ", set1)

# POP() METHOD : Removes an arbitary(random) element from the set and return the removed element.
set2 = {1, 23, 34, 2}
# print(set2)
set_pop = set2.pop()
print(set_pop) # output : 1 because it's removed and pop return it.
# print(set2)