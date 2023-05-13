def my_tuple():
    return 1, 2, 3, 4, 5


# reverse using slicing
def reverse_tuple(tuple):
    return tuple[::-1]  # [start:stop:step] -1 means reverse


if __name__ == '__main__':
    print(reverse_tuple(my_tuple()))
