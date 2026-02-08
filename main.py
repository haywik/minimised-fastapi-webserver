#minimised version from central, 28.jan.2026
#note: this is quite minimised tbf
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os,subprocess

user_of_program=str(subprocess.run("whoami",capture_output=True,text=True).stdout).replace('\n','')
os.chdir(f"/home/{user_of_program}/repo")

app=FastAPI()
tpl  = Jinja2Templates(directory="./templates")
static = app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/")
async def index(request: Request): return RedirectResponse(url="/home")


@app.get("/{path1:path}")
async def land(request: Request,path1 : str):
    if os.path.exists("./templates/"+path1+".html") == False: return RedirectResponse(url="/bad_path")
    return tpl.TemplateResponse((path1+".html"), {"request":request})




