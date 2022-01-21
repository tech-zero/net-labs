# Part 1
class Human:
    _needs = ["air", "water", "food"]
    def __init__(self, name):
        self._name = name
    
    @classmethod
    def needs(cls):
        return cls._needs
    
eddie = Human("eddie")
print(eddie._needs)

eddie._needs = ["pizza", "ice cream", "beer"]
print(eddie._needs)

print(eddie.needs())

'''
Part 2
Class methods are very useful for calling up factory methods
and uses the (cls) argument.
'''
class Fashion:
    def __init__(self, style):
        self.style = style
    
    @classmethod
    def funky(cls):
        return cls(["bellbottoms", "flowery shirt", "big boots"])
    
    @classmethod
    def gothic(cls):
        return cls(["trenchcoat", "leather jacket", "doc martin boots"])

    @classmethod
    def casual(cls):
        return cls(["t-shirt", "jeans", "sneakers"])
swimwear = Fashion(["trunks", "towel"])
print(swimwear)

funky_fred = Fashion.funky() # call the 'funky' method
print(funky_fred.style)

gothic_gary = Fashion.gothic() # call the 'gothic' method
print(gothic_gary.style)

casual_carl = Fashion.casual() # Calls the 'casual' method
print(casual_carl.style)