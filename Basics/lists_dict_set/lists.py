# Lists --> Like Arrays
# if --> list1 = list2, then making changes to list1, changes list2 as list1 is just referring to same list in memory
# indexes from left element starts from 0, from right starts from -1
# For empty list --> list_1 = [] or = list()
courses = ['History', 'Math', 'Physics', 'CompSc']
courses2 = ['History', 'Math', 'Physics', 'CompSc']

print(courses[0:])
print(courses[2:3])

# insert to end of list
courses.append('Art')
print(courses)

# insert anything to specified index of list
print('\nInserting element into the end of list:')
courses.insert(0, 'SSCD')
print(courses)

# let's add a list inside the list
print('\nInserting list into a list in a specific index:')
courses_2 = ['Computer Networks', 'Accounting and Financial Management']
courses.insert(2, courses_2)
print(courses)
print(courses[2])

# extend the list by adding elements of another list to it
print('\nExtending lists:')
print(courses2)
courses2.extend(courses_2)
print(courses2)

# remove elements by their value
print('\nRemoving elements by variable value')
courses.remove(courses_2)
print(courses)

print('\nRemoved Math: ')
courses.remove('Math')
print(courses)

# to remove last element
print(f'\nThe List: {courses2}')
course = courses2.pop()
print(f'Popped Course: {course}')