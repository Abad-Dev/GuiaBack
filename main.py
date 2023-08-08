from fastapi import FastAPI
from routes import create


app = FastAPI()
app.include_router(create.router)


@app.get('/')
def home():
    return{'200': 'OK'}


