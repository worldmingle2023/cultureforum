from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Greetings from Cloud commanders! This is culture forum"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
