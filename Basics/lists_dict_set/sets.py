# Sets --> does not store duplicate values --> No Order Maintained
# For empty set --> set_1 = set()
cs_courses = {'Computer Networks', 'Math', 'Data Structures', 'System Software'}
art_courses = {'History', 'Math', 'Geography', 'Design'}
print(f'CS courses: {cs_courses}\nArt Courses: {art_courses}\n')

# set_num = {1, 1, 2, 3, 5, 6, 3, 7, 4, 5, 4}  # will not store the duplicate values
# print(set_num)

# Set methods like Intersection -->To set common from both sets
print(f'Common Courses: {cs_courses.intersection(art_courses)}\n')

# Difference Method --> Not common with other sets
print(f'Present only in CS: {cs_courses.difference(art_courses)}')
print(f'Present only in Art: {art_courses.difference(cs_courses)}\n')

# All the elements together removing duplicates
print(f'Every Courses in CS and Art: {cs_courses.union(art_courses)}')