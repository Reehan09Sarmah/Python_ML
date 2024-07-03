import random
import math

import datetime
import calendar

courses = ['History', 'Physics', 'Math', 'CompSci']

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2022))
