language = 'Python'

if language == 'python':
    print(True)
elif language == 'Python':
    print(True)
else:
    print(False)

# Truthy Values: Values that evaluate to True
# -->True, Non-Empty sequences or collections, Numeric values != 0

# Falsy Values: Values that evaluate to False
# --> Empty sequences or collections, Numeric values = 0 (any type), None, False

user = 'Admin'
pwd = 'admin123'
loggedIn = False

if user == 'Admin' and pwd == 'admin12':
    loggedIn = True
    print('Admin Page')
else:
    loggedIn = False
    print('Bad Credentials. Try  Again!')


if not loggedIn:
    print('Please Log In')
else:
    print('Already Logged In')