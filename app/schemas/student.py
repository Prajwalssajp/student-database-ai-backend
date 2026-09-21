
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(..., ge=16, le=100)
    department: str = Field(..., min_length=2, max_length=100)
    year: int = Field(..., ge=1, le=6)
    marks: float = Field(..., ge=0, le=100)


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    email: EmailStr | None = None
    age: int | None = Field(None, ge=16, le=100)
    department: str | None = Field(None, min_length=2, max_length=100)
    year: int | None = Field(None, ge=1, le=6)
    marks: float | None = Field(None, ge=0, le=100)


class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)