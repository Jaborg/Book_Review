from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

application = FastAPI()

templates = Jinja2Templates(directory="templates")


@application.get("/")
async def index(request: Request):
    print('Ypoooo')
    return templates.TemplateResponse("frontpage.html", {"request": request})



@application.get("/information")
async def info(request: Request):


    return templates.TemplateResponse("information.html", {"request": request})



@application.get("/reviews")
async def review(request: Request):


    return templates.TemplateResponse("reviews.html", {"request": request})
