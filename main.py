from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app=FastAPI()

students={  #dic  key-value
    1: "Ali",
    2: "Ahmad",
    3: "Huzaifa"
}

class StudentCreate(BaseModel):  #	Pydantic model create karta hai
    name: str = Field(min_length=2, max_length=50)

@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    if students:
        new_id=max(students.keys())+1
    else:
        new_id=1    
    students[new_id]=student.name
    return{
        "student_id": new_id,
        "name": students[new_id],
        "message": "Student Created"
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

@app.get("/students")
def get_all_students():
    student_list=[]   #list   index         

    for student_id, name in students.items():
        student_list.append({     #list k andar dic
            "student_id": student_id,
            "name": name
        })

    return student_list

@app.put("/students/{student_id}")
def update_student(student_id:int, new_name:StudentCreate):
    if student_id not in students:
        raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

    students[student_id]=new_name.name
        

    return{
        "student_id": student_id,
        "name": new_name.name,
        "message": "Student Updated"    
    }    

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]

    return{
        "student_id": student_id,
        "message": "Student Deleted Successfully"
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