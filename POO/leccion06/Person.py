class Person:

    # Una variable de clase se comparte para todos objetos de la clase de tipo Person
    countPersons: int = 0

    @classmethod
    def genereteNextValue(cls):
        cls.countPersons += 1
        return cls.countPersons

    def __init__(self, name, age) -> None:
        # Person.countPersons += 1
        self.idPerson = Person.genereteNextValue()
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f'Person [{self.idPerson} {self._name} {self._age}]'


personOne = Person('Carlos', 54)
print(personOne)
personTwo = Person('Giovanna', 21)
print(personTwo)
personThree = Person('Antonio', 42)
print(personThree)
print(f'Count value persons: {Person.countPersons}')
