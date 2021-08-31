class Person:

    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    # overload method operator add
    def __add__(self, other):
        return f'{self._name} {other._name}'

    # overload method operator sub
    def __sub__(self, other):
        return self._age - other._age

personOne = Person('Alberto', 10)
PersonTwo = Person('Charles', 30)
print(personOne + PersonTwo)
print(personOne - PersonTwo)


# obj1 + obj2

# This syntx is not necesary
# obj1.__add__(obj2)