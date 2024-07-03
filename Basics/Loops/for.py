numb = [1, 2, 3, 4, 5]

for num in numb:
    if num == 3:
        print('Found')
        break
    print(num)

for num in numb:
    if num == 2:
        print("It's the one")
        continue
    print(num)

print('\n')

for num in numb:
    for letter in 'abc':
        print(f'{num} -> {letter}')

# using range --> 1 to 11-1=10
for i in range(1, 11):
    print(i)
