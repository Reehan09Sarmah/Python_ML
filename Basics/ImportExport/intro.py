# import my_module --> to import whole module
import sys

from my_module import find_index  # to import specific things

courses = ['History', 'Physics', 'Math', 'CompSci']

index = find_index(courses,'Math')
print(index)

print(sys.path)

# sys.path --> list of paths where compiler searcher for the module to import
# if files in path that is not there in sys.path, it will not be found -- error
# we can manually add that path to sys.path, so that we can import that module
#  at top of file: import sys then sys.path.append('path') --> not best method

