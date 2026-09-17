# Operators in Python
# Following are some common operators in Python:
# 1. Arethmatic Operators: +, -, *, / etc...
# 2. Assignment Opeators: =, +=, -= and etc...
# 3. Comparison Operators: == , >= , <= , != , and etc...
# 4. Logical Operators: and, or, not


# 1. Arithmatic Operators:
a = 2
b = 5
c = a + b # Assign it The some of the a and b varibles to c varible.
print(a + b) # print the result of the a and b plus operator.

# 2. Assignment Operators
d = 34 - 23 # assign it the result of the 34 - 23 to d.
print(d)

e = 10
e += 3 # Encrement the value of b by 3 and then assign it to e.
print(e)

f = 5 # The value of f is 5 now.
f -= 2 # Decrement the value of f by 5 and then assign it to f.
print(f)

g = 10 
g *= 10 # Multiple the value of g by 10 and then assign it to g.
print(g)

h = 12
h /= 3 # Devid the value of g by 10 and then assign it to g.
print(h)

# 3. Coparison Operators
# Comparison Operator is used to compare the operators. and the output of comparison operator is boolean.

i = 3 > 4 # 3 is not gratre than 4 then output of this comparison operator is False.
print(i)

j = 9 > 2 # 9 is gratre than 2 then output of this comparison operator is True.
print(j)

k = 12 >= 12 # 12 is greater than or equal to 12 then output of this comparison operator is True.
print(k)

l = 34 <= 33 # 34 is less than or equal 33 then output of this comparison operator is False.
print(l)

m = 3 != 4 # 3 is not equal to 4 then output is True.
print(m)


# 4. Logical Operators 
n = True or False # The output is True. Because the or operator is return if one of the boolean is are true.
print(n)

# The truth table of 'or'
print("True or false is : ", True or False) # true
print("False or True is : ", False or True) # True
print("True or True is : ", True or True) # True
print("False or Flase is : ", False or False) # False


# The truth table of 'and'
print("True and false is : ", True and False) # False
print("False and True is : ", False and True) # False
print("True and True is : ", True and True) # True 
print("False and Flase is : ", False and False) # False


print("The not of True is : ", not(True))
print("The not of False is : ", not(False))