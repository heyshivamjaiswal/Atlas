from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Atlas backend running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/version")
def version():
    return{
        "backend": "atlas",
        "version": "0.1"
    }