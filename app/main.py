
from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.student import Student
from app.api.students import router as student_router
from app.api.chat import router as chat_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Database Application System",
    description="Modular backend with CRUD APIs and AI chatbot integration",
    version="1.0.0"
)

app.include_router(student_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "Student Database API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }