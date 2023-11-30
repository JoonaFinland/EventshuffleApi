from fastapi import FastAPI, APIRouter
from .core.config import AppSettings
from app.api.event import router as event_router
settings = AppSettings()

app = FastAPI(
    title="Event Shuffle API",
    version="1.0",
    description="Sample API to showcase \"good practices\".",
)
prefix_router = APIRouter(prefix=settings.BASE_URL)

@prefix_router.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(prefix_router)
app.include_router(event_router, prefix=f"{settings.BASE_URL}/event", tags=["event"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)