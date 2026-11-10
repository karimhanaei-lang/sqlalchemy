from sqlalchemy import create_engine, Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///SchoolData.db', echo=True)

Base = declarative_base()

################################################
# Table 1: students
################################################

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    courses = relationship('Course', back_populates='student',
                           cascade='all, delete-orphan')

################################################
# Table 2: courses
################################################

class Course(Base):
    __tablename__ = 'courses'
    __table_args__ = {'extend_existing': True}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(String)
    unit = Column(INTEGER)
    student_id = Column(INTEGER, ForeignKey('students.id', ondelete='CASCADE'))

    student = relationship('Student', back_populates='courses')

################################################

Base.metadata.create_all(engine)
################################################

Session = sessionmaker(bind=engine)
sessionLocal = Session()
################################################
# Insert Students
################################################

student1 = Student(name='Ali Akbari')
student2 = Student(name='Nima Akbari')

sessionLocal.add_all([student1, student2])
sessionLocal.commit()
################################################
# Insert Courses (student_id -> students.id)
################################################

course1 = Course(title='Python', unit=3, student_id=1)
course2 = Course(title='SQL', unit=2, student_id=1)
course3 = Course(title='Math', unit=4, student_id=2)

sessionLocal.add_all([course1, course2, course3])
sessionLocal.commit()
################################################
# Student -> Courses  (One to Many)
################################################

student1 = sessionLocal.query(Student).filter_by(id=1).first()

if student1 is not None:
    print(student1.name)
    for course in student1.courses:
        print(course.title)
        print(course.unit)
        print('--'*30)
else:
    print('دانش‌آموزی با این id پیدا نشد')
################################################
# Course -> Student  (Many to One)
################################################

course1 = sessionLocal.query(Course).filter_by(id=1).first()

print(course1.title)
print(course1.student.name)
################################################
# Cascade Delete
# (deleting a student also deletes their courses)
################################################

student1 = sessionLocal.query(Student).filter_by(id=1).first()

if student1 != None:
    sessionLocal.delete(student1)
    sessionLocal.commit()


