'''
Composition allows us to model objects 
which has a "Has A" type of relationship
'''

class Payment:
    def __init__(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        
    def salary(self):
        return (self.wage * 52) + self.bonus

class Person:
    def __init__(self, name, height, wage, bonus):
        self.name = name
        self.height = height
        self.obj_payment = Payment(wage, bonus)

    def yearly_wage(self):
        return self.obj_payment.salary()
    
brandon = Person("Brandon", 70, 500, 5000)
brandon_total_wage = brandon.yearly_wage()
print(brandon_total_wage)