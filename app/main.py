from fastapi import FastAPI

from app.models import reclamation
from .routers import user, auth, reclamation
from .database import engine, get_db
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# Raouf : uncomment this line if you want to add a new model 
#         if you modify and existing model, you need alembic to update database
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Raouf : FIX IT Later after deploying the front end, allow only our web server instead of all "*"  
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(reclamation.router)

@app.get("/")
def root():
    return {"message": "Welcome to Doghello backend !"}
