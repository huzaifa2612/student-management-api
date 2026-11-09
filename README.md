<div align="center">

# 🎓 Student Management API

### A REST API for managing and retrieving student records with Python and FastAPI

A beginner-friendly backend project built while learning API development. The current version stores sample student data in memory, provides a GET endpoint to retrieve a student by ID, handles missing student records with a 404 response, and configures CORS for a local frontend.

![Python](https://img.shields.io/badge/Python-Language-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Status](https://img.shields.io/badge/Project-In%20Development-orange?style=for-the-badge)

[Overview](#-overview) • [Features](#-feature-progress) • [API](#-available-api-endpoint) • [Setup](#-getting-started) • [Roadmap](#-remaining-work)

</div>

---

## 📌 Overview

The **Student Management API** is a learning project for understanding how to build backend services with **Python** and **FastAPI**. It currently uses a Python dictionary as temporary in-memory storage for student records.

The implemented endpoint retrieves a student using their ID. If the requested ID does not exist, the API returns an HTTP `404 Not Found` response.

> **Project status:** In development. The current version supports reading a student record. Create, update, delete, and input-validation features are still pending.

## ✨ Feature Progress

The table below reflects the current implementation status shown in the project and its supplied progress screenshot.

| Feature | Status |
|---|---|
| FastAPI application | ✅ Done |
| Student data storage (in-memory dictionary) | ✅ Done |
| GET student by ID | ✅ Done |
| 404 error handling for an unknown student ID | ✅ Done |
| CORS middleware configuration | ✅ Done |
| Swagger UI testing | ✅ Done |
| POST — Add Student | ⏳ Pending |
| PUT — Update Student | ⏳ Pending |
| DELETE — Remove Student | ⏳ Pending |
| Input validation | ⏳ Pending |

## 🔌 Available API Endpoint

### Get a student by ID

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/students/{student_id}` | Retrieve a student using their ID |

**Example request**

```http
GET http://127.0.0.1:8000/students/1
```

**Successful response — student found (`200 OK`)**

```json
{
  "student_id": 1,
  "name": "Ali",
  "message": "Student Found"
}
```

The current sample data contains these records:

| Student ID | Name |
|---:|---|
| 1 | Ali |
| 2 | Ahmad |
| 3 | Huzaifa |

**Error response — student not found (`404 Not Found`)**

For an ID that is not present in the dictionary, the API returns:

```json
{
  "detail": "Student not Found"
}
```

## 🛠️ Technologies Used

- **Python** — programming language
- **FastAPI** — API framework
- **CORSMiddleware** — cross-origin request configuration
- **Swagger UI** — interactive API documentation and testing interface provided by FastAPI
- **Uvicorn** — ASGI server used to run the application locally

## 🚀 Getting Started

Follow these steps to run the current version on your computer.

### 1. Clone the repository

```bash
git clone https://github.com/huzaifa2612/student-management-api.git
```

### 2. Open the project folder

```bash
cd student-management-api
```

### 3. Install the required packages

```bash
python -m pip install fastapi uvicorn
```

### 4. Run the API

```bash
python -m uvicorn main:app --reload
```

The API should now be available at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation & Testing

FastAPI provides interactive API documentation automatically when the application is running.

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Open Swagger UI, expand `GET /students/{student_id}`, select **Try it out**, enter a student ID such as `1`, and execute the request. Try an unknown ID, such as `99`, to see the 404 response.

## 🌐 CORS Configuration

The current code configures CORS for this frontend origin:

```text
http://localhost:3000
```

It sets `allow_credentials=False`, allows the methods `GET`, `POST`, `PUT`, and `DELETE` at the middleware level, and allows the `Content-Type` and `Authorization` headers.

**Note:** Allowing an HTTP method in CORS does not create an API route for that method. At present, the code implements only `GET /students/{student_id}`. The POST, PUT, and DELETE endpoints remain pending.

## 🗂️ Project Structure

```text
student-management-api/
│
├── main.py        # FastAPI application, sample data, GET endpoint and CORS setup
└── README.md      # Project documentation
```

## 🧭 Remaining Work

The following items are not implemented in the supplied version of the code and are listed as pending in the project progress screenshot:

1. **POST — Add Student:** create and store a new student record.
2. **PUT — Update Student:** update an existing student's information.
3. **DELETE — Remove Student:** delete a student record.
4. **Input validation:** validate incoming data and handle invalid input appropriately.

These are planned tasks, not current capabilities.

## 👨‍💻 Author

**Muhammad Huzaifa**  
Computer Science Student | Learning Python and Backend Development

- GitHub: [@huzaifa2612](https://github.com/huzaifa2612)
- Repository: [student-management-api](https://github.com/huzaifa2612/student-management-api)

---

<div align="center">

*Built as part of a hands-on journey into Python backend and API development.*

</div>
