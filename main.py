from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import re
import os

app = FastAPI()

base = Path(__file__).parent
TEMPLATES_DIR = base / "templates"

tpl = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(base / "static")), name="static")


@app.get("/")
async def index(request: Request):
    return RedirectResponse(url="/home")

@app.get("/bad_path")
async def bad_path(request: Request):
    return tpl.TemplateResponse("bad_path.html", {"request": request}, status_code=404)

@app.get("/{path:path}")
async def serve_page(request: Request, path: str):
    if not re.fullmatch(r'[a-zA-Z0-9_\-/]+', path):
        return RedirectResponse("/bad_path")

    template_path = path + ".html"          # "about/team" → "about/team.html"
    full_path = TEMPLATES_DIR / template_path

    if not full_path.is_file() or not full_path.resolve().is_relative_to(TEMPLATES_DIR.resolve()):
        return RedirectResponse("/bad_path")

    return tpl.TemplateResponse(template_path, {"request": request})
