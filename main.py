from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import re

app = FastAPI()

base = Path(__file__).parent
TEMPLATES_DIR = base / "templates"

tpl = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(base / "static")), name="static")


@app.get("/")
async def index(request: Request):
    return RedirectResponse(url="/home")


@app.get("/{path1:path}")
async def land(request: Request, path1: str):
    if not re.fullmatch(r'[a-zA-Z0-9_\-/]+', path1):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    resolved = (TEMPLATES_DIR / path1).resolve()
    file = resolved.with_suffix(".html")

    if not str(resolved).startswith(str(TEMPLATES_DIR.resolve())) or not file.exists():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return tpl.TemplateResponse(path1 + ".html", {"request": request})
