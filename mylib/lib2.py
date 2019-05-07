import sys


def lib2_print(str='call lib2_print'):
    print(str)


if __name__ == '__main__':
    print('==========')
    lib2_print('In lib2.py')
    print(sys.path)
    print('==========')