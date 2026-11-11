<div align="center">

# 🎓 Student Management API

### A simple REST API for managing student records with Python and FastAPI

A hands-on backend project that demonstrates CRUD operations, Pydantic request validation, structured API responses, and basic error handling.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend%20Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

[Overview](#-overview) • [Features](#-features) • [Code](#-how-the-code-works) • [Endpoints](#-api-endpoints) • [Setup](#-run-locally)

</div>

---

## 📌 Overview

**Student Management API** is a beginner-friendly REST API built with **Python**, **FastAPI**, and **Pydantic**. It allows clients to create, view, update, and delete student records through HTTP requests.

The project currently stores student records in a Python dictionary. It is designed to demonstrate the core building blocks of a backend API: routes, request validation, response models, and error handling.

## ✨ Features

- Create a student record.
- Retrieve all students or a student by ID.
- Update a student's name.
- Delete a student record.
- Generate student IDs automatically.
- Validate student names with Pydantic.
- Return consistent response formats using response models.
- Handle requests for unknown student IDs with HTTP 404.
- Configure CORS for a local frontend.

## 🧠 How the Code Works

| Component | Responsibility |
|---|---|
| **FastAPI application** | Creates the API application and registers its endpoints. |
| **Student storage** | Keeps student IDs and names in an in-memory Python dictionary. |
| **`StudentCreate`** | Validates incoming student names. The name must be 2–50 characters and must not contain digits. |
| **`StudentResponse`** | Defines the response fields for create, get-by-ID, and update operations. |
| **`StudentListItem`** | Defines the fields returned for each student in the list endpoint. |
| **`StudentDeleteResponse`** | Defines the response returned after a student is deleted. |
| **CRUD endpoints** | Handle creating, reading, updating, and deleting student records. |
| **HTTPException** | Returns an HTTP 404 error when the requested student ID does not exist. |
| **CORS middleware** | Allows the configured local frontend origin to send requests to the API. |

### Request validation

Pydantic validates the incoming `name` field before the endpoint processes the request:

- Minimum length: **2 characters**
- Maximum length: **50 characters**
- Names containing digits are rejected.
- Invalid request data is rejected with HTTP **422 Unprocessable Entity**.

### Response models

Each endpoint uses a response model to keep its output consistent. FastAPI validates and serializes the returned data according to that model, so fields outside the declared response model are not included in the API response.

## 🔌 API Endpoints

| Method | Endpoint | Description | Success status |
|---|---|---|---|
| `POST` | `/students` | Create a student | `201 Created` |
| `GET` | `/students` | Retrieve all students | `200 OK` |
| `GET` | `/students/{student_id}` | Retrieve one student by ID | `200 OK` |
| `PUT` | `/students/{student_id}` | Update a student's name | `200 OK` |
| `DELETE` | `/students/{student_id}` | Delete a student | `200 OK` |

Requests using a student ID that does not exist return **404 Not Found**. Invalid request data returns **422 Unprocessable Entity**.

## 🛠️ Technologies

- **Python** — application logic
- **FastAPI** — REST API framework
- **Pydantic** — request validation and response models
- **Uvicorn** — local ASGI server
- **Git & GitHub** — version control and project hosting

## 🚀 Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/huzaifa2612/student-management-api.git
cd student-management-api
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Install the dependencies**

```bash
python -m pip install fastapi uvicorn "pydantic>=2"
```

**4. Start the API**

```bash
uvicorn main:app --reload
```

The API runs locally at `http://127.0.0.1:8000`.

## 📝 Current Scope

Student records are stored in memory, so the data resets whenever the application restarts. A database, automated tests, and authentication are not part of the current implementation.

## 👨‍💻 Author

**Muhammad Huzaifa** · Computer Science Student

[GitHub Profile](https://github.com/huzaifa2612) · [Project Repository](https://github.com/huzaifa2612/student-management-api)

<div align="center">

*Built while learning Python backend development and REST API design.*

</div>
