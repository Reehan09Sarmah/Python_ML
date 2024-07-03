# using with and as, we do not need to close files here.

# with open('test.txt', 'a') as f:
#     f.write('\nDr. Engineers!')

# using read() , readline(), etc
file = open('test.txt', 'r')
while True:
    line = file.readline()  # read line by line
    if not line:
        break
    print(line)

file.close()


# using readline()
File = open('myfile.txt', 'r')
i = 0
while True:
    i = i + 1
    line = File.readline()
    if not line:
        break
    # split() takes each element separated by the character and makes a list
    # for eg: line --> 12,123,34 will become [12, 123, 34]. Access like lists
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f'Marks of student {i} in Maths: {m1}')
    print(f'Marks of student {i} in English: {m2}')
    print(f'Marks of student {i} in SST: {m3}')


# using writeLine()

f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
