from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from db_create import Base
from sqlalchemy.orm import relationship

class School(Base):
    __tablename__ = "school"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship("Student", back_populates="school")

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    school_id = Column(Integer, ForeignKey("school.id"))
    school = relationship("School", back_populates="students")
    courses = relationship("Course", secondary="student_course_association")

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


# Here is used an association table. I learned how to do this from: https://www.youtube.com/watch?v=47i-jzrrIGQ&t=189s
student_course_association = Table(
    "student_course_association",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("student.id")),
    Column("course_id", Integer, ForeignKey("course.id"))
)