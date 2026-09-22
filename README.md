
# Student Database Application System – AI Backend

A modular backend application built with **FastAPI** for managing student records through CRUD APIs and an AI-powered chatbot using **Google Gemini**, **LangGraph**, and **ChromaDB**.

The system supports student record management, structured database retrieval, semantic student search, and natural-language answers through an AI chatbot.

---

## Features

### Student Management

- Create student records
- Retrieve all students
- Retrieve a student by ID
- Update student information
- Delete student records
- Email uniqueness validation
- Request and response validation using Pydantic
- Automatic synchronization of student records with ChromaDB

### AI-Powered Chatbot

- Google Gemini-powered natural-language responses
- LangGraph workflow for retrieval and answer generation
- Greeting handling for common greetings
- Student count queries
- Department-based student retrieval
- Marks-based student filtering
- Top-student retrieval based on marks
- Semantic search using ChromaDB
- Context-based answer generation
- Error handling for temporary Gemini API failures

### API and Documentation

- FastAPI REST APIs
- Automatic Swagger/OpenAPI documentation
- ReDoc documentation
- Modular backend architecture
- Environment-based configuration
- Basic automated API tests using Pytest

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI application server |
| SQLAlchemy | ORM and database operations |
| SQLite | Local relational database |
| Pydantic | Request and response validation |
| Pydantic Settings | Environment configuration |
| Google GenAI SDK | Gemini API integration |
| LangGraph | AI workflow orchestration |
| ChromaDB | Persistent vector database and semantic search |
| Pytest | Automated testing |
| HTTPX | API testing client |

---

## System Architecture

The application follows a modular backend architecture.

```text
                        Client
                          |
                          v
                    FastAPI API
                          |
             +------------+------------+
             |                         |
             v                         v
       Student APIs               Chat API
             |                         |
             v                         v
       CRUD Services             LangGraph
             |                         |
             v                         v
        SQLite DB              Retrieval Node
                                       |
                       +---------------+---------------+
                       |               |               |
                       v               v               v
                 SQLAlchemy       ChromaDB       Structured SQL
                 Retrieval        Search          Retrieval
                       |               |               |
                       +---------------+---------------+
                                       |
                                       v
                                Generate Node
                                       |
                                       v
                                  Gemini API
                                       |
                                       v
                                  AI Response
```

---

## Project Structure

```text
student-database-ai-backend/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   ├── chat.py
│   │   └── students.py
│   │
│   ├── chatbot/
│   │   ├── graph.py
│   │   ├── state.py
│   │   └── tools.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── crud/
│   │   └── student.py
│   │
│   ├── models/
│   │   └── student.py
│   │
│   ├── schemas/
│   │   ├── chat.py
│   │   └── student.py
│   │
│   └── services/
│       ├── gemini.py
│       ├── vector_store.py
│       └── sync_vector_store.py
│
├── data/
│   └── chroma/
│
├── tests/
│   ├── test_main.py
│   └── test_students.py
│
├── .env
├── .gitignore
├── requirements.txt
├── students.db
└── README.md
```

> **Note:** The `data/chroma/` directory contains locally persisted ChromaDB data. It should be excluded from Git using `.gitignore` when the vector database is generated locally.

---

## Student Data Fields

The student schema contains the following fields:

| Field | Description | Validation |
|---|---|---|
| `id` | Unique student identifier | Automatically generated |
| `name` | Student name | 2–100 characters |
| `email` | Student email address | Valid email format and unique |
| `age` | Student age | 16–100 |
| `department` | Academic department | 2–100 characters |
| `year` | Academic year | 1–6 |
| `marks` | Student marks | 0–100 |

### Example Student Record

```json
{
  "id": 1,
  "name": "Prajwal",
  "email": "prajwal@gmail.com",
  "age": 21,
  "department": "ISE",
  "year": 3,
  "marks": 88.5
}
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Prajwalssajp/student-database-ai-backend.git
cd student-database-ai-backend
```

---

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, open PowerShell with the appropriate permissions or use another supported activation method.

---

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

Example `requirements.txt` dependencies:

