<div align="center">

# 🎓 Student Management API

### A RESTful API for managing student records with Python and FastAPI

A beginner-friendly backend project built as part of my practical journey into **Python Backend Development and Applied AI Engineering**. The API supports creating, retrieving, updating, and deleting student records, with Pydantic field constraints, custom field validation, response models, and HTTP error handling.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend%20Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-E92063?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-In%20Development-orange?style=for-the-badge)

[Overview](#-project-overview) • [Features](#-implemented-features) • [Technologies](#-technologies-used) • [API](#-api-endpoints) • [Response Models](#-pydantic-models-and-response-models) • [Setup](#-getting-started) • [Roadmap](#-upcoming-improvements)

</div>

---

## 📌 Project Overview

The **Student Management API** is a RESTful backend project built using **Python** and **FastAPI**. It provides endpoints to manage student records through Create, Read, Update, and Delete (CRUD) operations.

The application currently stores student information in an **in-memory Python dictionary**. It uses **Pydantic models** to validate incoming student data and FastAPI `response_model` definitions to control the structure of outgoing API responses.

This project is part of my hands-on learning journey in backend development, REST APIs, request validation, response serialization, and API testing.

## ✨ Implemented Features

The following features are implemented in the current project version:

- **Create Student:** Add a new student record using a POST request.
- **Get Student by ID:** Retrieve an individual student record using its ID.
- **Get All Students:** Retrieve the complete list of available student records.
- **Update Student:** Update the name of an existing student.
- **Delete Student:** Remove an existing student record.
- **Automatic ID Generation:** Generate a new student ID based on the current records.
- **Request Validation:** Validate student names with Pydantic `Field` constraints (minimum 2 and maximum 50 characters).
- **Advanced Field Validation:** Use Pydantic `@field_validator` with `mode="after"` to reject names containing numeric digits.
- **Response Models:** Define the expected output structure for create, read, update, list, and delete operations.
- **Response Filtering:** Use FastAPI response models to return only the fields defined by the relevant model.
- **Error Handling:** Return HTTP `404 Not Found` when a requested student ID does not exist.
- **CORS Middleware:** Allow requests from the configured local frontend origin.
- **Interactive API Documentation:** Explore and test API endpoints using Swagger UI.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend API framework |
| Pydantic | Request models, field constraints, custom validation, and response data models |
| Uvicorn | ASGI development server |
| CORSMiddleware | Cross-origin resource sharing |
| Swagger UI | Interactive API documentation and testing |
| Git & GitHub | Version control and source code hosting |

## 📂 Project Structure

```text
student-management-api/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

| Method | Endpoint | Description | Expected Status |
|---|---|---|---|
| `POST` | `/students` | Create a student | `201 Created` / `422` |
| `GET` | `/students` | Retrieve all students | `200 OK` |
| `GET` | `/students/{student_id}` | Retrieve a student by ID | `200 OK` / `404 Not Found` |
| `PUT` | `/students/{student_id}` | Update a student's name | `200 OK` / `404 Not Found` / `422` |
| `DELETE` | `/students/{student_id}` | Delete a student | `200 OK` / `404 Not Found` |

## 🧩 Pydantic Models and Response Models

The project defines four Pydantic models to validate request data and shape API responses.

| Model | Purpose | Used by |
|---|---|---|
| `StudentCreate` | Validates the incoming student name | `POST /students` and `PUT /students/{student_id}` |
| `StudentResponse` | Defines `student_id`, `name`, and `message` in a single-student response | POST, GET by ID, and PUT |
| `StudentListItem` | Defines `student_id` and `name` for each item in the student list | `GET /students` |
| `StudentDeleteResponse` | Defines `student_id` and `message` in the delete response | `DELETE /students/{student_id}` |

### Request validation with `Field`

`StudentCreate` applies length constraints to the incoming `name` field:

```python
class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
```

A student name must contain at least **2 characters** and no more than **50 characters**. Requests that fail validation are rejected with HTTP `422 Unprocessable Entity`.

### Advanced Pydantic validation with `@field_validator`

The project also uses a custom Pydantic field validator to check the student name after the normal field validation:

```python
@field_validator("name", mode="after")
@classmethod
def validate_name(cls, value):
    if any(char.isdigit() for char in value):
        raise ValueError("Student name must not contain numbers")
    return value
```

This rejects names containing digits. For example, `"Huzaifa123"` produces a validation error, while a name such as `"Huzaifa"` passes this custom check (provided it also meets the length constraints).

**Important implementation note:** The current `StudentCreate` code defines both the `mode="before"` and `mode="after"` validators with the same Python method name, `validate_name`. The second definition replaces the first name in the class namespace, so the whitespace-trimming (`value.strip()`) validator is not registered as written. The digit-checking `mode="after"` validator remains. This means whitespace is not currently stripped before validation.

To activate both validators, give them distinct method names, for example:

```python
@field_validator("name", mode="before")
@classmethod
def strip_name(cls, value):
    if isinstance(value, str):
        value = value.strip()
    return value

@field_validator("name", mode="after")
@classmethod
def reject_digits(cls, value):
    if any(char.isdigit() for char in value):
        raise ValueError("Student name must not contain numbers")
    return value
```

The code above is the recommended correction for enabling both trimming and digit validation; the distinct method names need to be applied in `main.py` before claiming that whitespace trimming is active.

### Controlling output with `response_model`

Each endpoint declares a response model. FastAPI uses it to validate and serialize the returned data, keeping the public response structure consistent.

For example, `GET /students/{student_id}` returns the fields defined by `StudentResponse`:

```python
class StudentResponse(BaseModel):
    student_id: int
    name: str
    message: str
```

The GET-by-ID function also includes an `internal_note` value in its Python return dictionary as a demonstration. Because the route declares `response_model=StudentResponse`, that extra field is excluded from the API response. The client receives only `student_id`, `name`, and `message`.

## 📝 API Usage Examples

The following examples show the request and response formats supported by the current code.

### 1. Create Student

**POST** `/students`  
**Status:** `201 Created`

Request Body:

```json
{
  "name": "Sara"
}
```

Example Successful Response:

```json
{
  "student_id": 4,
  "name": "Sara",
  "message": "Student Created"
}
```

The API generates the new ID using the highest current student ID plus one.

### 2. Get All Students

**GET** `/students`  
**Status:** `200 OK`

Example Response:

```json
[
  {
    "student_id": 1,
    "name": "Ali"
  },
  {
    "student_id": 2,
    "name": "Ahmad"
  },
  {
    "student_id": 3,
    "name": "Huzaifa"
  }
]
```

The endpoint uses `list[StudentListItem]` as its response model.

### 3. Get Student by ID

**GET** `/students/1`  
**Status:** `200 OK`

Example Response:

```json
{
  "student_id": 1,
  "name": "Ali",
  "message": "Student Found"
}
```

The route uses `StudentResponse`. Any additional value in the internal return dictionary, such as `internal_note`, is not included in the client response.

### 4. Update Student

**PUT** `/students/1`  
**Status:** `200 OK`

Request Body:

```json
{
  "name": "Ali Khan"
}
```

Example Successful Response:

```json
{
  "student_id": 1,
  "name": "Ali Khan",
  "message": "Student Updated"
}
```

The same `StudentCreate` model validates the new name. If the student ID does not exist, the endpoint returns `404 Not Found`.

### 5. Delete Student

**DELETE** `/students/1`  
**Status:** `200 OK`

Example Response:

```json
{
  "student_id": 1,
  "message": "Student Deleted Successfully"
}
```

The endpoint uses `StudentDeleteResponse`. If the student ID does not exist, it returns `404 Not Found`.

## ⚠️ Data Validation and Error Handling

The API uses Pydantic and FastAPI for request validation and HTTP error responses.

- Minimum student name length: **2 characters**.
- Maximum student name length: **50 characters**.
- Names containing numeric digits are rejected by the active `mode="after"` field validator.
- Invalid request data returns HTTP **422 Unprocessable Entity**.
- A student ID that does not exist returns HTTP **404 Not Found**.
- Whitespace trimming is intended in the `mode="before"` validator, but is not currently active because both validator methods share the same name. See [Advanced Pydantic validation](#advanced-pydantic-validation-with-field_validator) for the correction.

Example `422 Unprocessable Entity` response for a name containing digits (FastAPI/Pydantic validation response):

```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "name"],
      "msg": "Value error, Student name must not contain numbers",
      "input": "Huzaifa123"
    }
  ]
}
```

Example `404 Not Found` response:

```json
{
  "detail": "Student not found"
}
```

The exact capitalization of the message depends on the endpoint's implementation.

## 🌐 CORS Configuration

The API is configured to accept cross-origin requests from the following local frontend origin:

```text
http://localhost:3000
```

**Allowed HTTP methods:**

- `GET`
- `POST`
- `PUT`
- `DELETE`

**Allowed request headers:**

- `Content-Type`
- `Authorization`

CORS credentials are currently disabled (`allow_credentials=False`).

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/huzaifa2612/student-management-api.git
```

