from fastapi import FastAPI

app = FastAPI(
    title="Vision Inspector API",
)


@app.get("/")
def root():
    return {"message": "Vision Inspector API"}
