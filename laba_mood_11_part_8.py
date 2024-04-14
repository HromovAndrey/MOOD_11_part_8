# Завдання 4
# Створіть метаклас, який автоматично реєструє всі
# нові класи у певному реєстрі для подальшого
# використання.

class ClassRegistry(type):
    registry = {}

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        ClassRegistry.registry[name] = cls
class MyClass1(metaclass=ClassRegistry):
    pass

class MyClass2(metaclass=ClassRegistry):
    pass
print(ClassRegistry.registry)






