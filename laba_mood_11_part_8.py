# Завдання 2
# Створіть метаклас, що перевіряє наявність певних
# атрибутів у всіх класах, які використовують цей
# метаклас.
class MetaClass2(type):
    def __init__(cls, name, bases, dct):
        if 'required_attribute' not in dct:
            raise TypeError(f"Class {name} must have a 'required_attribute' attribute")
        super().__init__(name, bases, dct)


class Person(metaclass=MetaClass2):
    age = 20
    name = "Mary"

    def info(self):
        print(f"Name:{self.name}, age {self.age} ")











