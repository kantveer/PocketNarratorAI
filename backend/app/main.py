from fastapi import FastAPI

app = FastAPI(
    title="PocketNarratorAI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "PocketNarratorAI"
    }