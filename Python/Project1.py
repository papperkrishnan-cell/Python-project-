class Company:
    def __init__(self, name, loc, dir, management):
        self.name = name
        self.loc = loc
        self.dir = dir
        self.management = management

class Employee:
    def __init__(self, name, emp_id, age, com: Company):
        self.name = name
        self.id = emp_id
        self.age = age
        self.company = com

    def showDetails(self):
        print(f"Name: {self.name}\nID: {self.id}\nCompany Name: {self.company.name}")
        print(f"Location: {self.company.loc}")

# Objects Creation
c_object = Company("abcd", "Calicut", "xyz", "Ajay")
e1 = Employee("Mitun", 101, 25, c_object)

# Display Details
e1.showDetails()
