from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

Session = sessionmaker(bind = engine)
session = Session()

# Find students taking ML
students_taking_machine_learning = (
    session.query(Student)
    .join(Course, Student.courses)
    .filter(Course.name == 'Machine Learning')
    .all()
)

for student in students_taking_machine_learning:
    print(f"Student Name: {student.name}")
    