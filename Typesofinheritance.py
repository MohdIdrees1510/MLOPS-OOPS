# single or basic inheritence

#class parent:
#    def __init__(self, name):
#        self.name = name

#    def greet(self):
#        print(f"Hello my name is {self.name}.")

#class child(parent):
    
#    def play(self):
#        print(f"{self.name} is playing.")

#kid = child("Alice")
#kid.greet()
#kid.play()

# Multilevel inheritance

# class Grandparent:
#    def __init__(self, name):
#        self.name = name

#    def tell_a_story(self):
#        print(f"{self.name} tells a story every night.")

# class Parent(Grandparent):

#    def work(self):
#        print(f"{self.name}'s kids goes to work everyday.")

# class Child(Parent):

#    def play(self):
#        print(f"{self.name}'s grandchildrens plays everyday.")

#child = Child("Iqbal")
#child.tell_a_story()
#child.work()
#child.play()



# Heirarchical

#class Parent:
#    def __init__(self, name):
#        self.name = name

#    def greet(self):
#        print(f"my name is {self.name}")

#class child1(Parent):

#    def work(self):
#        print(f"{self.name} is working.")

#class child2(Parent):
    
#    def play(self):
#        print(f"{self.name} is playing.")

#child1 = child1("Hasan")
#child2 = child2("Hussain")

#child1.greet()
#child1.work()

#child2.greet()
#child2.play()

# Multiple (Diamond Problem)

class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A. {self.name}")

class B(A):
    def greet(self):
        print(f"Hello from B. {self.name}")
        super().greet()

class C(A):
    def greet(self):
        print(f"Hello from C. {self.name}")
        super().greet()

class D(B, C):
    def greet(self):
        print(f"Hello from D. {self.name}")
        super().greet()

d = D("Iqbal")
d.greet()