from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.predict import router as predict_router
from app.core.config import OUTPUT_DIR, get_allow_origins

app = FastAPI(
    title="Vision Inspector API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allow_origins(),
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


@app.get("/health")
def health():
    return {"status": "ok!"}
