
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)
from app.crud import student as student_crud

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    student = student_crud.create_student(db, student_data)

    return student


@router.get(
    "",
    response_model=list[StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):
    return student_crud.get_students(db)


@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = student_crud.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = student_crud.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    try:
        return student_crud.update_student(
            db,
            student,
            student_data
        )
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = student_crud.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student_crud.delete_student(db, student)

    return None