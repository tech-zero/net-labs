class Drummer:
    member_type = "Percussionist"
    def __init__(self, style, lead_hand, brand):
        self.style = style
        self.lead_hand = lead_hand
        self.brand = brand
        
    def paradiddle(self):
        if self.lead_hand == "left":
            print("L! R! L! L!")
        else: 
            print("R! L! R! R!")
            
    def introduction():
        print("")
            
buddy_rich = Drummer("jazz", "right", "Slingerland")
buddy_rich.paradiddle()
print(buddy_rich.style)
print(buddy_rich.lead_hand)
print(buddy_rich.brand)