```text
fastapi
uvicorn[standard]
sqlalchemy
pydantic-settings
python-dotenv
google-genai
langgraph
chromadb
pytest
httpx
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual Google Gemini API key.

**Security requirements:**

- Do not commit `.env` to GitHub.
- Do not expose your API key in source code.
- Do not share your API key publicly.
- Use separate credentials for development and production environments.

Example `.gitignore` entries:

```gitignore
.env
venv/
__pycache__/
.pytest_cache/
*.pyc
data/chroma/
```

---

### 5. Start the Application

Run the FastAPI application using Uvicorn:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger allows you to:

- View available endpoints
- Inspect request schemas
- Send API requests
- View response formats
- Test CRUD operations
- Test the chatbot endpoint

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

### OpenAPI Schema

```text
http://127.0.0.1:8000/openapi.json
```

---

## API Endpoints

### General Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the API is running |
| GET | `/health` | Returns API health status |

---

### Student CRUD Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students` | Creates a student |
| GET | `/students` | Retrieves all students |
| GET | `/students/{student_id}` | Retrieves a student by ID |
| PUT | `/students/{student_id}` | Updates a student |
| DELETE | `/students/{student_id}` | Deletes a student |

---

## Student CRUD Examples

### 1. Create a Student

**Request**

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

**Example Response**

```json
{
  "id": 1,
  "name": "Test Student",
  "email": "student@example.com",
  "age": 21,
  "department": "Computer Science",
  "year": 3,
  "marks": 85.5
}
```

The exact response depends on the implementation of the response schema and the generated student ID.

---

### 2. Retrieve All Students

**Request**

```http
GET /students
```

**Example Response**

```json
[
  {
    "id": 1,
    "name": "Test Student",
    "email": "student@example.com",
    "age": 21,
    "department": "Computer Science",
    "year": 3,
    "marks": 85.5
  }
]
```

---

### 3. Retrieve a Student by ID

**Request**

```http
GET /students/1
```

This endpoint returns the student associated with the provided ID.

If the student does not exist, the API returns a `404 Not Found` response.

---

### 4. Update a Student

**Request**

```http
PUT /students/1
Content-Type: application/json
```

```json
{
  "name": "Updated Student",
  "email": "updated@example.com",
  "age": 22,
  "department": "Information Science",
  "year": 4,
  "marks": 91.0
}
```

The updated record is stored in the SQL database and synchronized with ChromaDB.

---

### 5. Delete a Student

**Request**

```http
DELETE /students/1
```

When a student is successfully deleted:

1. The student is removed from the SQL database.
2. The corresponding ChromaDB record is deleted.
3. The API returns a successful deletion response.

---

## HTTP Status Codes

| Status Code | Meaning |
|---|---|
| `200 OK` | Request completed successfully |
| `201 Created` | Student created successfully |
| `204 No Content` | Student deleted successfully |
| `404 Not Found` | Student record does not exist |
| `409 Conflict` | Email already exists |
| `422 Unprocessable Entity` | Request validation failed |
| `500 Internal Server Error` | Unexpected server-side error |

The exact status code for an operation depends on the API implementation and exception handling.

---

# AI Chatbot

The application provides an AI chatbot that answers questions about student records.

The chatbot combines:

- FastAPI
- LangGraph
- SQLAlchemy
- ChromaDB
- Google Gemini

## Chatbot Endpoint

```http
POST /chat
```

---

## Chat Request

```json
{
  "message": "How many students are there?"
}
```

The `message` field must contain between 1 and 1,000 characters according to the chat schema.

---

## Chat Response

```json
{
  "response": "There are ... students in the database."
}
```

The exact response depends on the records currently stored in the database and the generated Gemini response.

---

## Example Chatbot Questions

The chatbot can be used for questions such as:

```text
Hi
```

```text
How many students are there?
```

```text
Which students are in the CSE department?
```

```text
Show students with marks above 80.
```

```text
Who has the highest marks?
```

```text
Show the top students.
```

```text
Find students related to computer science.
```

The supported response depends on the retrieval logic and the information available in the database.

---

# LangGraph Workflow

The chatbot uses a LangGraph workflow consisting of retrieval and answer-generation nodes.

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

