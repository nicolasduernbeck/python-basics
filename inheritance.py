class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job


employeeOne = Employee("Anna", 20, "Pilot")
print(employeeOne.age, employeeOne.name, employeeOne.job)
