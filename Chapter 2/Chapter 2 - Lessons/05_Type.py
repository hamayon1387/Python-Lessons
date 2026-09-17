# TYPE() FUNCTION AND TYPECASTING
# type() function is used to find the data type of a given varible in python.

a = 1
print(type(a)) # The output is : <class 'int'>

b = "hamayon"
print(type(b)) # The output is : <class 'str'> 

c = True
print(type(c)) # <class 'boolean or bool'>

d = 23.2
print(type(d)) # <class 'float'>



# We can using from functions like: str(), float(), int() convert a data type to another data types.

e = "23"
print(type(e)) # The output is str
f = int(e) # e varible is now converted to a int or number.
print(type(f)) # The output is int
g = float(e) # g varible is now converted to a float.
print(type(g))
h = bool(e)
print(type(h))


str(31) # integer to string conversion.
int("31") # string to integer conversion.
float("45") # strign to float conversion.
# and so on...