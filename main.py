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
                "data": [100, 120, 130, 150, 200, 250, 50]
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
                "data": [220, 230, 50, 200, 198, 190, 238]
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
        return templates.TemplateResponse("widget_partials/_dashboard_prospect_widget.html",
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
            "widget_partials/_dashboard_sales_type_widget.html",
            {"request": request, "sales_data": sales_data}
        )


# Sample sale data
@app.get("/widget/sales-purchase", response_class=HTMLResponse)
async def sales_purchase_widget(request: Request):
    sales_purchase_data = [
        {"month": "Jan", "sale": 100, "purchase": 50},
        {"month": "Feb", "sale": 200, "purchase": 150},
        {"month": "Mar", "sale": 50, "purchase": 100},
        {"month": "Apr", "sale": 160, "purchase": 200},
        {"month": "May", "sale": 250, "purchase": 180},
        {"month": "June", "sale": 105, "purchase": 200},
        {"month": "July", "sale": 200, "purchase": 500},
        {"month": "August", "sale": 650, "purchase": 50},
    ]
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("widget_partials/_dashboard_sales_purchase_widget.html",
                                          {"request": request, "sales_purchase_data": sales_purchase_data}
                                          )


@app.get("/widget/countries-sales-data", response_class=HTMLResponse)
async def countries_sales_widget(request: Request):
    countries_sales_data = [
        {"country": "USA", "month": "Jan", "income": 10000},
        {"country": "USA", "month": "Feb", "income": 12000},
        {"country": "USA", "month": "Mar", "income": 9000},
        {"country": "USA", "month": "Apr", "income": 15000},
        {"country": "USA", "month": "May", "income": 16000},
        {"country": "USA", "month": "Jun", "income": 17000},
        {"country": "Canada", "month": "Jan", "income": 8000},
        {"country": "Canada", "month": "Feb", "income": 9000},
        {"country": "Canada", "month": "Mar", "income": 8500},
        {"country": "Canada", "month": "Apr", "income": 11000},
        {"country": "Canada", "month": "May", "income": 10500},
        {"country": "Canada", "month": "Jun", "income": 11500},
        {"country": "UK", "month": "Jan", "income": 7000},
        {"country": "UK", "month": "Feb", "income": 7500},
        {"country": "UK", "month": "Mar", "income": 8000},
        {"country": "UK", "month": "Apr", "income": 9500},
        {"country": "UK", "month": "May", "income": 10000},
        {"country": "UK", "month": "Jun", "income": 11000},
        {"country": "Germany", "month": "Jan", "income": 6000},
        {"country": "Germany", "month": "Feb", "income": 6500},
        {"country": "Germany", "month": "Mar", "income": 7000},
        {"country": "Germany", "month": "Apr", "income": 8500},
        {"country": "Germany", "month": "May", "income": 9000},
        {"country": "Germany", "month": "Jun", "income": 9500},
        {"country": "France", "month": "Jan", "income": 5000},
        {"country": "France", "month": "Feb", "income": 5500},
        {"country": "France", "month": "Mar", "income": 6000},
        {"country": "France", "month": "Apr", "income": 7500},
        {"country": "France", "month": "May", "income": 8000},
        {"country": "France", "month": "Jun", "income": 8500},
    ]

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("widget_partials/_dashboard_countries_sales_widget.html",
                                          {"request": request, "countries_sales_data": countries_sales_data}
                                          )


@app.get("/widget/location-quantity-widget", response_class=HTMLResponse)
async def location_quantity_widget(request: Request):
    quantity_by_location_data = [
        {"location": "America", "quantity": 100},
        {"location": "France ", "quantity": 200},
        {"location": "Canada", "quantity": 300},
        {"location": "Uk", "quantity": 400},
    ]

    if request.headers.get("HX-Request"):

        return templates.TemplateResponse("widget_partials/_dashboard_location_quantity_widget.html",
                                          {"request": request, "quantity_by_location_data": quantity_by_location_data})