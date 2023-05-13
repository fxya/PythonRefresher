class my_class:

    def __init__(self):
        self.internal_variable = {'apple, orange, banana'}

    def update(self, fruit):
        self.internal_variable.add(fruit)

    def __str__(self):
        return f'{self.internal_variable}'  # f-string used to format the string representation of the object


if __name__ == '__main__':
    my_class_instance = my_class()
    print(my_class_instance)
    my_class_instance.update('mango')
    print(my_class_instance)
