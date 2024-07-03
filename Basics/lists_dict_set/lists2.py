courses = ['History', 'Math', 'Physics', 'CompSc']
num = [7, 3, 5, 2, 4, 1]

# sort in ascending
courses.sort()
num.sort()
print('Sort Alphabetically(string list) and Ascending order(number list)')
print(courses)
print(num)

# sort in descending
print('Sort Reverse Alphabetically(string list) and Descending order(number list)')
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)

# to get a sorted version of list without altering original list
courses2 = sorted(courses)
num2 = sorted(num)
print(courses2)
print(num2)

# minimum, maximum and sum of the values of numbers list
print('\nMinimum, Maximum and Sum of the values in list "num" ')
print(min(num))
print(max(num))
print(sum(num))

# find index of a certain value
mathIndex = courses.index('Math')
print(f'\nIndex of Math in courses: {mathIndex}')

# To check if an element is in the list or not
print('Art' in courses)
print('Math' in courses)