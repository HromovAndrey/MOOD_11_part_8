# Завдання 3
# Реалізуйте метаклас, що забороняє спадкування від
# певних класів чи змінює порядок спадкування.

class ForbiddenSubclass(type):
    def __subclasscheck__(cls, subclass):
        if cls.forbidden_class in subclass.__mro__:
            print(f"Subclassing from {cls.forbidden_class.__name__} is not allowed.")
            return False
        return True

class BaseClass:
    pass

class ForbiddenClass(BaseClass, metaclass=ForbiddenSubclass):
    pass
class AllowedClass(BaseClass):
    pass
class SubclassOfForbidden(ForbiddenClass):
    pass
class SubclassOfAllowed(AllowedClass):
    pass










