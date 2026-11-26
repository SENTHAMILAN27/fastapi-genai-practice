from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Senthu"}

@app.get("/students")
def get_students():
    return {"name": "Senthu", "age": 25}


@app.get("/health")
def health_check():
    return {"status": "ok"}

