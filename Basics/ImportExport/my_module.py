print('Importing my module....')

test = 'Test String'


# Search for an element in a list and return a string stating its index
def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return f'It is index: {i}'

    return -1
