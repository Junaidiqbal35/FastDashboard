import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("index.html", context)
