<div align="center">

# 🎓 Student Management API

### A RESTful API for managing student records with Python and FastAPI

A beginner-friendly backend project built as part of my practical journey into **Python Backend Development and Applied AI Engineering**. The API is being developed to create, retrieve, update, and delete student records, with request validation and HTTP error handling.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend%20Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-E92063?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-In%20Development-orange?style=for-the-badge)

[Overview](#-project-overview) • [Features](#-implemented-features) • [Technologies](#-technologies-used) • [API](#-api-endpoints) • [Setup](#-getting-started) • [Roadmap](#-upcoming-improvements)

</div>

---

## 📌 Project Overview

The **Student Management API** is a RESTful backend project built using **Python** and **FastAPI**. It provides API endpoints for managing student records through Create, Read, Update, and Delete (CRUD) operations.

The current project uses an **in-memory Python dictionary** for storing student information and **Pydantic models** for validating incoming request data.

This project is part of my hands-on learning journey in backend development, REST APIs, request validation, and API testing.

## ✨ Implemented Features

The following features are included in the current project version:

- **Create Student:** Add new student records through POST requests.
- **Get Student by ID:** Retrieve an individual student record using its ID.
- **Get All Students:** Retrieve all available student records.
- **Update Student:** Modify the information of an existing student.
- **Delete Student:** Remove a student record.
- **Automatic ID Generation:** Generate student IDs automatically for new records.
- **Data Validation:** Validate student names using Pydantic.
- **Error Handling:** Return HTTP 404 responses when a requested student record does not exist.
- **CORS Middleware:** Configure cross-origin requests for a local frontend.
- **Interactive API Documentation:** Explore and test API endpoints using Swagger UI.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend API framework |
| Pydantic | Request data validation |
| Uvicorn | ASGI development server |
| CORSMiddleware | Cross-origin resource sharing |
| Swagger UI | API documentation and testing |
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

The project is designed around the following REST API endpoints:

| Method | Endpoint | Description | Expected Status |
|---|---|---|---|
| `POST` | `/students` | Create a student | `201 Created` |
| `GET` | `/students` | Retrieve all students | `200 OK` |
| `GET` | `/students/{student_id}` | Retrieve a student by ID | `200 OK` / `404 Not Found` |
| `PUT` | `/students/{student_id}` | Update a student | `200 OK` / `404 Not Found` |
| `DELETE` | `/students/{student_id}` | Delete a student | `200 OK` / `404 Not Found` |

## 📝 API Usage Examples

The following examples illustrate the intended request and response formats for the API.

### 1. Create Student

**POST** `/students`

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

### 2. Get All Students

**GET** `/students`

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

### 3. Get Student by ID

**GET** `/students/1`

Example Response:

```json
{
  "student_id": 1,
  "name": "Ali",
  "message": "Student Found"
}
```

### 4. Update Student

**PUT** `/students/1`

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

### 5. Delete Student

**DELETE** `/students/1`

Example Response:

```json
{
  "student_id": 1,
  "message": "Student Deleted Successfully"
}
```

## ⚠️ Data Validation and Error Handling

Student names are validated using **Pydantic**.

The current validation rules are:

- Minimum student name length: **2 characters**
- Maximum student name length: **50 characters**
- Invalid request data returns HTTP **422 Unprocessable Entity**.
- A student ID that does not exist returns HTTP **404 Not Found**.

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

```bash
python -m pip install -r requirements.txt
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

Open Swagger UI to explore the available endpoints, provide request data, and test API responses directly from your browser.

## ⚠️ Current Project Limitations

This project is currently an early-stage backend application with the following limitations:

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
- Response models and improved request validation.
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
