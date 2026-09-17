# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1,2]}

# No — and there is an important problem with your example.

# s = {8, 7, 12, "Harry", [1, 2]}

# This will actually produce an error:

# TypeError: unhashable type: 'list'
# Why?

# A Python set can only contain hashable (immutable) objects.

# A list is mutable, meaning its contents can be changed:

# my_list = [1, 2]
# my_list[0] = 100

# Because lists can change, Python does not allow them as elements of a set.

# So this is invalid:

# s = {8, 7, 12, "Harry", [1, 2]}
# #                                  ❌ list inside set
# What about a tuple?

# A tuple is immutable, so it can be inside a set:

# s = {8, 7, 12, "Harry", (1, 2)}

# Then:

# s.add((3, 4))

# works.

# But you cannot do:

# s[0] = ...

# because sets don't support indexing, and tuples themselves cannot be modified.

# The key rule

# Set elements must be hashable. Lists are not hashable because they are mutable.

# So the answer to your question is: you cannot have a list inside a normal Python set in the first place, therefore you cannot change a list contained in that set.