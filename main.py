from fastapi import FastAPI

app = FastAPI(title="LAB9 CI/CD API")


@app.get("/")
def read_root():
    return {"status": "ok", "message": "API FastAPI - LAB9 CI/CD"}


@app.get("/health")
def health():
    return {"status": "healthy"}
