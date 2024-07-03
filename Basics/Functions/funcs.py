def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Reehan', age=20)

# args take in the positional parameters while kwargs takes on the keyword ones
# args make them into tuple while Kwargs makes them into dictionary
# So use the * and ** logically


courses = ['Math', 'Art']
info = {'name': 'Reehan', 'age': 20}

# student_info(courses, info) --> would not do as all the values
# will be unpacked by * and put into tuple
# So to specify

student_info(*courses, **info)  # courses -> tuple, info -> dictionary

# Date functions --> return number of days in a month in a particular year
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


year = int(input('Enter the year: '))
month = int(input('Enter Month Number: '))
print(f'It is a leap year? {is_leap(year)}')
print(f'Days in Month: {days_in_month(year, month)}')