### 2. Open the Project Directory

```bash
cd student-management-api
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows CMD:**

```cmd
.venv\Scripts\activate.bat
```

### 5. Install Dependencies

If the repository includes `requirements.txt`, install the listed dependencies:

```bash
python -m pip install -r requirements.txt
```

Alternatively, install the packages used to run this application:

```bash
python -m pip install fastapi uvicorn
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Open Swagger UI to explore all five endpoints, provide request data, and test API responses directly from your browser.

## ⚠️ Current Project Limitations

The current version is a functional CRUD learning project with the following limitations:

- Student records are stored in an **in-memory Python dictionary**.
- Data is not persistent and resets when the server restarts.
- PostgreSQL database integration has not been implemented yet.
- Automated testing with Pytest has not been implemented yet.
- Authentication and authorization have not been implemented yet.
- The application currently uses a single Python file.

## 🗺️ Upcoming Improvements

The following improvements are planned for future development:

- PostgreSQL database integration.
- SQLAlchemy ORM.
- A more organized and scalable backend project architecture.
- Automated testing using Pytest.
- Environment variable configuration.
- JWT-based authentication and authorization.
- Pagination and filtering.
- Docker containerization.
- Cloud deployment.

## 👨‍💻 Author

**Muhammad Huzaifa**

Computer Science Student | Learning Python Backend Development and Applied AI Engineering.

- **GitHub:** [@huzaifa2612](https://github.com/huzaifa2612)
- **Repository:** [student-management-api](https://github.com/huzaifa2612/student-management-api)

---

<div align="center">

*Built with Python and FastAPI as part of a hands-on software engineering learning journey.*

</div>
