# open(par1, par2) --> par1 = File, par2 = Mode in which file should be opened
# mode --> r = read(default),
# w = write (write new data into file by replacing initial data),
# a = append (to add into end of file)


file = open('test.txt', 'r')
text = file.read()
print(text)
file.close()

file2 = open('testWrite.txt', 'w')
file2.write(text)
file2.close()

Str = 'Hello Dear!'

file2 = open('testWrite.txt', 'a')
file2.write(Str)
file2.close()
