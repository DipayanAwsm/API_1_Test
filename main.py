from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is live!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting": f"Hello, {name}!"}

print("Hi")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)