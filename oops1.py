class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
# Creating object of the class
s1 = Student("Hamsa", 101)
# Calling method
s1.display()