from sqlalchemy import create_engine, Column, INTEGER, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ۱. ایجاد موتور ارتباطی و دیتابیس
engine = create_engine('sqlite:///StudentsSimple.db', echo=True)
Base = declarative_base()

# ۲. تعریف جدول Student (طبق دستور: id, name, score)
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String)
    score = Column(INTEGER)

# ساخت جدول در دیتابیس
Base.metadata.create_all(engine)

# ایجاد Session برای عملیات
Session = sessionmaker(bind=engine)
session = Session()

################################################
# عملیات Create: اضافه کردن دانش‌آموز جدید
################################################
def create_student(name, score):
    new_student = Student(name=name, score=score)
    session.add(new_student)
    session.commit()
    print(f"دانش‌آموز {name} با موفقیت اضافه شد.")

################################################
# عملیات Read: گرفتن لیست تمام دانش‌آموزان
################################################
def read_all_students():
    students = session.query(Student).all()
    print("\n--- لیست تمام دانش‌آموزان ---")
    for s in students:
        print(f"ID: {s.id} | Name: {s.name} | Score: {s.score}")
    print("---------------------------\n")

################################################
# عملیات Update: تغییر نام یا نمره
################################################
def update_student(student_id, new_name=None, new_score=None):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        if new_name:
            student.name = new_name
        if new_score is not None:
            student.score = new_score
        session.commit()
        print(f"اطلاعات دانش‌آموز {student_id} به‌روزرسانی شد.")
    else:
        print("دانش‌آموز پیدا نشد.")

################################################
# عملیات Delete: حذف دانش‌آموز با id
################################################
def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"دانش‌آموز {student_id} با موفقیت حذف شد.")
    else:
        print("دانش‌آموز پیدا نشد.")
        # --- تست عملیات ---

# ۱. تست Create
create_student('Ali', 18)
create_student('Sara', 20)
create_student('Reza', 12)

# ۲. تست Read
read_all_students()

# ۳. تست Update (تغییر نمره علی به ۱۹)
update_student(1, new_score=19)

# ۴. تست Delete (حذف رضا)
delete_student(3)

# مشاهده نتیجه نهایی
read_all_students()