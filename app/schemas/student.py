from pydantic import BaseModel, Field, field_validator


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