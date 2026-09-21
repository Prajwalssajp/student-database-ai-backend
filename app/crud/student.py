
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


def create_student(db: Session, student_data: StudentCreate):
    student = Student(**student_data.model_dump())

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


def get_students(db: Session):
    statement = select(Student).order_by(Student.id)
    return db.scalars(statement).all()


def get_student_by_id(db: Session, student_id: int):
    return db.get(Student, student_id)


def update_student(
    db: Session,
    student: Student,
    student_data: StudentUpdate
):
    update_data = student_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student


def delete_student(db: Session, student: Student):
    db.delete(student)
    db.commit()