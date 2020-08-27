from object_functions_getter import get_object_functions


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'My name is {self.name}')

    @staticmethod
    def say_hi():
        print('hi')

    @classmethod
    def reproduce(cls, name):
        return cls(name, 0)


person = Person('Rafael', 27)
get_object_functions(person)
