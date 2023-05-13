import sys


def print_hi(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    name = sys.argv[1:]
    if name:  # Empty list evaluates to false
        print_hi(''.join(name))
    else:
        print_hi('World')
