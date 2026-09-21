# Student Database Application System – AI Backend

A modular backend application built with **FastAPI** for managing student records through CRUD APIs and an AI-powered chatbot using **Google Gemini** and **LangGraph**.

## Features

- Student CRUD operations
- FastAPI REST APIs
- Automatic Swagger/OpenAPI documentation
- SQLAlchemy database integration
- Pydantic request and response validation
- Gemini-powered student database assistant
- LangGraph workflow with retrieval and answer-generation nodes
- Greeting handling for common greetings
- Basic automated API tests with pytest
- Environment-based configuration for the Gemini API key

## Technology Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **Pydantic / Pydantic Settings**
- **Google GenAI SDK**
- **LangGraph**
- **SQLite** (based on the local `students.db` database)
- **Pytest**
- **HTTPX**

> **Note:** `chromadb` is currently listed in `requirements.txt`, but the supplied chatbot implementation retrieves context directly from the SQLAlchemy database. ChromaDB should not be described as an active part of the chatbot until it is integrated into the code.

## Project Structure

```text
student-database-ai-backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── chat.py
│   │   └── students.py
│   ├── chatbot/
│   │   ├── graph.py
│   │   ├── state.py
│   │   └── tools.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── crud/
│   │   └── student.py
│   ├── models/
│   │   └── student.py
│   ├── schemas/
│   │   ├── chat.py
│   │   └── student.py
│   └── services/
│       └── gemini.py
├── data/
├── tests/
│   ├── test_main.py
│   └── test_students.py
├── .gitignore
├── requirements.txt
└── students.db
```

## Student Data Fields

The student schema contains:

| Field | Description | Validation |
|---|---|---|
| `id` | Student identifier | Automatically generated |
| `name` | Student name | 2–100 characters |
| `email` | Student email | Valid email format; unique in database |
| `age` | Student age | 16–100 |
| `department` | Academic department | 2–100 characters |
| `year` | Academic year | 1–6 |
| `marks` | Student marks | 0–100 |

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-database-ai-backend.git
cd student-database-ai-backend
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Do not commit `.env` to GitHub. The API key must remain private.

### 5. Start the application

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

### General Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the API is running |
| GET | `/health` | Returns health status |

### Student CRUD Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students` | Creates a student |
| GET | `/students` | Returns all students |
| GET | `/students/{student_id}` | Returns a student by ID |
| PUT | `/students/{student_id}` | Updates a student |
| DELETE | `/students/{student_id}` | Deletes a student |

### Create Student Example

```http
POST /students
Content-Type: application/json
```

```json
{
  "name": "Test Student",
  "email": "student@example.com",
  "age": 21,
  "department": "Computer Science",
  "year": 3,
  "marks": 85.5
}
```

### Error Handling

- `404 Not Found`: Student record does not exist
- `409 Conflict`: Email already exists during an update
- `201 Created`: Student successfully created
- `204 No Content`: Student successfully deleted

## AI Chatbot

The chatbot endpoint is:

```text
POST /chat
```

### Request

```json
{
  "message": "How many students are there?"
}
```

The `message` field must contain between 1 and 1,000 characters.

### Response

```json
{
  "response": "There are ... students in the database."
}
```

The exact answer depends on the records stored in the database.

## LangGraph Workflow

The chatbot is implemented using a simple LangGraph workflow:

```text
START
  |
  v
retrieve
  |
  v
generate
  |
  v
END
```

### Retrieve Node

The retrieve node:

- Checks for count-related questions
- Counts students using SQLAlchemy
- Detects department names mentioned in the question
- Retrieves student records from the database
- Limits retrieved student records to 20
- Produces text context for the generation step

### Generate Node

The generate node:

- Receives the user question
- Receives the retrieved database context
- Sends a prompt to Google Gemini
- Instructs the model to use only the supplied context
- Returns the generated answer

The prompt also instructs the assistant not to invent student records and not to reveal unnecessary private information.

### Greeting Handling

Common greetings such as the following are handled directly:

- `hi`
- `hello`
- `hey`
- `hii`
- `good morning`
- `good afternoon`
- `good evening`

## Testing

Run the tests using:

```powershell
python -m pytest -v
```

The current test suite covers:

- Root endpoint
- Health endpoint
- Student creation
- Retrieving all students
- Student-not-found handling

## Database

The application uses SQLAlchemy and creates database tables through:

```python
Base.metadata.create_all(bind=engine)
```

The local project currently includes a SQLite database file named `students.db`.

For production use, database configuration should be managed through environment variables and migrations should be considered.

## Vector Database Research

ChromaDB is included in the dependency list for possible vector database functionality. The current chatbot implementation retrieves student context directly from SQLAlchemy rather than using vector search.

Possible future use cases for a vector database include:

- Semantic search over student-related documents
- Retrieval of policy or academic documents
- Embedding-based question answering
- Retrieval-Augmented Generation (RAG)

Any vector database integration should be implemented and tested before being described as a completed feature.

## Future Improvements

- Add more automated CRUD and chatbot tests
- Add authentication and authorization
- Add structured logging
- Add database migrations
- Add pagination and filtering
- Add a production database configuration
- Integrate and evaluate a vector database
- Add Docker support
- Add CI/CD using GitHub Actions
- Improve chatbot intent detection and response validation

## Security Notes

- Keep the Gemini API key in `.env`
- Never commit `.env` to GitHub
- Use separate development and production credentials
- Add authentication before exposing sensitive student data publicly
- Avoid returning unnecessary personal information through the chatbot

## Project Status

The project currently includes a modular FastAPI backend, student CRUD APIs, a Gemini and LangGraph chatbot, and basic automated tests.
