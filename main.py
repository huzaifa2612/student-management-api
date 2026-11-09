from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

students={
    1: "Ali",
    2: "Ahmad",
    3: "Huzaifa"
}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail= "Student not Found"
        )

    return{
        "student_id": student_id,
        "name": students[student_id],
        "message": "Student Found"
    }

origins=[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    #	Allowed frontend URLs
    allow_credentials=False,   #Cookies/credentials allow karna
    allow_methods=["GET", "POST", "PUT", "DELETE"],   #Allowed HTTP methods
    allow_headers=["Content-Type", "Authorization"]   #Allowed request headers
)