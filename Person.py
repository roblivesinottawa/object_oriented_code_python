class Person:
    def __init__(self, first_name, last_name, age, height, ehtnicity):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.height = height
        self.ethnicity = ehtnicity

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old. They are {self.height} tall and {self.ethnicity}."

class Student(Person):
    def __init__(self, first_name, last_name, age, height, ehtnicity, graduation):
        super().__init__(self, first_name, last_name, age, height, ehtnicity)
        self.graduation = graduation

    def __str__(self):
        return f"student {self.first_name} is currently taking {self.graduation} classes at UCLA."

class Employee(Person):
    def __init__(self, first_name, last_name, age, height, ehtnicity, graduation):
        super().__init__(self, first_name, last_name, age, height, ehtnicity, college, company_name, salary, position)
        self.college = college
        self.company_name = company_name
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"Employee {self.first_name} {self.last_name} has been an employee at {self.company} for 5 years. {self.first_name} is a graduate of {self.college}."


# create instances of the class Person
iron_man = Person("Tony", "Stark", 45, "6ft", "White")
captain_america = Person("Sam", "Wilson", 35, "6ft", "Black")
print(iron_man)
print(captain_america)
