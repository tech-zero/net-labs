'''
Inheritence allows us to model objects which 
has an 'Is A' relationship.
'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sounds(self):
        return "WOOF!"

class Frenchie(Dog): # Inherits the name of the class 'Dog'
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def sounds(self):     #This method will overwrite the inherited Dog.sounds() method 
        return "YAP YAP"  # since it is more specific
    def breathing(self):
        return "Gremlin"

murphy = Frenchie("Murphy", 1)  #Enters the name of the Frenchie dog named "Murphy", who is 1 year old
print(murphy.name)
print(murphy.age)
print(murphy.sounds())  #Calls the 'sounds method from the class 'Dog'
print(murphy.breathing(), "\n") #Calls the 'breathing' method from the class 'Dog'

zeus = Dog("Zeus", 2)
print(zeus.name, zeus.age, zeus.sounds(), sep="\n", end="\n") 