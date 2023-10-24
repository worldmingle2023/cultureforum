from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Greetings from Cloud commanders! This is culture forum"}
