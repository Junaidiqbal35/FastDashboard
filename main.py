import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse, JSONResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("dashboard.html", context)


@app.get("/widgets/data/without-graph", response_class=HTMLResponse)
async def widgets_data_view(request: Request):
    widgets_data_without_graph = [
        {
            "id": 1,
            "title": "Holding Days",
            "value": 365,
            "percentage": "12%",
            "average": "480 day average",
            "trend": "down"
        },
        {
            "id": 2,
            "title": "Retail Price",
            "value": "$23k",
            "percentage": "22%",
            "average": "$32K average Price",
            "trend": "up"
        }
    ]

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("widget_partials/_dashboard_widget_without_graph.html",
                                          {"request": request,
                                           "widgets_data_without_graph": widgets_data_without_graph})


@app.get("/widget/data/graph", response_class=HTMLResponse)
async def read_graph(request: Request):
    widget_data_with_line_graph = [
        {
            "id": 1,
            "type": "data",
            "title": "Category Web Views",
            "value": "300",
            "percentage": "8%",
            "trend": "up",
            "line_graph_data": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                "data": [100, 120, 130, 150, 200, 250, 300]
            }
        },
        {
            "id": 2,
            "type": "data",
            "title": "Category Sales",
            "value": "$238k",
            "percentage": "3%",
            "trend": "down",
            "line_graph_data": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                "data": [220, 230, 210, 200, 198, 190, 238]
            }
        }
    ]

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("widget_partials/_dashboard_widget_with_graph.html",
                                          {"request": request,
                                           "widgets_data_with_graph": widget_data_with_line_graph})


@app.get("/kpi-widget-data", response_class=HTMLResponse)
async def kpi_widget_categories_data(request: Request):
    kpi_widget_categories = {
        "Tea Pots Category": {
            "KPIs": [
                {
                    "title": "Current Qty Available",
                    "data": {
                        "six_months": {
                            "value": 453,
                            "percentage": "23%"
                        },
                        "two_years": {
                            "value": 453,
                            "percentage": "23%"
                        }
                    }
                },
                {
                    "title": "Qty on Website",
                    "data": {
                        "six_months": {
                            "value": 153,
                            "percentage": "13%"
                        },
                        "two_years": {
                            "value": 153,
                            "percentage": "13%"
                        }
                    }
                }
            ]
        }
    }
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("widget_partials/_dashboard_kpi_widget.html",
                                          {"request": request,
                                           "kpi_widget_categories": kpi_widget_categories})


@app.get("/widget/prospects", response_class=HTMLResponse)
async def prospects_widget(request: Request):
    prospects_widget_data = [
        {
            "name": "John Doe",
            "reason": "Interested in product demo",
            "rank": 1
        },
        {
            "name": "Jane Smith",
            "reason": "Requested a quote",
            "rank": 2
        },
        {
            "name": "Samuel Brown",
            "reason": "Follow-up meeting scheduled",
            "rank": 3
        },
        {
            "name": "Lucy Gray",
            "reason": "Downloaded whitepaper",
            "rank": 4
        }
    ]
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("widget_partials/_prospect_widget.html",
                                          {"request": request,
                                           "prospects_widget_data": prospects_widget_data})


@app.get("/widget/sales-type", response_class=HTMLResponse)
async def sales_widget(request: Request):
    sales_data = [
        {"type": "Retail", "amount": "$353k", "percentage": "76%"},
        {"type": "Trade", "amount": "$6k", "percentage": "21%"},
        {"type": "Distributor", "amount": "$500", "percentage": "8%"}
    ]
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse(
            "widget_partials/_sales_type_widget.html",
            {"request": request, "sales_data": sales_data}
        )
