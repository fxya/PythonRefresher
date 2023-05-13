def my_function():
    return lambda x: x * 2  # my_function returns a lambda function


if __name__ == '__main__':
    print(my_function()(10))
