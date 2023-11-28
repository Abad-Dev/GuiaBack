from fastapi import FastAPI
from routes import create, relate, gets, deletes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(create.router)
app.include_router(relate.router)
app.include_router(gets.router)
app.include_router(deletes.router)


@app.get('/')
def home():
    return{'200': 'OK'}


