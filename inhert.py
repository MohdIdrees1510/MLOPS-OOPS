# inheritance

# Simple Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# create an object/instance of Animal class
animal = Animal("Generic Animal")
animal.speak()


# Derived class
class Dog(Animal):

    def speak(self):
        print(f"{self.name} barks")

# create an object/instance of Dog class
dog = Dog("Buddy")
dog.speak()

