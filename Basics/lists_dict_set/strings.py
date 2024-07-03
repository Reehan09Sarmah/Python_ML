message = 'Hello World'
print(message)
# slicing
print(message[0:5])
print(message[6:])

# Using methods
print(message.lower())  # to lowercase
print(message.upper())  # to UPPERCASE

print(message.count('l'))  # count number of 'l' present

# replaces a part with our given part and returns a new string
newMessage = message.replace('World', 'Universe')
print(newMessage)

# formatted string
msg = f'{message},{newMessage}. Welcome!'
print(msg)

# print all the attributes and methods available
# print(dir(message))
# print(help(str)) --> help for string


