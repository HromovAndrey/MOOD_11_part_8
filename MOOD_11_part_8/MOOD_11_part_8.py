# class MyMeta(type):
#     def __new__(cls, name, bases, dct):
#         print(f"{cls=}")
#         print(f"{name=}")
#         print(f"{bases=}")
#         print(f"{dct=}")
#         return super(). __new__(cls, name, bases, dct)
#
# class Perenta:
#     country = "Ukraine"
#
# class Person(Perenta, metaclass=MyMeta):
#     age = 20
#     name="Mary"
#
#
#     def __init__(self, country="Ukraine"):
#         self.country = country
#
#     def info(self):
#         print(f"Name : {self.name}, age:{self.age}")
#
#
# class MyMeta(type):
#     def __new__(cls, name, bases, dct):
#         dct["country"] = "Ukraine"
#         if "name" not in dct:
#             raise AttributeError("There is no attribute name")
#         return super().__new__(cls, name, bases, dct)
# class Person( metaclass=MyMeta):
#     age = 20
#     name = "Mary"
#
#     def __init__(self, country="Ukraine"):
#         self.country = country
#
#     def info(self):
#         print(f"Name : {self.name}, age:{self.age}")
#
# print(Person.country)

# class MyMeta(type):
#     needed_methods = ["info" "get"]
#     def __init__(cls, name, bases, dct):
#         for method_name in cls.needed_methods:
#             if method_name not in dct:
#                 raise AttributeError(f"There is not method {method_name} in class {name}")
#         return super(). __new__(cls, name, bases, dct)
#
# class Person(metaclass=MyMeta):
#     age = 20
#     name = "Mary"
#
#     def info(self):
#         print(f"Name:{self.name}, age {self.age} ")
#
#     def get


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        for method_name, method in dct.items():
            if callable(method):
                dct[method_name] = cls.meta_decor(method)

        return super(). __new__(cls, name, bases, dct)
    @staticmethod
    def meta_decor(method):
        def decored_method(*args, **kwargs):
            print("hello from metaclass")
            return method(*args, **kwargs)

        return decored_method()


class Number(metaclass=MyMeta):
    value = 10

    def __add__(self, other):
        return self.value + other.value


    def __mul__(self, other):
        return self.value * other.value


    def __sub__(self, other):
        return self.value - other.value

    def __truediv__(self, other):
        return self.value / other.value


num1 = Number()
num2 = Number()
print(num1 + num2)
print(num1 * num2)
print(num1 - num2)
print(num1 / num2)






