from fastapi import FastAPI;

app = FastAPI();

@app.get("/my-fisrt-api")
def hello(name: str):
    return {"Hello ": name + "!"}