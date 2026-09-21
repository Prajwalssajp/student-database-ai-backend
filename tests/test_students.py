from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_student():
    student_data = {
        "name": "Test Student",
        "email": "test_student_2026@example.com",
        "age": 21,
        "department": "Computer Science",
        "year": 3,
        "marks": 85.5
    }

    response = client.post("/students", json=student_data)

    assert response.status_code in [201, 409]

    if response.status_code == 201:
        data = response.json()

        assert data["name"] == student_data["name"]
        assert data["email"] == student_data["email"]
        assert "id" in data


def test_get_all_students():
    response = client.get("/students")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_student_not_found():
    response = client.get("/students/999999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"