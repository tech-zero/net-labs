import random

class CreateEmail:
    provider = ["outlook.com", "outlook.co.uk"]
    
    def __init__(self, name):
        self.name = name
        
    def generate(self):
        suffix = random.choice(self.provider)
        email = f"{self.name}@{suffix}"
        return email