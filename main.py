# Class definitions
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
instance1 = MyClass('Gav', '21')
instance2 = MyClass('Sue', '31')

class MyClassWithMethod():

    species = 'Human' # Class atrribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printNameandAge(self):
        print("Name is: " + self.name, "Age is: " + self.age + " " + self.species)
    
    def __str__(self):
        return "Name is: " + self.name, "Age is: " + self.age + " " + self.species

instance1 = MyClassWithMethod('Gav', '21')
instance2 = MyClassWithMethod('Sue', '31')

instance1.printNameandAge()

# Inheritance

class NewClass(MyClassWithMethod):
    pass

n1 = NewClass('Bob', '42')

print(n1.printNameandAge())