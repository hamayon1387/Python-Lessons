# SETS IN PYTHON: Set is a collection of non-repetitive elements.


s = {1, 2, 3, 5, 6, 6}
print(s, type(s))

s2 = {2, 3, 5, 12, "Hamayon", "Ahmad", "Mahmod", True, False, 34.34, 89, 9} # Set is are unordered => Element's order doesn't matter.
print(s2, type(s2))



# Properties Of Sets
# Sets are unordered => Element’s order doesn’t matter
# Sets are unindexed => Cannot access elements by index
# There is no way to change items in sets.
# Sets cannot contain duplicate values


s3 = {} # For making empty set don't use s3 = {} it will create a empty dictionary.
print(s3)
s4 = set()
print("it's an empty set: ", s4)
