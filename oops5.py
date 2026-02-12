# encapsulation
class Employee:
    def __init__(self,name,salary):
      self.name = name
      self._salary = salary
    def set_salary(self ,amount):
        if amount > 0:
            self._salary = amount
        else:
            print("invalid salary amount")
    def get_salary(self):
        return self._salary
emp = Employee("hamsa",800000)
print(emp.name)
print(emp.get_salary())