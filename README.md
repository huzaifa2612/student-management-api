# Student Management API

**A FastAPI REST API for managing student records with validated requests, consistent responses, and configurable CORS.**

This is a Python backend project built to practice API routing, CRUD operations, Pydantic validation, error handling, and environment-based configuration. The current implementation uses an in-memory dictionary rather than a database.

![Python](https://img.shields.io/badge/Python-3.10%2B-0f172a?style=for-the-badge&logo=python&logoColor=22d3ee)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-0ea5e9?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-0f172a?style=for-the-badge&logo=pydantic&logoColor=22d3ee)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-0ea5e9?style=for-the-badge&logoColor=white)
![Status](https://img.shields.io/badge/Status-Functional%20Prototype-0f172a?style=for-the-badge&logoColor=22d3ee)

---

## 1. Project Overview

Student Management API exposes five HTTP endpoints for creating, listing, retrieving, updating, and deleting students. Each student consists of an integer ID and a name.

The API is organized into an application entry point, a student router, Pydantic schemas, and a settings module. It starts with three sample students in memory: `1: Ali`, `2: Ahmad`, and `3: Huzaifa`. Changes made through the API last only while the Python process is running.

The implementation focuses on a clear learning-sized backend rather than claiming production readiness or features that are not present in the source code.

## 2. Implemented Features

- **Create a student:** `POST /students` accepts a validated name and assigns an integer ID.
- **List students:** `GET /students` returns an array of student IDs and names.
- **Find a student:** `GET /students/{student_id}` returns one record or an HTTP 404 error.
- **Update a student:** `PUT /students/{student_id}` replaces an existing student's name after validation.
- **Delete a student:** `DELETE /students/{student_id}` removes an existing student and returns a confirmation.
- **Request validation:** Names are trimmed, must contain 2–50 characters after trimming, and cannot contain numeric digits.
- **Response schemas:** The API defines separate response models for student details, list items, and deletion results.
- **Error handling:** Missing IDs produce HTTP 404; invalid request data produces HTTP 422.
- **CORS configuration:** A frontend origin and allowed methods/headers are configured through the application settings.
- **Interactive documentation:** FastAPI provides Swagger UI and ReDoc automatically.

## 3. Technology Stack

| Technology | Verified use in this project |
|---|---|
| Python | Application logic and in-memory data structures |
| FastAPI | API application, router registration, response models, and HTTP errors |
| Pydantic v2 | Input fields, field validators, and response schemas |
| `pydantic-settings` | Settings from environment variables and `.env` |
| `python-dotenv` | Environment-file support (included in `requirements.txt`) |
| Uvicorn | ASGI server used to run the application |
| Git / GitHub | Source control and repository hosting |

The checked-in `requirements.txt` does not pin exact dependency versions.

## 4. Project Architecture and Folder Structure

```text
student-management-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── students.py
│   └── schemas/
│       ├── __init__.py
│       └── student.py
├── .env.example
├── .gitattributes
├── .gitignore
├── README.md
└── requirements.txt
```

The supplied ZIP also contains local `.git/`, `.venv/`, and `__pycache__/` directories; these are development/generated artifacts rather than application source files. `.venv/` and `__pycache__/` are ignored by the provided `.gitignore`.

### Request flow

```text
HTTP request
    |
    v
FastAPI app (app/main.py)
    |
    v
Student router (app/routers/students.py)
    |
    +--> Pydantic input validation (app/schemas/student.py)
    |
    +--> In-memory students dictionary (in the router)
    |
    v
Pydantic response model -> JSON response
```

The **active** student store is the `students` dictionary inside `app/routers/students.py`. A separate `students` dictionary also exists in `app/main.py`, but the routes do not use that second dictionary.

## 5. File-by-File Explanation

| File | Responsibility |
|---|---|
| `app/main.py` | Creates the FastAPI application, sets its title/version, configures CORS middleware, and includes the students router. |
| `app/config.py` | Defines `Settings` using `BaseSettings`, with defaults for application name, version, and frontend origin; loads `.env`. |
| `app/routers/students.py` | Holds the active in-memory student dictionary and implements all five CRUD endpoints. |
| `app/schemas/student.py` | Defines the input validator and the `StudentCreate`, `StudentResponse`, `StudentListItem`, and `StudentDeleteResponse` models. |
| `app/__init__.py` | Marks `app` as a Python package. It has no additional logic. |
| `app/routers/__init__.py` | Marks `routers` as a Python package. It has no additional logic. |
| `app/schemas/__init__.py` | Marks `schemas` as a Python package. It has no additional logic. |
| `.env.example` | Provides sample values for `APP_NAME`, `APP_VERSION`, and `FRONTEND_ORIGIN`; contains no API credentials. |
| `.gitignore` | Ignores Python caches, virtual environments, `.env`, and pytest cache files. |
| `.gitattributes` | Enables Git text-file line-ending normalization (`* text=auto`). |
| `requirements.txt` | Lists `fastapi`, `uvicorn[standard]`, `pydantic-settings`, and `python-dotenv`. |
| `README.md` | Explains the project, endpoints, configuration, and local setup. |

## 6. API Endpoints Reference

Base URL when running locally: `http://127.0.0.1:8000`

| HTTP method | Route | Action | Success | Other expected status codes |
|---|---|---|---|---|
| `POST` | `/students` | Create a student | `201 Created` | `422` for invalid request body |
| `GET` | `/students` | List all students | `200 OK` | — |
| `GET` | `/students/{student_id}` | Retrieve one student | `200 OK` | `404` if missing; `422` if ID is not an integer |
| `PUT` | `/students/{student_id}` | Update a student name | `200 OK` | `404` if missing; `422` for invalid ID/body |
| `DELETE` | `/students/{student_id}` | Delete a student | `200 OK` | `404` if missing; `422` if ID is not an integer |

`{student_id}` is a path parameter declared as an `int`. No API-key authentication or login is required by the current implementation.

### Response models

| Model | Fields | Used by |
|---|---|---|
| `StudentCreate` | `name: str` | `POST` and `PUT` request bodies |
| `StudentResponse` | `student_id: int`, `name: str`, `message: str` | Create, get by ID, update |
| `StudentListItem` | `student_id: int`, `name: str` | Each item in `GET /students` |
| `StudentDeleteResponse` | `student_id: int`, `message: str` | Delete |

## 7. Request and Response Examples

The examples below assume a **freshly started** server containing the three initial sample records. Creating `Sara` therefore produces ID `4`.

### Create a student — `POST /students`

Request body:

```json
{
  "name": "Sara"
}
```

Response — **201 Created**:

```json
{
  "student_id": 4,
  "name": "Sara",
  "message": "Student Created"
}
```

### List students — `GET /students`

Response — **200 OK** (after the creation above):

```json
[
  {"student_id": 1, "name": "Ali"},
  {"student_id": 2, "name": "Ahmad"},
  {"student_id": 3, "name": "Huzaifa"},
  {"student_id": 4, "name": "Sara"}
]
```

### Retrieve one student — `GET /students/4`

Response — **200 OK**:

```json
{
  "student_id": 4,
  "name": "Sara",
  "message": "Student Found"
}
```

### Update a student — `PUT /students/4`

Request body:

```json
{
  "name": "Sara Khan"
}
```

Response — **200 OK**:

```json
{
  "student_id": 4,
  "name": "Sara Khan",
  "message": "Student Updated"
}
```

### Delete a student — `DELETE /students/4`

Response — **200 OK**:

```json
{
  "student_id": 4,
  "message": "Student Deleted Successfully"
}
```

### Student not found — `GET /students/999`

Response — **404 Not Found**:

```json
{
  "detail": "Student not Found"
}
```

> The update and delete endpoints use the error message `Student not found` (lowercase “found”); the get-by-ID endpoint uses `Student not Found`, as written in the source.

### Try a request from Windows PowerShell

With Uvicorn running in another terminal:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/students" -Method Get
```

To create a student:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/students" -Method Post -ContentType "application/json" -Body '{"name":"Sara"}'
```

## 8. Pydantic Validation and Error Handling

The `StudentCreate` model validates the `name` field used by **both POST and PUT**:

1. A `mode="before"` validator applies `.strip()` when the input is a string.
2. Pydantic checks the field type and the declared length: **2–50 characters**.
3. A `mode="after"` validator rejects any name containing a digit (`char.isdigit()`).

Examples:

| Input `name` | Outcome |
|---|---|
| `"  Sara  "` | Accepted and stored as `"Sara"` |
| `"A"` | Rejected: fewer than 2 characters |
| `"Ali2"` | Rejected: name contains a digit |
| A string longer than 50 characters | Rejected |
| Missing `name` | Rejected: required field |

The validator **does not** enforce an alphabetic-only name; punctuation and other non-numeric characters are not explicitly rejected by the current code.

### Validation error — HTTP 422

For a request body of `{"name":" x "}`, the name becomes `"x"` after trimming and fails the minimum-length check. A representative response from the inspected implementation is:

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "name"],
      "msg": "String should have at least 2 characters",
      "input": "x",
      "ctx": {"min_length": 2}
    }
  ]
}
```

FastAPI/Pydantic can include different or additional error-detail fields depending on the installed versions.

Missing student IDs are handled explicitly with `HTTPException(status_code=404, ...)`, whereas request-body and integer path-parameter validation are handled automatically by FastAPI/Pydantic.

## 9. CORS Configuration

`app/main.py` registers `CORSMiddleware` with the following settings:

| Option | Current value |
|---|---|
| Allowed origins | A one-item list containing `settings.frontend_origin` |
| Default allowed origin | `http://localhost:3000` |
| Allowed methods | `GET`, `POST`, `PUT`, `DELETE` |
| Allowed headers | `Content-Type`, `Authorization` |
| Allow credentials | `False` |

