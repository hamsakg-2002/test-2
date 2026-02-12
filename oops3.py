class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")

    def get_salary(self):
        return self.__salary


# Object creation
emp = Employee("Hamsa", 30000)

print(emp.name)              # public access
print(emp.get_salary())      # controlled access

emp.set_salary(40000)        # valid update
print(emp.get_salary())

       # invalid update