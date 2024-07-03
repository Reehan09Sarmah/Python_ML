# a and b are 2 different objects
a = [1, 2, 3]
b = [1, 2, 3]
c = a  # c is now pointing to the same object as a

print(a == b)  # checks value
print(a is b)  # checks type
print(c is a)
