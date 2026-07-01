from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.predict import router as predict_router
from app.core.config import OUTPUT_DIR

app = FastAPI(
    title="Vision Inspector API",
)

app.mount(
    "/outputs",
    StaticFiles(directory=OUTPUT_DIR),
    name="outputs",
)

app.include_router(predict_router)


@app.get("/")
def root():
    return {"message": "Vision Inspector API"}
