from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Anonymous", "login at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! How are you doing today?"}