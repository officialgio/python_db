from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

Session = sessionmaker(bind = engine)
session = Session()

# Create schools
school1 = School(name="School A")
school2 = School(name="School B")

# Enroll students in schools
student1 = Student(name="Giovanny", school=school1)
student2 = Student(name="Faizaan", school=school2)
student3 = Student(name="Mary", school=school2)

# Create a function to check and update student-school affiliation
def enroll_student_in_school(student, school):
    if student.school and student.school != school:
        raise Exception(f"Student {student.name} is already affiliated with a different school.")
    student.school = school

enroll_student_in_school(student1, school1)
enroll_student_in_school(student2, school2)
enroll_student_in_school(student3, school2)

# Enroll students in courses (many-to-many relationship)
course1 = Course(name="Computer Network")
course2 = Course(name="Machine Learning")
course3 = Course(name="Object-Oriented Design")
course4 = Course(name="Web Development")
course5 = Course(name="Discrete Structures")
course6 = Course(name="Operating System")

student1.courses.extend([course1, course2])
student2.courses.extend([course2, course3])
student3.courses.append(course1)

# Add and commit the changes to the database
session.add_all([school1, 
                 school2, 
                 student1, 
                 student2, 
                 student3, 
                 course1, 
                 course2, 
                 course3, 
                 course4, 
                 course5, 
                 course6])
session.commit()
