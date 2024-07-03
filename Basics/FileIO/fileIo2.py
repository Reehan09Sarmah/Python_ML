# seek() and tell() functions are used to work with file objects and their
# positions within a file

with open('file.txt', 'r') as f:
    print(type(f))

    f.seek(5)  # tells file pointer to move to that position
    print(f.tell())  # tells us the pointer position at the current moment
    data = f.read(15)  # read 10 bytes/characters from where file pointer points to
    print(data)
    print(f.tell())


# Now in the above given code :
# we did f.seek(5) --> file pointer moves to 5th character in file
# print(f.tell()) --> prints 5
# then we read 15 characters of data using file pointer, so fp moves 15 more
# characters to read
# print(f.tell()) --> prints 20


# The truncate() method resizes the file to the given number of bytes.
# If the size is not specified, the current position will be used.

with open('sample.txt', 'w') as file:
    file.write('Hello World!')
    file.truncate(5)  # truncate/limit to only 5 bytes/characters

with open('sample.txt', 'r') as file:
    print(file.read())

