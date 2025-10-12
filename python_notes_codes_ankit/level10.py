# 1. Class and Object
# Class is a blueprint for creating objects. Objects are instances of a class.
class Employee:
    # Class attribute (shared by all objects)
    company = "TechCorp"

    def show_details(self):
        print(f"Employee works at {self.company}")

emp1 = Employee()   # instance attribute
emp2 = Employee()
emp1.show_details()
emp2.show_details()

# 2. Class vs Instance Attributes
# Class attributes belong to the class, instance attributes belong to specific objects
class Sample:
    a = "Ankit" #class attribute

# creating an object
obj = Sample()
obj.a = "Vikky" #instance attribute
Sample.a = "Rohan" # changing class attribute

print(Sample.a)
print(obj.a)

# 3. Self Parameter
# Self refers to the instance calling the method
class Cat:
    def __init__(self, name, age):
        self.name = name #instance
        self.age = age #instance

    def info(self):
        print(f"i am a cat. My name is {self.name} i am {self.age} years old")

#creating object and calling method
cat1 = Cat("Whiskers", 3)
cat1.info()

# Creating object and calling method
cat1 = Cat("Whiskers", 3)
cat1.info()

# 4. static method
# Static methods don't use self and are marked with @staticmethod
class StaticExample:
    @staticmethod
    def greet():
        print("Hello from static method !")

obj = StaticExample()
obj.greet()
StaticExample.greet()

# calling static method without self
obj = StaticExample()
obj.greet()
StaticExample.greet()

# 5. Constructor (__init__)
# Constructor initializes objects when they are created
class Programmer:
    company = "Microsoft" # class attribute

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    def show_info(self):
        print(f"name : {self.name}, salary: {self.salary}, pin : {self.pin}, company : {self.company}")

p1 = Programmer("Ankit", 12000000, 23424)
p2 = Programmer("Hayy", 12000403, 34242)
p1.show_info()
p2.show_info()

# 6. Modelling a Problem in OOP
# Nouns -> Class (e.g., Car)
# Adjectives -> Attributes (e.g., color, speed)
# Verbs -> Methods (e.g., drive, stop)
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        print(f"the {self.color} car is driving at {self.speed} km/n")

    def stop(self):
        print(f"the {self.color} car has stopped")

    #creating object and using methods
car1 = Car("Red", 120)
car1.drive()
car1.stop()

