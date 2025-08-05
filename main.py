from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is live!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting": f"Hello, {name}!"}
