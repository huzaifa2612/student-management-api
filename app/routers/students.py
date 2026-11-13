from fastapi import APIRouter, HTTPException

from app.schemas.student import (
    StudentCreate,
    StudentResponse,
    StudentListItem,
    StudentDeleteResponse
)

router = APIRouter(tags=["Students Management"])

students = {
    1: "Ali",
    2: "Ahmad",
    3: "Huzaifa"
}




@router.post("/students", status_code=201, response_model=StudentResponse)  # sif wohi field display hon gi jo response model ki class mai defined han 
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

@router.get("/students/{student_id}", response_model=StudentResponse)
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

@router.get("/students", response_model=list[StudentListItem])
def get_all_students():
    student_list=[]   #list   index         

    for student_id, name in students.items():
        student_list.append({     #list k andar dic
            "student_id": student_id,
            "name": name
        })

    return student_list

@router.put("/students/{student_id}", response_model=StudentResponse)
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

@router.delete("/students/{student_id}", response_model=StudentDeleteResponse)
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