## 1. Retrieve Node

The retrieve node analyzes the user's question and selects a retrieval strategy.

The current retrieval functionality includes:

- Student count queries
- Department-related retrieval
- Structured marks-based retrieval
- Top-student retrieval based on marks
- Semantic search through ChromaDB
- SQLAlchemy fallback retrieval
- Context preparation for the Gemini model

### Structured Retrieval

SQLAlchemy is used for queries that require reliable database operations, such as:

- Counting students
- Filtering students by minimum marks
- Sorting students by marks
- Retrieving top students

For example:

```text
Show students with marks above 80.
```

The system can use a structured SQL query to retrieve students whose marks meet the requested threshold.

For ranking questions such as:

```text
Who has the highest marks?
```

the system uses marks-based ordering to retrieve top students.

### Semantic Retrieval

ChromaDB is used for semantic search over student records.

This allows the system to search student information using natural-language queries rather than relying only on exact keyword matches.

---

## 2. Generate Node

The generate node:

1. Receives the user's question.
2. Receives the retrieved database context.
3. Builds a prompt for Google Gemini.
4. Sends the prompt to the Gemini API.
5. Returns the generated answer.

The prompt instructs Gemini to use the supplied database context and clearly indicate when the requested information is unavailable.

The application also includes error handling for temporary Gemini API failures.

---

## Greeting Handling

Common greetings are handled directly by the chatbot.

Examples include:

- `hi`
- `hello`
- `hey`
- `hii`
- `good morning`
- `good afternoon`
- `good evening`

Greeting handling avoids unnecessary database retrieval for simple conversational messages.

---

# ChromaDB Integration

ChromaDB is integrated into the application as a persistent vector database for semantic student retrieval.

## Purpose

ChromaDB supports:

- Student document storage
- Persistent vector collection
- Semantic search
- Student record synchronization
- Retrieval of relevant student information

---

## Student Synchronization

When a student is created or updated:

1. The student record is saved in the SQL database.
2. A text document is generated from the student fields.
3. The document is stored or updated in ChromaDB.
4. The student ID is used as the ChromaDB record identifier.

When a student is deleted:

1. The student is removed from the SQL database.
2. The corresponding ChromaDB record is deleted.

This helps maintain consistency between the relational database and the vector database.

---

## Retrieval Responsibilities

| Component | Responsibility |
|---|---|
| SQLAlchemy | Structured database queries |
| SQLite | Persistent relational student records |
| ChromaDB | Semantic student document search |
| LangGraph | Workflow orchestration |
| Gemini | Natural-language answer generation |

Structured numerical operations such as marks filtering and ranking should use SQL-based retrieval rather than relying only on semantic similarity.

---

# Database

The application uses **SQLAlchemy** with a local **SQLite** database.

The current local database file is:

```text
students.db
```

Database tables are created through the SQLAlchemy metadata configuration:

```python
Base.metadata.create_all(bind=engine)
```

## Database Responsibilities

The relational database stores:

- Student IDs
- Student names
- Email addresses
- Ages
- Departments
- Academic years
- Marks

SQLAlchemy is used for:

- Creating records
- Reading records
- Updating records
- Deleting records
- Filtering records
- Counting records
- Sorting records by marks

---

## Database Configuration

The current project uses a local SQLite database for development.

For production use, the following improvements are recommended:

- Environment-based database configuration
- Database migrations
- PostgreSQL or another production database
- Connection pooling
- Backup and recovery procedures

---

# Testing

The project includes basic automated API tests using Pytest.

## Run Tests

Activate the virtual environment and execute:

```powershell
python -m pytest -v
```

## Current Test Coverage

The test suite includes tests for:

- Root endpoint
- Health endpoint
- Student creation
- Retrieving student records
- Student-not-found handling

Additional tests are recommended for complete coverage of all application functionality.

## Recommended Additional Tests

Future tests can cover:

- Updating a student
- Deleting a student
- Duplicate email validation
- Invalid student data
- Marks-based retrieval
- Top-student retrieval
- ChromaDB synchronization
- Chatbot greeting handling
- Chatbot database questions
- Gemini API failure handling
- Empty or invalid chat messages

