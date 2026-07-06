from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.predict import router as predict_router
from app.core.config import OUTPUT_DIR

app = FastAPI(
    title="Vision Inspector API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
