# lambda functions are small anonymous functions without a name
# defined using the 'lambda' keyword followed by the syntax
# use when oneliner function needed, as an argument you pass a function

# def double(x):
#     return x * 2

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y: (x + y) / 2

print(double(5))
print(avg(34.5, 45.7))


def appl(fx, value):
    return 6 + fx(value)


print(appl(cube, 5))
