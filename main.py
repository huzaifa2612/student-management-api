from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator

app=FastAPI()

students={  #dic  key-value
    1: "Ali",
    2: "Ahmad",
    3: "Huzaifa"
}

class StudentCreate(BaseModel):  #	Pydantic model create karta hai
    name: str = Field(min_length=2, max_length=50)
   # to remove spaces and empty strig    Advance Pydantic Validation

   # Check String
   #validator mode ha 4 execution modes
    @field_validator("name", mode="before")   #Name field validate karta hai    mode=before Normal field validation se pehle execute hota hai
    @classmethod                # Validator class method ke taur par execute hota hai
    def validate_name(cls, value):
        if isinstance(value, str):   # check if variable is of particular data type
            value=value.strip()

        return value    


# Check Number
    @field_validator("name", mode="after")
    @classmethod
    def validate_number(cls, value):
        result = any(char.isdigit() for char in value)

        if result:
            raise ValueError("Student name must not contain numbers")
        else:
            return value


    

class StudentResponse(BaseModel):
    student_id: int
    name: str
    message: str


class StudentListItem(BaseModel):
    student_id: int
    name: str


class StudentDeleteResponse(BaseModel):
    student_id: int
    message: str    

@app.post("/students", status_code=201, response_model=StudentResponse)  # sif wohi field display hon gi jo response model ki class mai defined han 
                                                          #us k illawa agar kuch return mai bhejin gy to to reutn nhi ho ga
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

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail= "Student not Found"
        )

    return{
        "student_id": student_id,
        "name": students[student_id],
        "message": "Student Found",
        "internal_note": "This should not reach the client"
    }

@app.get("/students", response_model=list[StudentListItem])
def get_all_students():
    student_list=[]   #list   index         

    for student_id, name in students.items():
        student_list.append({     #list k andar dic
            "student_id": student_id,
            "name": name
        })

    return student_list

@app.put("/students/{student_id}", response_model=StudentResponse)
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

@app.delete("/students/{student_id}", response_model=StudentDeleteResponse)
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