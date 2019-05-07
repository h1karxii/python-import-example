import sys


def lib1_print(str='call lib1_print'):
    print(str)


print('==========')
lib1_print('In lib1.py')
print(sys.path)
print('==========')