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

@app.get("/{path1:path}")
async def land(request: Request, path1: str):
    if not re.fullmatch(r'[a-zA-Z0-9_\-/]+', path1):
        return RedirectResponse(url="/bad_path")

    resolved = (TEMPLATES_DIR / path1).resolve()
    file = resolved.with_suffix(".html")

    if not str(resolved).startswith(str(TEMPLATES_DIR.resolve())) or not file.exists():
        return RedirectResponse(url="/bad_path")

    if os.path.exists(str(Path(path1).resolve())+".html") == False:
        return RedirectResponse(url="/bad_path")
    else:
    	return tpl.TemplateResponse(path1 + ".html", {"request": request})
