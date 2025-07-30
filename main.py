from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.api.server import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router)
