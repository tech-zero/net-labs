class Dog:
    kind = "canine"
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
d = Dog("Kiko", "Blue_heeler", 5)

print(d.name)
print(d.breed)
print(d.age)

e = Dog("Daisy", "Mixed_breed", 10)
print()
print(e.name)
print(e.breed)
print(e.age)