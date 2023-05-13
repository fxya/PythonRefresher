import string


def filter_names():
    names = ['Alice', 'Bob', 'Frances', 'Grace', 'Charles', 'Debbie', 'Edward']
    return [n for n in names if len(n) <= 5]


def reverse_name(name):
    return ''.join(name)[::-1]  # [start:stop:step] -1 means reverse


if __name__ == '__main__':
    filtered_names = filter_names()
    reversed_name: string = reverse_name(filtered_names[0:1])  # slicing [start, stop] returns a list

    print(f'Filtered names: {filtered_names}')
    print(f'Reversed name: {reversed_name}')
