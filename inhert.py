# inheritance

# Simple Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# create an object/instance of Animal class
#animal = Animal("Generic Animal")
#animal.speak()


# Derived class
class Dog(Animal): # this can also be said as a problem of constructor overloading. Since Dog class has its own constructor but is also calling animal class inside which 
    def __init__(self): # itself has its own constructor.
        self.behavior = 'friendly'        # here Dog class has its  own constructor. Hence, it will not use the constructor of Animal class. 
                                        # previously it did not had its own constructor and it was using the constructor of animal class. 
    def speak(self):
        print(f"Buddy barks. he is very {self.behavior}.")

# create an object/instance of Dog class
dog = Dog()
dog.speak()

