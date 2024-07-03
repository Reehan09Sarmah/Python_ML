def hello(name):
    print(f'Hello {name}!')


def returnSum(a, b):
    return a + b


hello('Reyhan')
print(returnSum(2, 3))


def hello_func(greeting, name='You'):
    return f'{greeting} {name}'


print(hello_func('Hello', 'reehan').upper())


