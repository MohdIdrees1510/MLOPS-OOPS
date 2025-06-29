# initiate a class
class employee:
    # sepcial method/ magic method /dunder method
    def __init__(self):
        print("initializing the attributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("atributes have been initialized")

    def travel(self, destination):
        print("calling the method/function manually")
        print(f"sam is travelling to {destination}")

# creating an object
sam = employee()

# attributes
#print(sam.designation)

# function/method
#sam.travel("kerala")

print(type(sam))