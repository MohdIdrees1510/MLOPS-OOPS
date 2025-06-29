# Super keyword

# Parent class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. He is a {self.breed}.")

dog = Dog("Golden Retriever")
dog.speak()
