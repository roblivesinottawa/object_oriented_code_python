class Employee:
    employee_count = 0

    def __init__(self, fullname, salary):
        self.fullname = fullname
        self.salary = salary
        Employee.employee_count += 1

    def displayCount(self):
        return f"Total Employee: {Employee.employee_count}"

    def displayEmployee(self):
        return f"Name: {self.fullname}, Salary: {self.salary}"


# create instances

employee_one = Employee("John Doe", 75000)
print(employee_one.displayCount())
print(employee_one.displayEmployee())