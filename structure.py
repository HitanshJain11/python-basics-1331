class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

student = Student("Rahul", 101, 85)

print("Student Name:", student.name)
print("Roll Number:", student.roll_no)
print("Marks:", student.marks)