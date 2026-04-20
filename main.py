import os

from dotenv import load_dotenv
from fastapi import FastAPI

from routers import items, users

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "FastAPI Project Task"),
    version="1.0.0",
    description="Sample FastAPI project with users and items CRUD endpoints.",
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI project is running"}
