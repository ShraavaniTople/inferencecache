from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.inference.proxy import handle_inference

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "output": None})

@router.post("/infer", response_class=HTMLResponse)
async def infer(request: Request, prompt: str = Form(...)):
    result = await handle_inference(prompt)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "output": result["output"],
        "hash": result["hash"],
        "signature": result["signature"]
    })
