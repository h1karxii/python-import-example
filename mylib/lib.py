import sys


def lib_print(str='call lib_print'):
    print(str)


print('==========')
lib_print('In lib.py')
print(sys.path)
print('==========')