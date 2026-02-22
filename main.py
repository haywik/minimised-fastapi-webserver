#minimised version from central, 28.jan.2026
#note: this is quite minimised tbf
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os,subprocess

app=FastAPI()
tpl  = Jinja2Templates(directory="__file__/templates")
static = app.mount("/static", StaticFiles(directory="__file__/static"), name="static")


@app.get("/")
async def index(request: Request): return RedirectResponse(url="/home")

@app.get("/{path1:path}")
async def land(request: Request,path1 : str):
    if os.path.exists("__file__/templates/"+Path(path1).absolute()+".html")) == False or ".." in path1:
        raise HTTPException(status_code=status.HTTP.404_NOT_FOUND)
        return RedirectResponse(url="/bad_path")
    return tpl.TemplateResponse((path1+".html"), {"request":request})




