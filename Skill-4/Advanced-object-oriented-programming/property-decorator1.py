class Student:
    def __init__(self, name, studentnum):
        self._name = name
        self._studentnum = studentnum

eddie = Student("Eddie", 1234)

print(eddie)
print(eddie._name)
print(eddie._studentnum)