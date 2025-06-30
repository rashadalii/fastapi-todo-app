from fastapi import FastAPI

app = FastAPI(title="FastAPI ToDo API")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI ToDo API!"}
