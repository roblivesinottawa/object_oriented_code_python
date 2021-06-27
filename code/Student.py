class Student:
    def __init__(self, fname, lname, age, grade):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"The student's name is {self.fname} {self.lname} and they are {self.age} years old. Their grade is {self.grade}."





student_one = Student("Steve", "Rogers", 15, 87.9)
student_two = Student("Carol", "Denvers", 17, 96)

print(student_one)
print(student_two)