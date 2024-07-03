# map(), filter(), reduce () are higher order functions --> takes function
# as an argument
# we are then converting the sequence into a list by using list()

from functools import reduce


def cube(x):
    return x * x * x


list1 = [1, 2, 3, 5, 6, 2]

# uses cube function on every element of list1 and returns a sequence.
list2 = list(map(cube, list1))
print(list2)


# filter() --> filters a list by checking the elements that qualify a condition
def filter_function(a):
    return a > 4


# uses filter_function on each element, checks if condition met, return sequence
newl = list(filter(filter_function, list1))
print(newl)

numbers = [1, 2, 3, 4, 5]


def mysum(x, y):
    return x + y


# the reduce function applies the argument function to the 1st 2 elements in
# list and then applies the function to the result and the next element
Sum = reduce(mysum, numbers)
print(Sum)