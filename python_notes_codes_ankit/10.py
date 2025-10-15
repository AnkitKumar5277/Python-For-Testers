# 1. Class and Object
# Class is a blueprint for creating objects. Objects are instances of a class.
class Employee:
    company = "TechCorp"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary

    def increment(self, amount):
        self.salary += amount
        return self.salary

emp1 = Employee("Alice", 30, 50000)
emp2 = Employee("Bob", 25, 45000)

print(f"Employee 1: {emp1.name}, Age: {emp1.age}, Salary {emp1.get_salary()}, Company: {emp1.company}")
print(f"Employee 2: {emp2.name}, Age: {emp2.age}, Salary {emp2.get_salary()}, Company: {emp2.company}")

emp1.increment(5000)
print(f"Employee 1 after increment: {emp1.get_salary()}")

# 2. Class Attribute vs Instance Attribute
# Class attributes belong to the class, instance attributes belong to the object.
class Sample:
    a = "Ankit"
obj = Sample()
obj.a = "Vikky"
Sample.a = "Rohan"
print(f"Class attribute: {Sample.a}")
print(f"Instance attribute: {obj.a}")

# 3. Self Parameter
# 'self' refers to the instance calling the method. It is automatically passed.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

cat = Cat("Whiskers", 3)
cat.info()
cat.make_sound()

# 4. Static Method
# Static methods don’t require self and are decorated with @staticmethod.
class StaticExample:
    @staticmethod
    def greet():
        print("Hello, I am a static method!")

StaticExample.greet()
obj = StaticExample
obj.greet()

# 5. Constructor (__init__)
# Constructor is called automatically when an object is created.
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(f"Programmer {self.name} intialized with salary {self.salary} and pin {self.pin}")
p = Programmer("Ankit", 120000000, 240011)
print(f"{p.name}, {p.salary}, {p.pin}, {p.company}")

r = Programmer("Rohan", 1200000, 340000)
print(f"{r.name}, {r.salary}, {r.pin}, {r.company}")

