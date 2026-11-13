from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.students import router as students_router
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

students={  #dic  key-value
    1: "Ali",
    2: "Ahmad",
    3: "Huzaifa"
}


origins = [
    settings.frontend_origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    #	Allowed frontend URLs
    allow_credentials=False,   #Cookies/credentials allow karna
    allow_methods=["GET", "POST", "PUT", "DELETE"],   #Allowed HTTP methods
    allow_headers=["Content-Type", "Authorization"]   #Allowed request headers
)

# Register Student Router
app.include_router(students_router) 
# it connects all the registered endpoints of Student router to main FastAPI application