Update `FRONTEND_ORIGIN` in `.env` if a frontend runs at a different origin. The value must match the frontend's **scheme, hostname, and port**. For example, `http://127.0.0.1:3000` and `http://localhost:3000` are different origins.

CORS controls browser cross-origin access; it does **not** provide authentication or authorization.

## 10. Environment Variables and Configuration

Configuration is defined by `Settings` in `app/config.py`. It reads environment variables and an optional root-level `.env` file. The repository includes `.env.example` as a template.

| Variable | Example/default | What it controls |
|---|---|---|
| `APP_NAME` | `Student Management API` | Title shown in generated API documentation |
| `APP_VERSION` | `1.0.0` | Version displayed by FastAPI/OpenAPI |
| `FRONTEND_ORIGIN` | `http://localhost:3000` | Allowed browser frontend origin for CORS |

Create your local configuration in Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

The resulting `.env` file can contain:

```dotenv
APP_NAME=Student Management API
APP_VERSION=1.0.0
FRONTEND_ORIGIN=http://localhost:3000
```

All three settings have defaults in `app/config.py`. **No API tokens, passwords, or database credentials are required by the current project.** The `.env` file is ignored by `.gitignore` and should remain local. Restart the API after changing configuration values.

## 11. Installation and Setup (Windows PowerShell)

