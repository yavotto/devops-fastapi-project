from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/info")
def info():
    return {
        "service": "devops-demo",
        "version": "1.0",
        "time": str(datetime.utcnow())
    }
