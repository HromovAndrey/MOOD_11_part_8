# Завдання 1
# Задайте метаклас, що автоматично додає
# додатковий функціонал до всіх класів, що його
# використовують.цуву
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['additional_functionality'] = lambda self: print("Additional functionality added!")
        return super().__new__(cls, name, bases, dct)
class MyMeta(metaclass=MyMeta):
    pass

obj = MyMeta()
obj.additional_functionality()