---

# Environment Configuration

The Gemini API key is loaded through environment-based configuration.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Environment variables should be kept outside the source code.

## Security Guidelines

- Never commit `.env` to GitHub.
- Never hardcode API keys.
- Do not publish private student information.
- Use authentication before exposing the application publicly.
- Apply authorization to sensitive operations.
- Validate all incoming user data.
- Avoid returning unnecessary personal information in chatbot responses.
- Use separate development and production credentials.

---

# Error Handling

The application handles common errors such as:

- Student record not found
- Duplicate email addresses
- Invalid request data
- Temporary Gemini API failures
- Empty Gemini responses
- Invalid or unavailable student information

When the Gemini API is temporarily unavailable, the application returns a user-friendly error message instead of allowing the exception to crash the chatbot request.

---

# Running the Application

## Start the Backend

```powershell
uvicorn app.main:app --reload
```

## Open Swagger

Open the following URL in a browser:

```text
http://127.0.0.1:8000/docs
```

## Test the API

Use Swagger UI or an API client to test:

1. Health endpoints
2. Student CRUD endpoints
3. Chatbot endpoint
4. Structured student queries

---

# Example Workflow

A typical student creation and chatbot workflow looks like this:

```text
1. Client sends a POST request to /students
                    |
                    v
2. FastAPI validates the request using Pydantic
                    |
                    v
3. SQLAlchemy saves the student in SQLite
                    |
                    v
4. Student information is synchronized with ChromaDB
                    |
                    v
5. Client sends a question to /chat
                    |
                    v
6. LangGraph selects a retrieval strategy
                    |
                    v
7. Student context is retrieved from SQLAlchemy or ChromaDB
                    |
                    v
8. Gemini generates a natural-language answer
                    |
                    v
9. Chatbot returns the response to the client
```

---

# Limitations

The current project is designed as a functional backend prototype.

Current limitations may include:

- Basic automated test coverage
- No authentication or authorization system
- Local SQLite database configuration
- Limited chatbot intent detection
- Limited natural-language query parsing
- No production deployment configuration
- No database migration workflow
- No comprehensive response validation for every Gemini response
- Numerical queries require supported retrieval patterns
- Semantic search does not replace structured SQL filtering for numerical operations

---

# Future Improvements

The following improvements can be implemented in future versions:

## Backend Improvements

- Add authentication and authorization
- Add role-based access control
- Add pagination
- Add advanced filtering and sorting
- Add structured logging
- Add database migrations
- Add centralized exception handling
- Add improved API response schemas

## AI Improvements

- Improve chatbot intent classification
- Support more natural-language query formats
- Add tool-based query selection
- Improve retrieval accuracy
- Add response validation
- Add conversation history
- Add source references in chatbot responses
- Add evaluation datasets for chatbot accuracy

## Vector Database Improvements

- Improve embedding and retrieval strategies
- Add metadata filtering
- Evaluate semantic search quality
- Add document-level access controls
- Support academic policies and other student-related documents
- Implement a complete retrieval-augmented generation pipeline

## Deployment Improvements

- Add Docker support
- Add Docker Compose
- Deploy the backend to a cloud platform
- Use PostgreSQL for production
- Add CI/CD with GitHub Actions
- Configure monitoring and logging
- Use production-grade secret management

---

# Project Status

The project currently includes:

- Modular FastAPI backend
- Student CRUD APIs
- SQLAlchemy and SQLite integration
- Pydantic request and response validation
- Google Gemini integration
- LangGraph retrieval and generation workflow
- ChromaDB semantic retrieval
- Student synchronization between SQLAlchemy and ChromaDB
- Structured marks-based retrieval
- Top-student retrieval
- Greeting handling
- Basic automated API tests
- Swagger/OpenAPI documentation

The project is currently implemented as a **functional AI backend prototype**.

Additional improvements, including authentication, expanded test coverage, production database configuration, deployment, and advanced chatbot capabilities, can be added in future versions.

---

# License

This project is intended for educational and development purposes.

Add an appropriate open-source license, such as the MIT License, if you plan to publish the project for public reuse.