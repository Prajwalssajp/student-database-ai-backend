
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.models.student import Student


def retrieve_student_context(
    db: Session,
    question: str
) -> str:
    """
    Retrieve approved student information
    for the chatbot.
    """

    question_lower = question.lower().strip()

    # Count query
    if "how many" in question_lower or "count" in question_lower:
        total = db.scalar(
            select(func.count()).select_from(Student)
        )

        return f"Total students: {total}"

    # Get available departments safely
    departments = db.scalars(
        select(Student.department).distinct()
    ).all()

    department = None

    for item in departments:
        if item and item.lower() in question_lower:
            department = item
            break

    # Retrieve students
    statement = select(Student).order_by(Student.id)

    if department:
        statement = statement.where(
            Student.department == department
        )

    students = db.scalars(statement.limit(20)).all()

    if not students:
        return "No matching student records found."

    context_lines = []

    for student in students:
        context_lines.append(
            f"Student ID: {student.id}, "
            f"Name: {student.name}, "
            f"Department: {student.department}, "
            f"Year: {student.year}, "
            f"Marks: {student.marks}"
        )

    return "\n".join(context_lines)