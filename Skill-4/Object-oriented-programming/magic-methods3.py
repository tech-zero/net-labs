class Student:
    def __init__(self, age, course):
        self.age = age
        self.course = course
    def __str__(self):
        return f"I am student, aged {self.age}, and I am studying {self.course}"
        
sylvia = Student(47, "computer science")
eddie = Student(51, "network engineering")

print(sylvia)
print(eddie)