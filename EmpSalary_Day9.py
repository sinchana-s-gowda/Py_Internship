class EmployeeSalary:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, salary):
        self.employees[name] = salary

    def display_employees(self):
        print(self.employees)

    def update_salary(self, name, new_salary):
        if name in self.employees:
            self.employees[name] = new_salary

    def delete_employee(self, name):
        if name in self.employees:
            del self.employees[name]


emp = EmployeeSalary()
emp.add_employee("XYZ", 50000)
emp.add_employee("ABC", 60000)
emp.display_employees()
emp.update_salary("XYZ", 55000)
emp.delete_employee("ABC")
emp.display_employees()