**Prerequisites:** Python 3.10 or newer, Git, and Windows PowerShell.

### Step 1 — Clone the repository

```powershell
git clone https://github.com/huzaifa2612/student-management-api.git
cd student-management-api
```

### Step 2 — Create a virtual environment

```powershell
py -m venv .venv
```

If the Python launcher (`py`) is unavailable, use `python -m venv .venv`.

### Step 3 — Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can allow local script execution **for the current terminal session only** and then retry activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### Step 4 — Install project dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 5 — Create your local `.env`

```powershell
Copy-Item .env.example .env
```

Open `.env` and adjust only the values appropriate for your local application. You do not need to create a database or obtain credentials.

## 12. Running the Application

From the repository root, with the virtual environment active:

```powershell
python -m uvicorn app.main:app --reload
```

The server normally listens at:

- API base URL: `http://127.0.0.1:8000`
- Students endpoint: `http://127.0.0.1:8000/students`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Use **Ctrl + C** in the terminal to stop the server.

**Important:** The entry point is `app.main:app`. A command such as `uvicorn main:app --reload` is not correct for this repository structure. The root path `/` is not a defined application endpoint.

## 13. Swagger UI and ReDoc Documentation

FastAPI exposes interactive API documentation automatically:

| Page | Local URL | Purpose |
|---|---|---|
| Swagger UI | [`/docs`](http://127.0.0.1:8000/docs) | Explore endpoints, provide JSON bodies, and use **Try it out** |
| ReDoc | [`/redoc`](http://127.0.0.1:8000/redoc) | Read structured reference documentation |
| OpenAPI schema | [`/openapi.json`](http://127.0.0.1:8000/openapi.json) | View the generated OpenAPI JSON |

These links work after the local server starts. The CRUD endpoints appear under the **Students Management** tag defined in `app/routers/students.py`.

## 14. Current Project Limitations

This is a functional **in-memory CRUD prototype**, not a production student-information system.

- **No persistent storage:** All changes disappear when the server process restarts; the three sample records are recreated.
- **No database or ORM:** PostgreSQL, SQLite, SQLAlchemy, and database migrations are not implemented.
- **No authentication or authorization:** JWT, user accounts, and role-based access control are not implemented.
- **No automated project tests:** The ZIP contains no dedicated Pytest test suite.
- **No Docker or deployment setup:** No Dockerfile, Compose configuration, or hosting/deployment configuration is present.
- **No filtering, pagination, or sorting endpoints:** `GET /students` returns the complete in-memory collection.
- **Simple ID allocation:** The next ID is `max(existing_ids) + 1`, so an ID may be reused after deleting the highest-numbered record.
- **Duplicate sample dictionary:** `app/main.py` has a `students` dictionary that is not used by the router; the active storage is in `app/routers/students.py`.
- **Unpinned dependency versions:** `requirements.txt` does not lock package versions.

## 15. Future Improvements (Not Implemented)

Potential next steps for a more complete backend project include:

- Add persistent storage using SQLite or PostgreSQL, with an appropriate data-access layer or ORM.
- Introduce authentication, authorization, and protected write operations.
- Add automated tests covering CRUD routes, validation, errors, and CORS behavior.
- Improve ID generation and remove the unused duplicate dictionary.
- Add filtering, sorting, pagination, and richer student fields if project requirements expand.
- Pin or lock dependencies and add CI checks.
- Add containerization and a documented deployment workflow.

These items are **ideas for later development**, not features included in the uploaded source.

## 16. Author and Repository Information

**Muhammad Huzaifa** — Computer Science Student

- GitHub: [huzaifa2612](https://github.com/huzaifa2612)
- Repository: [student-management-api](https://github.com/huzaifa2612/student-management-api)

Built as a hands-on Python backend project to practice REST API design, validation, modular application structure, and local development with FastAPI.
