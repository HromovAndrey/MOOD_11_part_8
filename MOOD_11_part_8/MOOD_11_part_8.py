# class MyMeta(type):
#
#     def __new__(cls, name, bases, dct):
#          print(dct)
#         return super(). __new__ (cls, name, bases, dct)
#     @staticmethod
#     def cache_decor(method):
#         def decor_method(*args, **kwargs):
#             cache_data = (method.__name__, *args, tuple(kwargs.items)
#
#
#             if cache_data in MyMeta.cache:
#                 print("known data")
#                 return MyMeta.cache[cache_data]
#             result = method
#
# class Number:
#    value = 10
#
#     def __add__(self, ):
#     def __mul__(self, other):
#         return self.value - other.value
#
#
# class InfoSystem:
#     def add(self, num1, num2):
#         return num1 + num2
#
#
# obj =   InfoSystem()
# print(InfoSystem.add (2,2))
# print(InfoSystem.add (2,2))
# print(InfoSystem.add (2,2))
# print(InfoSystem.add (2,2))
# for date, result in MyMeta.cache.items():
#     print(data, result)

class MetaClass1(type):
    def __new__(cls, name, bases, dct):
        # Додаємо додатковий функціонал до всіх класів
        dct['additional_functionality'] = lambda self: (
            print("Additional functionality added!"))
        return super().__new__(cls, name, bases, dct)


class MyClass1(metaclass=MetaClass1):
    pass

# Використання
obj = MyClass1()
obj.additional_functionality()  # Виведе "Additional functionality added!"






