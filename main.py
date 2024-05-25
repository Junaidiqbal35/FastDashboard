import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse, JSONResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("index.html", context)


@app.get("/sales/widget", response_class=HTMLResponse)
async def sales_by_countries_widget(request: Request):
    data = [
        {"country": "United States", "visits": 9763, "increase": "2.6%", "flag": "media/flags/united-states.svg"},
        {"country": "Canada", "visits": 8500, "increase": "3.1%", "flag": "media/flags/canada.svg"},
        {"country": "Germany", "visits": 9600, "increase": "1.8%", "flag": "media/flags/germany.svg"}
    ]

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("widget_partials/_sales_by_countries.html",
                                          {"request": request, "visits": data})


@app.get("/channels/widget", response_class=HTMLResponse)
async def channels_widget(request: Request):
    data = [
        {
            "icon": "media/svg/brand-logos/dribbble-icon-1.svg",
            "title": "Dribbble",
            "description": "Community",
            "progress_percentage": 65
        },
        {
            "icon": "media/svg/brand-logos/slack-icon.svg",
            "title": "Slack",
            "description": "Community",
            "progress_percentage": 80
        },

        {
            "icon": "media/svg/brand-logos/google-icon.svg",
            "title": "Google",
            "description": "Community",
            "progress_percentage": 90
        }

    ]
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("widget_partials/_channel_widget.html",
                                          {"request": request, "channels_data": data})
