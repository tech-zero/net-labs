class Guitarist:
    member_type = "Guitars"
    def __init__(self, style, guitar, brand):
        self.style = style
        self.guitar = guitar
        self.brand = brand
    
        
eddie = Guitarist("rock", "lead", "Ibanez")

print(eddie.style)
print(eddie.guitar)
print(eddie.brand)
print()

sylvia = Guitarist("rock", "rythm", "Fender")

print(sylvia.style)
print(sylvia.guitar)
print(sylvia.brand)