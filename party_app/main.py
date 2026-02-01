from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path


app = FastAPI()

app.mount(
    "/party_app/static",
    StaticFiles(directory=Path(__file__).resolve().parent / "static"),
    name="static",
)
