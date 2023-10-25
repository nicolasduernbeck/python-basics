class Dog:
    name = "Bello"


theDog = Dog()
print(Dog.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello {self.name}")


personOne = Person("Peter", 30)
personOne.greet()
