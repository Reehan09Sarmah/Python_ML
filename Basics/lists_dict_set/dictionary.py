# dictionary is a key-value pair list--> mostly like a JS object
student = {'name': 'John', 'age': 20, 'courses': ['Math', 'CompSci']}
# 'Not Found' is written as a second parameter in case no key matches, it'll print out this
print(student.get('name', 'Not Found'))

student['phone'] = '98567-67523'

# to update multiple key-value, use .update
student.update({'name': 'Reehan', 'age': 21, 'phone': '98436-23419'})
print(student)

# to delete a key ---> del student['age']
# to delete and get returned the value of key
age = student.pop('age')
print(age)

# to get only keys
print(student.keys())

# to get values only
print(student.values())

# to get both --> each pair
print(student.items())
print('\n')
# to loop through
print('Keys and Values')
for key,value in student.items():
    print(f'{key} ---> {value}')