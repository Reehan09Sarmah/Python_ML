courses = ['History', 'Math', 'Physics', 'CompSc']

# looping through items
for item in courses:
    print(item, '\n')

# using enumerate, by default start is 0, but we can specify what it should start from
for index, course in enumerate(courses, start=1):
    print(index, ': ', course)
print('\n')

# using join --> Take the elements of a list and join them with the specified character and make into a string
course_str = ','.join(courses)
print(course_str, '\n')

# using split to split the string based on the given character and make it into a list
newCourseList = course_str.split(',')
print(newCourseList)
