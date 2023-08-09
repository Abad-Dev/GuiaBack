from fastapi import FastAPI
from routes import create, relate, gets


app = FastAPI()
app.include_router(create.router)
app.include_router(relate.router)
app.include_router(gets.router)


@app.get('/')
def home():
    return{'200': 'OK'}


