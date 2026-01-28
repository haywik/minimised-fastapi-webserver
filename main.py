#minimised version from central, 28.jan.2026
#note: this is quite minimised tbf
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os

app=FastAPI()
tpl  = Jinja2Templates(directory="./templates")
static = app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/")
async def index(request: Request): return RedirectResponse(url="/home")


@app.get("/{path:path}")
async def land(request: Request,path : str):
    if os.path.exists("./templates/"+(path+"html")) == False: return RedirectResponse(url="/bad_path")
    return tpl.TemplateResponse(file, {"request":request})




