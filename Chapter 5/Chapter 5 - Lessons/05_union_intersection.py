# UNION() FUNCTION : Returns a new set with all items from both set.
s1 = {1, 23, 1, 3}
# print("this s1: ", s1)
s2 = {2, 1, 23, 1, 5}
# print("this is s2: ", s2)
s3 = s1.union(s2)
# print("This is s3: ", s3)


# INTERSECTION() METHOD: Returns a new set with commonly items between 2 set.
s4 = {2, 3, 4}
print("s4 is: ", s4)
s5 = {1, 2, 3}
print("s5 is: ", s5)
s6 = s4.intersection(s5)
print("common values in s4 and s5 is: ", s6)