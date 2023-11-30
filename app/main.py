from fastapi import FastAPI
from .core.config import AppSettings

settings = AppSettings()

app = FastAPI()

@app.get("/")
def read_root():
    #return {"Hello": "World"}
    return settings.ALLOWED_CORS_ORIGINS


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)