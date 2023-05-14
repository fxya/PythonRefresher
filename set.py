def my_first_set():
    return {1, 2, 3}


def my_second_set():
    return {1, 2, 3, 4}


def get_intersection(first_set, second_set):
    return first_set.intersection(second_set)


if __name__ == '__main__':
    print(get_intersection(my_first_set(), my_second_set()))    # {1, 2, 3}
